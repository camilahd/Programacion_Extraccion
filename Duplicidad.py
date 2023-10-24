# Camila Elizabeth Hernandez Alaniz
# 951
# Ejercicios Preprocesamiento duplicidad y valores Nulos.

import pandas as pd

#1.Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.
datos = pd.read_csv("archivos/surveys.csv")
def porcentaje(datos):
    nulos = datos.isnull()
    p = (nulos.sum()/len(nulos))
    return p
print(porcentaje(datos))

#2.Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
def duplicados(datos):
    duplicados= datos.duplicated()
    return duplicados.sum()
#print(duplicados(datos))


#+Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las
# columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original.
# Retornar la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.
"""
while True:
    p_max = float(input("Ingrese el maximo porcentaje que este entre 0 y 1:"))
    if p_max < 1 and p_max > 0 :
        break
    else:
        print("ingrese otro que este entre 0 y 1, por favor")
"""
def eliminar_original(datos, p_max):
    p_nulos = porcentaje(datos)
    columnas_eliminar = p_nulos[p_nulos >= p_max].index.tolist()
    datos.drop(columnas_eliminar, axis="columns", inplace=True)
    return columnas_eliminar
#print("Las columnas que se eliminaron fueron:", eliminar_original(datos, p_max))

#+ 4.Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y
# una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los
# valores nulos por el método especificado y retornar el DataFrame modificado.

columnas = ["hindfoot_length", "weight"]
"""
while True:
    cadena = input("Ingrese porque metodo quiere sustituir los valores faltantes:")
    if cadena in ['mean', 'bfill', 'ffill']:
        break
    else:
        print("La cadena debe ser 'mean', 'bfill' o 'ffill'")
"""
def sustituir(datos, columnas, cadena):
    prom = datos[columnas].mean()
    if cadena == "mean" :
        datos_sustituidos = datos.fillna(prom)
    elif cadena == "bfill" :
        datos_sustituidos = datos.bfill()
    elif cadena == "ffill" :
        datos_sustituidos = datos.ffill()
    return datos_sustituidos, porcentaje(datos_sustituidos)
#print("DataFrame modificado:\n", sustituir(datos, columnas, cadena))


#+ 5.Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame
# Original. Debe retornar la cantidad de renglones eliminados.
def renglones_eliminar(datos):
    eliminar_duplicados= datos.drop_duplicates()
    renglones = len(datos) - len(eliminar_duplicados)
    return renglones
#print(renglones_eliminar(datos))
