import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


def mapFigure(join_data: pd.DataFrame, token: str) -> go:
    """Получаем dataframe
    Ставим точки на карте Москвы с публичными Wi-Fi в парках и публичным местах
    Возвращаем plotly.graph_objs"""

    map_center = {'lat': 55.76, 'lon': 37.62}
    mapFig = px.scatter_mapbox(join_data,
                               lat="Lat",
                               lon="Lon",
                               hover_name="Name",
                               hover_data=["District", 'CoverageArea'],
                               color='AdmArea',
                               zoom=11,
                               height=500,
                               width=1200,
                               center=map_center,
                               title='Wi-fi в парках Москвы')
    # TODO labels = join_data['CoverageArea'],
    # TODO size = size_marker) подобрать размер маркеров к масштабу

    mapFig.update_layout(mapbox_style="light", mapbox_accesstoken=token)
    mapFig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return mapFig


def treemapFigure(join_data: pd.DataFrame) -> go:
    treemap = px.treemap(join_data, path=['AdmArea', 'District'],
                         values=join_data['Name'].index,
                         color=join_data['District'],
                         hover_data=['District'],
                         width=1200,
                         height=500)
    return treemap
