from sync import getParsedData
import plotly.graph_objects as go
from ipywidgets import widgets
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import json
import sys
import glob
import subprocess
from datetime import datetime
import re
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

syncStateInt=False
globalThroughputMap={} #This is for gathering packet offset
def displayApp(dst):
    global globalThroughputMap
    entries = getParsedData(dst,-1,0,0)
    xData=[]
    yData=[]
    iter = 0
    for entry in entries:
        xData.append(entry["start"])
        yData.append(entry["y"])
        globalThroughputMap[iter]=entry
        iter = iter + 1
    trace1 = go.Scatter(x=xData, y=yData, mode='lines+markers')
    f = go.FigureWidget(data=[trace1],layout=go.Layout(title=dict(text='Throughput data'),barmode='overlay'))

    
    app.layout = html.Div([
        dcc.Interval(id='interval1', interval=1 * 1000, n_intervals=0),
        dcc.Graph(id='basic-interactions',figure=f),
        html.Div(id='hidden-div', style={'display':'none'}),
        html.Div(id='hidden-div2', style={'display':'none'})
    ])

selectTime=-1
packet=-1 
internalPacket=-1
@app.callback(
    dash.dependencies.Output('hidden-div2', 'children'),
    [dash.dependencies.Input('interval1', 'n_intervals')])
def update_interval(n):
    global packet
    global selectTime
    packetOffset=-1
    internalPacket=-1
    if os.path.exists("wiretodash.tmp"):
        with open("wiretodash.tmp","r") as files:
            packett = files.read()
        if packett != packet:
            packet=packett
            print("wire to dash packet ="+str(packet))
    if os.path.exists("internalTime.tmp"):
        with open("internalTime.tmp","r") as infile:
            selectedTime=infile.read()
        if selectTime != selectedTime:
            try:
                datetimeTarget=datetime.strptime(selectedTime, '%Y-%m-%dT%H:%M:%S') #2020-09-11 22:36:54
                for i in range(0,len(globalThroughputMap)):
                    datetimeObjCurr=datetime.strptime(globalThroughputMap[i]['start'], '%Y-%m-%dT%H:%M:%S')
                    if datetimeObjCurr < datetimeTarget:
                        packetOffset+=globalThroughputMap[i]['y']
                    else:
                        packetOffset+=globalThroughputMap[i]['y']
                        break
            except ValueError:
                try:
                    datetimeTarget=datetime.strptime(selectedTime, '%Y-%m-%dT%H:%M')
                    for i in range(0,len(globalThroughputMap)):
                        datetimeObjCurr=datetime.strptime(globalThroughputMap[i]['start'], '%Y-%m-%dT%H:%M:%S')
                        if datetimeObjCurr < datetimeTarget:
                            packetOffset+=globalThroughputMap[i]['y']
                        else:
                            packetOffset+=globalThroughputMap[i]['y']
                            break
                except:
                    print("invalid time format, please select the time cell")
                    selectTime = selectedTime
            
        if packetOffset != internalPacket:
            print("dash to wire packet ="+str(packetOffset))
            internalPacket = packetOffset
            with open("dashtowire.tmp","w") as files:
                files.write(str(packetOffset))
            selectTime = selectedTime


@app.callback(
    Output('hidden-div', 'children'),
    [Input('basic-interactions', 'clickData')])
def click_event_graph(hoverData):
    global globalThroughputMap
    packetOffset=0
    try:
        temp = hoverData["points"][0]
        startTime=temp['x']
        print(hoverData["points"])
        try:
            datetimeTarget=datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S') #2020-09-11 22:36:54
        except ValueError:
            datetimeTarget=datetime.strptime(startTime, '%Y-%m-%d %H:%M')
        for i in range(0,len(globalThroughputMap)):
            datetimeObjCurr=datetime.strptime(globalThroughputMap[i]['start'], '%Y-%m-%dT%H:%M:%S')
            if datetimeObjCurr < datetimeTarget:
                packetOffset+=globalThroughputMap[i]['y']
            else:
                packetOffset+=globalThroughputMap[i]['y']
                break
        # print(packetOffset)
        with open("dashtowire.tmp","w") as files:
            files.write(str(packetOffset))
        with open("internalTime.tmp","w") as outfile:
                outfile.write(datetimeTarget.strftime("%Y-%m-%dT%H:%M:%S"))
    except TypeError: #Starting up of app causes typeerror for no reason... bug
        return None



if sys.argv[1]:
    popen = subprocess.Popen(['netstat', '-lpn'],
                         shell=False,
                         stdout=subprocess.PIPE)
    (data, err) = popen.communicate()
    for line in data.decode().split("\n"):
        if re.match('^tcp.*8050.*python.*$',line):
            dataline=line
            temp=dataline.split("LISTEN")[1].strip()
            pid = temp.split("/")[0]
            subprocess.Popen(['kill', '-9', pid])

    projDir = sys.argv[1].split("ProjectData/")
    projName = projDir[1].split("/")[0]
    networkDataxyDir=projDir[0]+"ProjectData/"+projName 
    relevDir=glob.glob(networkDataxyDir+'/ecel-export_*')
    print(relevDir)
    displayApp(relevDir[0]+"/parsed/tshark/networkDataXY.JSON")
    app.run_server(debug=False, use_reloader=False) #port 8050 is default port





def time_to_packet(startTime):
    global packetOffset
    try:
        datetimeTarget=datetime.strptime(startTime, '%Y-%m-%dT%H:%M:%S') #2020-09-11 22:36:54
    except ValueError:
        datetimeTarget=datetime.strptime(startTime, '%Y-%m-%dT%H:%M')
    for i in range(0,len(globalThroughputMap)):
        datetimeObjCurr=datetime.strptime(globalThroughputMap[i]['start'], '%Y-%m-%dT%H:%M:%S')
        if datetimeObjCurr < datetimeTarget:
            packetOffset+=globalThroughputMap[i]['y']
        else:
            packetOffset+=globalThroughputMap[i]['y']
            break
        print(packetOffset)
    return packetOffset