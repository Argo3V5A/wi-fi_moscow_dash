import dash
import json
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from transdata import preq

with open(r".\data\data-20191015T0100.json", 'r') as f:
    js = json.load(f)

fdf = pd.DataFrame.from_dict(js)
sdf = pd.read_csv(r"./data/data-9776-2020-12-21.csv", sep=';', encoding='cp1251')

data = preq(fdf.iloc[:, :13].copy())
sec_data = preq(sdf)

map_token = open("mapbox_token.txt").read()  # you will need your own token
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

map_center = {'lat': data['Lat'].values[0], 'lon': data['Lon'].values[0]}
fig = px.scatter_mapbox(data,
                        lat="Lat",
                        lon="Lon",
                        hover_name="Name",
                        hover_data=["District"],
                        color_discrete_sequence=["fuchsia"],
                        zoom=9,
                        height=500,
                        center=map_center,
                        title='Wi-fi в парках Москвы',
                        labels=dict(size=data['CoverageArea']),
                        size=data['CoverageArea'])

fig.update_layout(mapbox_style="dark", mapbox_accesstoken=map_token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# fig.show()

map_center2 = {'lat': sec_data['Lat'].values[0], 'lon': sec_data['Lon'].values[0]}
fig2 = px.scatter_mapbox(sec_data,
                         lat="Lat",
                         lon="Lon",
                         hover_name="Name",
                         hover_data=["District"],
                         color_discrete_sequence=["fuchsia"],
                         zoom=9,
                         height=500,
                         center=map_center2,
                         title='Wi-fi в парках Москвы',
                         labels=dict(size=sec_data['CoverageArea']),
                         size=sec_data['CoverageArea'])

fig2.update_layout(mapbox_style="dark", mapbox_accesstoken=map_token)
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# fig2.show()
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


app = dash.Dash(__name__)
app.title = "Wi-fi в паркам москвы: Understand Your Avocados!"

app.layout = html.Div([
    dcc.Graph(figure=fig)]
)

if __name__ == "__main__":
    app.run_server(debug=True,
                   host='127.0.0.1')
