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
    f = go.FigureWidget(data=[trace1],layout=go.Layout(title=dict(text='HelloWOrld'),barmode='overlay'))

    
    app.layout = html.Div([
        dcc.Interval(id='interval1', interval=1 * 1000, n_intervals=0),
        dcc.Graph(id='basic-interactions',figure=f),
        html.Div(id='hidden-div', style={'display':'none'}),
        html.Div(id='hidden-div2', style={'display':'none'})
    ])

packet=-1 
@app.callback(
    dash.dependencies.Output('hidden-div2', 'children'),
    [dash.dependencies.Input('interval1', 'n_intervals')])
def update_interval(n):
    global packet
    with open("wiretodash.tmp","r") as files:
        packett = files.read()
    if packett != packet:
        packet=packett
        print("Going to packet ="+str(packet))
        

        

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
    app.run_server(debug=False, use_reloader=True) #port 8050 is default port





