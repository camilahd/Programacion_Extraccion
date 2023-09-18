#+Camila Elizabeth Hernandez Alaniz
# 951


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # queda pendiente
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def busqueda_amazon(producto_buscar, pestañas):
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

    for h in range(pestañas):
        nombres = amazon.find_elements(By.CLASS_NAME, 'a-size-base-plus.a-color-base.a-text-normal')
        ratings = amazon.find_elements(By.CLASS_NAME, 'a-size-base.puis-bold-weight-text') #cambia constantemente y en este momento no tiene como tal el numero de las estrellas amazon
        precios = amazon.find_elements(By.CLASS_NAME, 'a-price')
        fechas_entrega = amazon.find_elements(By.CLASS_NAME, 'a-color-base.a-text-bold')

        for i in range(len(nombres)):
            datos["Nombre"].append(nombres[i].text)
            if len(ratings) > i:
                datos["Rating"].append(ratings[i].text)
            else:
                datos["Rating"].append("None")
            precio_text = precios[i].text
            precio_numero = precio_text.replace("$", "")
            if len(precio_numero) > 0:
                datos["Precio"].append(precio_numero)
            else:
                datos["Precio"].append("None")
            if len(fechas_entrega) > 0:
                datos["Fecha de entrega"].append(fechas_entrega[i].text)
            else:
                datos["Fecha de entrega"].append("None")
        try:
            boton_next = amazon.find_element(By.CLASS_NAME, 's-pagination-item.s-pagination-button')
            boton_next.click()
            time.sleep(3)
        #except NoSuchElementException:
            #print("El botón 'Siguiente' no se encontró en la página.")
            #break
        except:
            break

    amazon.close()
    datos_df = pd.DataFrame(datos)
    datos_df.to_csv("archivos/datos_shampoo.csv")

    return datos_df

producto_buscar = input("Ingrese el producto que desea buscar:")
pestañas = int(input("¿Cuantos pestañas de productos desea buscar?"))
busqueda_amazon(producto_buscar, pestañas)