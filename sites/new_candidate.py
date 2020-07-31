# -*- coding: utf-8 -*-
from server import app, server
import dash_core_components as dcc
import dash_html_components as html
from modal import modal

layout = [
    html.Div(
        [
            html.Div(
                [
                    html.H6("New Candidate Entry", style={"paddingTop": "15px", "marginBottom": "30px"}),
                    html.P("Please select the job position:", style={"fontWeight":"700"}),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="position",
                                options=[{'label':x, 'value':x} for x in ['Junior HR Manager', 'Full Stack Developer', 'Database Engineer']],
                                value=None,
                                multi=False,
                                clearable=True,
                            )
                        ],
                        style={"width": "35%", "margin": "auto", "marginBottom": "50px"}
                    ),
                    html.Div(
                        [
                            html.P("Please fill in the Candidate Profile:", style={"fontWeight":"700"}),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("First Name:"),
                                            dcc.Input(
                                                id='profile_fn',
                                                type='text',
                                                value='',
                                                style={"textAlign": "center"}
                                            ),
                                        ],
                                        className="six columns"
                                    ),
                                    html.Div(
                                        [
                                            html.P("Last Name:"),
                                            dcc.Input(
                                                id='profile_ln',
                                                type='text',
                                                value='',
                                                style={"textAlign": "center"}
                                            ),
                                        ],
                                        className="six columns"
                                    ),
                                ],
                                className="row"
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("E-mail:"),
                                            dcc.Input(
                                                id='profile_email',
                                                type='text',
                                                value='',
                                                style={"textAlign": "center"}
                                            ),
                                        ],
                                        className="six columns"
                                    ),
                                    html.Div(
                                        [
                                            html.P("Phone:"),
                                            dcc.Input(
                                                id='profile_phone',
                                                type='text',
                                                value='',
                                                style={"textAlign": "center"}
                                            ),
                                        ],
                                        className="six columns"
                                    ),
                                ],
                                className="row"
                            )
                        ],
                        id="profile_div",
                        style={"display": "inline"}
                    ),
                    html.Div(
                        [
                            html.Br(),
                            html.Br(),
                            html.Span(
                                "Video Recording",
                                id="advanced_filter_button",
                                n_clicks=0,
                                className="button button--primary",
                                # style={
                                #     "height": "34",
                                #     "background": "#119DFF",
                                #     "border": "1px solid #119DFF",
                                #     "color": "white",
                                # },
                            ),
                        ],
                        id="recording_div",
                        className="row",
                        style={"display": "inline"}
                    ),
                    html.Div(
                        [
                            html.Br(),
                            html.Video(
                                src=app.get_asset_url('Prawin_Sugumaran_mock_interview.mp4'),
                                width='320px',
                                height='180px',
                                controls='True',
                            )
                        ],
                        className="row",
                        id="video_div",
                        style={"display": "none"},
                    ),
                    html.Div(
                        [
                            html.Br(),
                            html.Br(),
                            html.Span(
                                "Submit Candidate",
                                id="submit_button",
                                n_clicks=0,
                                className="button button--primary",
                                style={"backgroundColor": "#BBB"},
                                # style={
                                #     "height": "34",
                                #     "background": "#119DFF",
                                #     "border": "1px solid #119DFF",
                                #     "color": "white",
                                # },
                            ),
                        ],
                        id="submit_div",
                        n_clicks=0,
                    ),
                    html.Div(
                        [
                            html.H3(["Successfully Submited"]),
                        ],
                        style={"display": "none"},
                        id="success_div",
                        className="success"
                    ),
                    modal(),
                ],
                id="content",
                style={"height": "95%", "width": "98%"},
            )
        ],
        className="six columns chart_div",
        style={"minHeight": "800px", "textAlign":"center", "float":"None", "margin": "auto"}
    ),
]
