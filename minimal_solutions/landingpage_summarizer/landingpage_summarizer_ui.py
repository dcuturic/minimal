import dash_bootstrap_components as dbc
from dash import html

def get_landingpage_summarizer_component():
    return dbc.Container([
        html.H2("Landingpage Summarizer"),
        html.P("UI Component for Landingpage Summarizer")
    ])
