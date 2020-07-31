# -*- coding: utf-8 -*-
from server import app, server
from sites.new_candidate import layout
import dash_core_components as dcc
import dash_html_components as html

app.layout = html.Div(
    [
        # header
        html.Div([

            html.Div(
                html.Img(src=app.get_asset_url('logo.png') ,height="50%")
                ,style={"margin":"auto","paddingTop":"20px","height":"70%","width":"100px"})
        ],
        className="row header",
        style={"backgroundColor":"#27303A", "marginBottom": "30px"}
        ),
        html.Div(
            layout,
            id="full_content",
            className="row",
            style={
                "marginBottom": "5px",
                "textAlign": "center",
            }
        ),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet")
    ]
)

import callbacks

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=5001)
