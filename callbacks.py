# -*- coding: utf-8 -*-
from server import app, server
from sites.new_candidate import layout

from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from flask import send_file
import re
import base64
import io
import pandas as pd
import numpy as np
import os
import xlsxwriter
import time

# @app.callback(
#     Output('profile_div', 'style'),
#     [Input('position', 'value')])
# def display_div(val):
#     if val == None:
#         return {"display": "none"}
#     else:
#         return {"display": "inline"}
#
# @app.callback(
#     Output('start_stop', 'children'),
#     [Input('loading_recording', 'loading_state')]
# )
# def loading(state):
#     if bool(state):
#         print('success')
#         return 'Stop Recording'
#     else:
#         return 'Start Recording'

@app.callback(
    Output('success_div', 'style'),
    [Input('submit_button', 'n_clicks')],
)
def contents(n):
    if n == 0:
        return {"display": "none"}
    else:
        return {"display": "block"}

@app.callback(
    [Output('start_stop', 'children'),
    Output('recording_app_div', 'style'),
    Output('loader_div', 'style'),
    Output('start_stop', 'className'),
    Output('video_div', 'style')],
    [Input('start_stop', 'n_clicks')],
    [State('start_stop', 'children')]
)
def recording(n, x):
    if n == 0:
        return ['Start Recording', {'display': 'inline'}, {'display': 'none'}, "button button--primary", {'display': 'none'}]
    else:
        if x == 'Start Recording':
            return ['Stop Recording', {'display': 'none'}, {'display': 'inline'}, "button button--primary red", {'display': 'none'}]
        else:
            return ['Start Recording', {'display': 'inline'}, {'display': 'none'}, "button button--primary", {'display': 'inline'}]

@app.callback(
    Output('submit_button', 'style'),
    [Input('profile_fn', 'value'),
    Input('profile_ln', 'value'),
    Input('profile_email', 'value'),
    Input('profile_phone', 'value'),
    Input('position', 'value'),
    Input('video_div', 'style')])
def display_div(val1, val2, val3, val4, val5, vid):
    if all([bool(val1), bool(val2), bool(val3), bool(val4), bool(val5), bool(vid['display'] == 'inline')]):
        return {"cursor": "select"}
    else:
        return {"cursore": "default", "backgroundColor": "#BBB"}

# hide/show modal
@app.callback(
    Output("advanced_filter_window", "style"),
    [Input("advanced_filter_button", "n_clicks")]
)
def display_opportunities_modal_callback(n):
    if n > 0:
        return {"display": "block"}

    return {"display": "none"}

# reset to 0 add button n_clicks property
@app.callback(
    Output("advanced_filter_button", "n_clicks"),
    [Input("advanced_filter_close", "n_clicks"),
    Input("apply_other_filter", "n_clicks")]
)
def close_modal_callback(n, n2):
    return 0
