import pandas as pd
import numpy as np

transacciones = [
    {"cliente": "Cliente1", "monto": 100, "fecha": "2024-03-01"},
    {"cliente": "Cliente2", "monto": 150, "fecha": "2024-03-02"},
    {"cliente": "Cliente3", "monto": 200, "fecha": "2024-03-03"},
    {"cliente": "Cliente1", "monto": 120, "fecha": "2024-03-04"},
    {"cliente": "Cliente4", "monto": 80, "fecha": "2024-03-05"},
    {"cliente": "Cliente2", "monto": 90, "fecha": "2024-03-06"},
    {"cliente": "Cliente5", "monto": 300, "fecha": "2024-03-07"},
    {"cliente": "Cliente3", "monto": 250, "fecha": "2024-03-08"},
    {"cliente": "Cliente1", "monto": 180, "fecha": "2024-03-09"},
    {"cliente": "Cliente6", "monto": 200, "fecha": "2024-03-10"}
]

df_transacciones = pd.DataFrame(transacciones)

print(df_transacciones)
#print(df_transacciones['monto'].describe())

suma = sum(df_transacciones['monto'])
print(suma)

conjunto_transaccion = set(df_transacciones['cliente'])
print(conjunto_transaccion)