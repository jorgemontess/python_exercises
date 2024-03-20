'''

Imagina que trabajas para una empresa de comercio electrónico y te han proporcionado un conjunto 
de datos en forma de diccionario que contiene información sobre las transacciones de los clientes. 
Quieren que realices un análisis básico para comprender mejor el comportamiento de compra de los clientes.

Problema: Utiliza Pandas para responder a las siguientes preguntas sobre las transacciones:

- ¿Cuántas transacciones hay en total?  --> Hay en total 10 transacciones

- ¿Cuál es el monto total de todas las transacciones? --> El monto total de las transacciones es 1670

- ¿Cuántos clientes únicos han realizado transacciones? --> 6 Clientes unicos han realizado transacciones 


'''

import pandas as pd

# Nuestro DataSet
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
# Convirtiendo el diccionario (Dataset) en un DataFrame de Pandas
df_transacciones = pd.DataFrame(transacciones)
print(df_transacciones)

# Pregunta: ¿Cuántas transacciones hay en total?
# Respuesta: Hay en total 10 transacciones
transacciones_total = len(df_transacciones['monto'])
print(f'El total de transacciones es: {transacciones_total}')


#Pregunta: ¿Cuál es el monto total de todas las transacciones?
# El monto total de las transacciones es 1670
monto_total = df_transacciones['monto'].sum()          # Suma con el Metodo sum de Pandas
print(f'El monto total de todas las transacciones es: {monto_total}')



# Pregunta: ¿Cuántos clientes únicos han realizado transacciones?
# Respuesta: 6 Clientes unicos han realizado transacciones 
conjunto_transaccion = set(df_transacciones['cliente'])
print(f'Los clientes unicos que realizaron transacciones fueron: {len(conjunto_transaccion)}')