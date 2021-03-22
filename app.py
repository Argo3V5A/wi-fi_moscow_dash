import dash
import json
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import visual
from transdata import clearData

#----------------------------------------------------------------------
with open(r".\data\data-20191015T0100.json", 'r') as f:
    js = json.load(f)

_first_df = pd.DataFrame.from_dict(js)
_second_df = pd.read_csv(r"./data/data-9776-2020-12-21.csv", sep=';', encoding='cp1251')

data = clearData(_first_df.iloc[:, :13].copy())
second_data = clearData(_second_df)

join_data = pd.concat([data, second_data], join='inner')

__map_token__ = open("mapbox_token.txt").read()  # you will need your own token

#----------------------------------------------------------------------

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
        html.H1(children="Public wi-fi Mocsow Analytics",
                className="header-title"),
        html.P(
            children="Analyz    e the behavior of avocado prices"
                     " and the number of avocados sold in the US"
                     " between 2015 and 2018",
        ),
        dcc.Graph(figure=fig),
        dcc.Graph(figure=fig2)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True,
                   host='127.0.0.1')
