# Camila Elizabeth Hernandez Alaniz
# 951
# meta 2.3
import pandas as pd

data = pd.read_csv("archivos/titanic.csv")
data = pd.DataFrame(data)

# Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.
def porcentaje(data):
    porcentaje = ((data.isnull().sum()/len(data))*100).round(2)
    return porcentaje
#print(porcentaje(data))



# Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
def valor_dup(data):
    duplicados = data.duplicated().sum()
    if duplicados == 0:
        print("El dataframe no tiene valores duplicados")
    else:
        return duplicados
#print(valor_dup(data))



# Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las columnas
# que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original. Retornar la lista
# nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.
def eliminar_columnas(data, max_porcentaje):
    if not 0 <= max_porcentaje <= 1:
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1")
    columnas = data.columns[data.isnull().sum()/len(data) >= max_porcentaje]
    data = data.drop(columns=columnas)
    return columnas
#print(eliminar_columnas(data, 0.6))



# Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y
# una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los
# valores nulos por el método especificado y retornar el DataFrame modificado.
def sustituir(data, columnas, metodo):
    # Validar
    metodos_validos = ["mean", "bfill", "ffill"]
    if metodo not in metodos_validos:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'")
    for columna in columnas:
        if columna not in data.columns:
            print(f"La columna {columna} no existe en el DataFrame.")
            continue
        if metodo == "mean":
            rellenar = data[columna].mean()
        elif metodo == "bfill":
            rellenar = data[columna].bfill()
        elif metodo == "ffill":
            rellenar = data[columna].ffill()
        data[columna].fillna(rellenar, inplace=True)
    return data
#print(sustituir(data, ["Cabin"] , "bfill"))
#print(data["Cabin"].isnull().sum())



# Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original.
# Debe retornar la cantidad de renglones eliminados.
def eliminar(data):
    r_antes = len(data)
    data.drop_duplicates(inplace=True)
    r_despues = len(data)
    r_eliminados = r_antes - r_despues
    return r_eliminados
print(eliminar(data))