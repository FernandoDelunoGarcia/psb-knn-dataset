import os
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def LoadDataset(filename):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        return df
    
    raise Exception("Invalid filename!")

def Create2DFigure(dataset, class_name, x_column, y_column, title):
    classes = dataset["class"].unique()
    traces = []
    template = '<br><b>' + x_column + '<b>: %{x}' + '<br><b>' + y_column + '<b>: %{y}'

    for c in classes:
        df_class = dataset.loc[dataset["class"] == c]
        trace = go.Scatter(name = class_name["class_name"].iloc[c-1], x = df_class[x_column], y = df_class[y_column], mode="markers", hovertemplate=template, marker=dict(size=4))
        traces.append(trace)
    
    layout = go.Layout(title=title, xaxis_title=x_column, yaxis_title=y_column)    
    fig = go.Figure(data = traces, layout=layout)

    return fig

def Create3DFigure(dataset, class_name, x_column, y_column, z_column, title):
    classes = dataset["class"].unique()
    traces = []
    template = '<br><b>' + x_column + '<b>: %{x}' + '<br><b>' + y_column + '<b>: %{y}' + '<br><b>' + z_column + '<b>: %{z}'

    for c in classes:
        df_class = dataset.loc[dataset["class"] == c]
        trace = go.Scatter3d(name = class_name["class_name"].iloc[c-1], x = df_class[x_column], y = df_class[y_column], z = df_class[z_column], mode="markers", hovertemplate=template, marker=dict(size=4))
        traces.append(trace)
    
    layout = go.Layout(title=title, scene = dict(xaxis_title=x_column, yaxis_title=y_column,zaxis_title=z_column), width=700)    
    fig = go.Figure(data = traces, layout=layout)

    return fig

def GetFigures2D():
    figs_2d_tbl = [
        {"x":"pf", "y":"p", "title":"P x PF"},
        {"x":"pf", "y":"qf", "title":"QF x PF"},
        {"x":"pf", "y":"vf", "title":"VF x PF"}
    ]

    return figs_2d_tbl

def GetFigures3D():
    figs_3d_tbl = [
        {"x":"pf", "y":"p", "z": "qf", "title":"P x PF x QF"}
    ]

    return figs_3d_tbl