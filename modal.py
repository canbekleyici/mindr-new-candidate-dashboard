# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

# returns modal (hidden by default)
def modal():
    return html.Div(
        html.Div(
            [
                html.Div(
                    [

                        # modal header
                        html.Div(
                            [
                            html.Span(
                                "Select Video-Call Application",
                                style={
                                    "color": "#506784",
                                    "fontWeight": "bold",
                                    "fontSize": "20",
                                },
                            ),
                            html.Span(
                                "×",
                                id="advanced_filter_close",
                                n_clicks=0,
                                style={
                                    "float": "right",
                                    "cursor": "pointer",
                                    "marginTop": "0",
                                    "marginBottom": "17",
                                },
                            ),
                        ],
                        className="row",
                        style={"borderBottom": "1px solid #C8D4E3"},
                        ),
                        html.Br(),
                        html.Div(
                            [
                                html.Div(
                                    className="loader",
                                    id="loader",
                                ),
                            ],
                            style={"display": "none"},
                            id="loader_div",
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    id='recording_app',
                                    options=[{'label':x, 'value':x} for x in ['Skype']],
                                    value='Skype',
                                    multi=False,
                                    clearable=False,
                                ),
                            ],
                            style={"display": "inline", "height": "30px"},
                            id="recording_app_div",
                        ),
                        html.Br(),
                        # submit button
                        html.Div([
                            html.Span(
                                "Start Recording",
                                id="start_stop",
                                n_clicks=0,
                                className="button button--primary",
                                # style={
                                #     "background": "#119DFF",
                                #     "border": "1px solid #119DFF",
                                #     "color": "white",
                                # }
                            ),
                        ], style={"marginBottom": "10px"}),
                        # submit button
                        html.Div([
                            html.Span(
                                "Back",
                                id="apply_other_filter",
                                n_clicks=0,
                                className="button button--primary",
                                # style={
                                #     "background": "#119DFF",
                                #     "border": "1px solid #119DFF",
                                #     "color": "white",
                                # }
                            ),
                        ])
                    ],
                    className="modal-content",
                    style={"textAlign": "center"},
                )
            ],
            className="modal",
        ),
        id="advanced_filter_window",
        style={"display": "none"},
    )
