
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

def get_table_from_url(url, tickerName):
  response = requests.get(url)
  response.encoding = 'latin1'  # Cambia a 'latin1' para manejar caracteres especiales en español

  # Usa pandas para leer las tablas desde el contenido HTML
  tables = pd.read_html(response.text)

  # Selecciona la primera tabla
  df = tables[0]


  #0 	Fecha 	Apertura 	Máximo 	Mínimo 	Cierre 	Volumen
  df = df.drop(index=0)
  new_col = 'Cierre'+'_'+tickerName

  df.rename(columns={0: 'Fecha', 4: new_col}, inplace=True)

  df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%y')
  df[new_col] = df[new_col].replace({',': ''}, regex=True).astype(float)

  return df[['Fecha', new_col]]

def getDfArbitraje():
  url1 = 'https://clasico.rava.com/empresas/precioshistoricos.php?e=GD30D'
  df1  = get_table_from_url(url1, 'GD30D')

  url2 = 'https://clasico.rava.com/empresas/precioshistoricos.php?e=AL30D'
  df2  = get_table_from_url(url2, 'AL30D')

  df = pd.merge(df1, df2, on='Fecha')

  df['ratio'] = df['Cierre_GD30D']/df['Cierre_AL30D']

  media = df['ratio'].mean()
  destd = df['ratio'].std()

  df['media'] = media
  df['std_inf'] = media - destd
  df['std_sup'] = media + destd

  return df

