import pandas as pd
import matplotlib as plt

datos_ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Electrónicos': [10000, 12000, 13000, 11000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000],
    'Ropa': [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500],
    'Hogar': [6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500]
}


df_ventas = pd.DataFrame(datos_ventas)
print(df_ventas)