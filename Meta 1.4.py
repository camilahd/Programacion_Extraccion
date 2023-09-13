#+Camila Elizabeth Hernandez Alaniz
# 951
# 10/09/23


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # queda pendiente
from webdriver_manager.chrome import ChromeDriverManager
#from bs4 import BeautifulSoup

def busqueda_amazon(producto_buscar, pestañas_cantidad):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size= 1020, 1200")
    amazon = webdriver.Chrome(service=s, options=opc)
    amazon.get("https://www.amazon.com.mx/")
    time.sleep(12)

    busqueda = amazon.find_element(By.NAME, 'field-keywords')
    busqueda.send_keys(producto_buscar)
    boton = amazon.find_element(By.XPATH, '//input[@type="submit"]')
    time.sleep(2)
    boton.click()

    datos = { "Nombre": [], "Rating": [], "Precio": [], "Fecha de entrega": []}
    time.sleep(2)


    for pestaña in range(pestañas_cantidad):
        if pestaña >= 1:
            pestaña_e= amazon.find_element(By.CLASS_NAME, "s-pagination-item.s-pagination-button")
            pestaña_e.click()
        nombres = amazon.find_elements(By.CLASS_NAME, 'a-size-base-plus.a-color-base.a-text-normal')
        ratings = amazon.find_elements(By.CLASS_NAME, 'a-size-base.puis-bold-weight-text')
        precios = amazon.find_elements(By.CLASS_NAME, 'a-price')
        fechas_entrega = amazon.find_elements(By.CLASS_NAME, 'a-color-base.a-text-bold')

        for i in range(len(nombres)):
            # Añade la información del producto actual a los datos
            datos["Nombre"].append(nombres[i].text)

            if len(ratings) > 0:
                datos["Rating"].append(ratings[i].text)
            else:
                datos["Rating"].append("None")
            precio_text = precios[i].text
            precio_numero = precio_text.replace("$", "")

            if len(precio_numero) > 0:
                datos["Precio"].append(precio_numero)
            else:
                datos["Precio"].append("None")
            datos["Fecha de entrega"].append(fechas_entrega[i].text)

    amazon.close()
    datos_df = pd.DataFrame(datos)
    datos_df.to_csv("archivos/datos_shampoo.csv")

    return datos_df

producto_buscar = input("Ingrese el producto que desea buscar:")
pestañas_cantidad = int(input("¿Cuantos pestañas de productos desea buscar?"))
busqueda_amazon(producto_buscar, pestañas_cantidad)