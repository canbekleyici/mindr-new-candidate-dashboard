# -*- coding: utf-8 -*-
from flask import Flask
from dash import Dash
import logging

server = Flask(__name__)
app = Dash(__name__, server=server)
app.title = "mindR - Recording Interface"

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')
