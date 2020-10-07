from sync import getParsedData
import plotly.graph_objects as go
from ipywidgets import widgets
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import json


# import plotly.io as pio
# print(pio.renderers)
# exit()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dest = "ecel-export_1599863833/parsed/tshark/networkDataXY.JSON"
projHome = "/home/kali/eceld-netsys/ProjectData/"

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

syncStateInt=False
globalAuditMap={}
globalKeyPressMap={}
globalThroughputMap={} #This approach will be mem intensive if large data sets, fix this (perhaps find the line with specific id)
def displayApp(dst):
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
    # entries = getParsedData("ProjectData/new/ecel-export_1599863833/parsed/auditd/auditdData.JSON",-1,0,0)
    # keypressentries = getParsedData("ProjectData/new/ecel-export_1599863833/parsed/pykeylogger/keypressData.JSON",-1,0,0)
    # xData=[]
    # yData=[]
    # # zData=[]
    # iter = 0
    # for entry in entries:
    #     # xData.append(entry["start"])
    #     # yData.append(entry["auditd_id"])
    #     # zData.append(entry["content"])
    #     globalAuditMap[iter]=entry
    #     iter = iter + 1
    # xData=[]
    # yData=[]
    # iter = 0
    # for entry in keypressentries:
    #     # xData.append(entry["start"])
    #     # yData.append(entry["content"])
    #     globalKeyPressMap[iter]=entry
    #     iter = iter + 1
    # trace2 = go.Scatter(x=xData, y=yData, mode='lines+markers')
    f = go.FigureWidget(data=[trace1],layout=go.Layout(title=dict(text='HelloWOrld'),barmode='overlay'))
    # f2 = go.Figure(data=[go.Table(header=dict(values=['Start', 'ID',"content"]),
    #              cells=dict(values=[xData,yData,zData]))
    #                  ])
                     #go.FigureWidget(data=[trace2],layout=go.Layout(title=dict(text='HelloWOrld2'),barmode='overlay'))
    # scatter = f.data[0]
    # scatter.on_click(update_point)
    # # container = widgets.HBox()
    # # widgets.VBox([container])j
    # f.show(renderer="browser")
    # f= go.FigureWidget()
    # f
    
    app.layout = html.Div([
        # dcc.Checklist(id="syncstate",
        #     options=[
        #         {'label': 'Sync?', 'value': 'SyncEnabled'}],
        #     labelStyle={'display': 'inline-block'}
        # ),
        dcc.Graph(id='basic-interactions',figure=f),
        
        # dash_table.DataTable(id="next",columns=[{"name": i, "id": i} for i in ['start','auditd_id','content']],data = entries),
        # dash_table.DataTable(id="next2",columns=[{"name": i, "id": i} for i in ['start','keypresses_id','content']],data = keypressentries),
        # dcc.Table(id='next',figure=f2),
        # html.Div(className='row', children=[
        #     html.Div([
        #         dcc.Markdown("""
        #             **Hover Data**

        #             Mouse over values in the graph.
        #         """),
        #         html.Pre(id='hover-data', )
        #     ], className='three columns')
        # ]),
        # html.Div(className='row', children=[
        #     html.Div([
        #         dcc.Markdown("""
        #             **Hover Data**

        #             Mouse over values in the graph.
        #         """),
        #         html.Pre(id='hover-data2', )
        #     ], className='three columns')
        # ]),
        html.Div(id='hidden-div', style={'display':'none'}),
        html.Div(id='hidden-div2', style={'display':'none'})
    ])
    

@app.callback(
    Output('hidden-div', 'children'),
    [Input('basic-interactions', 'clickData')])
def click_event_graph(hoverData):
    # 'points': [{'curveNumber': 0, 'pointNumber': 7, 'pointIndex': 7, 'x': '2020-09-11 22:37:01', 'y': 27}]}
    # global syncStateInt
    # if not syncStateInt:
    #     return
    try:
        temp = hoverData["points"][0]
        temp2 = temp['pointIndex']
        # if temp2 > len(globalAuditMap.keys())-1:
        #     temp2 = list(globalAuditMap.keys())[-1] #Last valid element
        print(temp2)
        # dictt = {
        #     "row": temp2,
        #     "column": 0,
        #     #   "row_id": df.country[row],
        #     #   "column_id": df.columns[column]
        # }
        # if temp2 > len(globalKeyPressMap.keys())-1:
        #     temp2 = list(globalKeyPressMap.keys())[-1] #Last valid element
        # print(temp2)
        # dictt2 = {
        #     "row": temp2,
        #     "column": 0,
        #     #   "row_id": df.country[row],
        #     #   "column_id": df.columns[column]
        # }
        # selCells=[dictt]
        # selCells2=[dictt2]
        # return dictt,selCells,selCells2 #str(temp["pointIndex"]),
    except TypeError: #Starting up of app causes typeerror for no reason... bug
        return None

# syncStateInt=False
# @app.callback(
#     Output('hidden-div', 'children'),
#     [Input('syncstate', 'value')])
# def display_syncStat(hoverData):
#     global syncStateInt
#     if hoverData:
#         syncStateInt = True
#     else:
#         syncStateInt = False
#     print(syncStateInt)
    
# @app.callback(
#     Output('hidden-div2', 'children'),
#     [Input('next', 'active_cell')])
# def click_event_table(hoverData):
#     try:
#         return str(globalAuditMap[hoverData["row"]])
#     except TypeError:
#         pass
#     except KeyError:
#         # print(list(globalAuditMap.keys())[-1])
#         return str(list(globalAuditMap.keys())[-1])
# @app.callback(
#     [
#         Output('datatable-row-ids', 'active_cell'),
#         Output('country', 'children'),
#         Output('key', 'children'),
#         Output('value', 'children'),
#     ],
#     [
#         Input('df_row', 'value'),
#         Input('df_column', 'value'),
#     ]
# )
# def update_active_cell(row, column):
#     row = 0 if row is None else row
#     column = 0 if column is None else column
#     dict = {
#       "row": row ,
#       "column": column,
#       "row_id": df.country[row],
#       "column_id": df.columns[column]
#     }
#     return dict, '{}\'s '.format(df.country[row]),  '{}:'.format(df.columns[column]), df.iat[row, column]


displayApp("/home/kali/eceld-netsys/ProjectData/new/ecel-export_1599863833/parsed/tshark/networkDataXY.JSON")
app.run_server(debug=True, use_reloader=True)





