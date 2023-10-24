# Camila Elizabeth Hernandez Alaniz
# 951
# Ejercicios Preprocesamiento Normalización.

import pandas as pd

#+ 1. Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame y otro parámetro
# que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.

datos = pd.DataFrame({
    "Nombre" : ["Raul", "Maria", "Juan", "Selena"],
    "Estatura": [160, 170, 180, 190],
    "Peso": [60, 70, 80, 90]
})
columnas = ["Estatura", "Peso"]

# X= (xi - min) /(max - min)
def min_max(datos, columnas):
    for i in columnas:
        min = datos[i].min()
        max = datos[i].max()
        datos[i] = (datos[i] - min) / (max - min)
    return datos
#print(min_max(datos, columnas))


#+ 2.Realizar una función que normalice los datos usando Z-Score que reciba como parámetro un DataFrame y otro parámetro
# que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.

# X= (Xi - promedio) / std
def Z_Score(datos, columnas):
    for i in columnas:
        media = datos[i].mean()
        desviacion_estandar = datos[i].std()
        datos[i] = (datos[i] - media) / desviacion_estandar
    return datos
#print(Z_Score(datos, columnas))


#+ 3. Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y otro
# parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.

# X= (Xi) / max
def escalado_simple(datos, columnas):
    for i in columnas:
        max = datos[i].max()
        datos[i] = datos[i] / max
    return datos
print(escalado_simple(datos, columnas))