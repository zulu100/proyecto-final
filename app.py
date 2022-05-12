# Se llamar las librerias
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go

# Declarar objetos principales
app = Dash(__name__)

# Cargar la base de datos
def serve_layout():
  df = pd.read_excel('data.xlsx')
  return html.Div([html.H1(df['Titulo']),
                       html.Div(df['Noticia1']),
                       html.Div(df['Noticia2'])])                
#funcion principal
app.layout = serve_layout

if __name__ == '__main__':
  #Cargar el objeto principal a todas las interfaces de red en el puerto 80
  app.run_server(host='0.0.0.0',port=80)
