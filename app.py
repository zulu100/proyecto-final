# Se llamar las librerias
from dash import Dash, html, dcc 
import plotly.graph objs as go
import pandas as pd

# Declarar objetos principales
app = Dash(__name__)

# Cargar la base de datos
def serve_layout():
df = pd.read_excel('datanot.xlsx')
return html.Div([html.H1(df['Titulo']),
                 html.Div(df['Noticia1']),
                 html.Div(df['Noticia2'])])
                 
# Declaro metodos principales
app.layout =serve_layout

if__name__== '__main__':
#ejecuto el objeto dash en todas las interfaces
app.run_server(host='0,0,0,0',port=80)
  
