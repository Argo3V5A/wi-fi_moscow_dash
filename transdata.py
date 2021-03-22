import pandas as pd


def clearData(df: pd.DataFrame) -> pd.DataFrame:
    """
    Получает dataframe созданные из json с данными о публичный wi-fi г.Москвы
    Возвращает dataframe готовый к визуализации
    """
    df.rename({'Longitude_WGS84': 'Lon', 'Latitude_WGS84': 'Lat'}, axis=1, inplace=True)
    df[['Lat', 'Lon', 'CoverageArea']] = df[['Lat', 'Lon', 'CoverageArea']].apply(pd.to_numeric, errors="coerce")
    df.dropna(subset=['Lat', 'Lon', 'global_id'], inplace=True)
    df.set_index(df['global_id'].astype(int), inplace=True)
    df.sort_index(inplace=True)
    df.drop(columns='global_id', axis=1, inplace=True)
    return df.copy()
