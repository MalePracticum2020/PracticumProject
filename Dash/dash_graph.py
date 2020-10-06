import os
import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import threading


def run_dash(data, format):
    app = dash.Dash()

    app.layout = html.Div(children=[
        html.H1(children='Traffic Throughput'),

        dcc.Graph(
            id='example-graph',
            figure=data,

        )
    ]
    )
    app.run_server(debug=False)


if __name__ == '__main__':
    basePath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_json(basePath + '/throughput.json')
    print(df)
    fig = px.line(df, x="traffic_xy_id", y="y")
    threading.Thread(target=run_dash, args=(fig, "Data Visualization"), daemon=True).start()

    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.load(QUrl("http://localhost:8050/"))
    web.show()
    sys.exit(app.exec_())
