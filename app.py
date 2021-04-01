import dash
import json
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import visual
import setting
from transdata import clearData

# ----------------------------------------------------------------------
with open(r".\data\data-20191015T0100.json", 'r') as f:
    js = json.load(f)

__first_df__ = pd.DataFrame.from_dict(js)
__second_df__ = pd.read_csv(r"./data/data-9776-2020-12-21.csv", sep=';', encoding='cp1251')

data = clearData(__first_df__.iloc[:, :13].copy())
second_data = clearData(__second_df__)
join_data = pd.concat([data, second_data], join='inner')

api = setting.Dostup()
__map_token__ = api.MY_API_TOKEN['mapbox_token']  # you will need your own token

# ----------------------------------------------------------------------

fig = visual.mapFigure(join_data, __map_token__)
fig2 = visual.treemapFigure(join_data)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Public Wi-fi Moscow: Know the freebie by sight!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📶", className="header-emoji"),
                html.H1(
                    children="Public Wi-fi Moscow", className="header-title"
                ),
                html.P(
                    children="Открытые данные о точкам Wi-Fi г. Москва."
                             " Более 4000 т. точек в парках и публичных местах."
                             " Практически все точки имеют покрытие в 50м!",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure=fig,
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure=fig2,
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True,
                   host='127.0.0.1')
