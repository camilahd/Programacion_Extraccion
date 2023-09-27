#Camila Elizabeth Hernandez Alaniz
#27-09-23
#Meta 1.5

"""
#Numero 3
lista = [1, 3, 1, 4, 5, 3, 7]
def contador(lista):
   repet = 0
   for i in lista :
       if lista.count(i) == 1 :
           repet += 1
   sin_repetidos =  len(lista) - repet
   tupla = (repet, sin_repetidos)
   return tupla
print(contador(lista))
"""

"""
#Numero 5
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # queda pendiente
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size= 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://pypi.org/account/login/")
time.sleep(2)

txtEmail= navegador.find_element(By.ID, "username")
txtEmail.send_keys("usuario@gmail.com")
time.sleep(2)

txtPassword= navegador.find_element(By.ID, "password")
txtPassword.send_keys("Hola1")
time.sleep(2)

btnLogin= navegador.find_element(By.CLASS_NAME, "button.button--primary")
btnLogin.click()

navegador.save_screenshot("archivos/img_test_.png")
#navegador.find
#print(navegador.title)

time.sleep(5)
"""


"""
#Numero 6
import pandas as pd
url = "C:/Users/camil/Downloads/titanic (1).csv"
class CSVReader:
    def __init__(self, url):
        self.url = url
        self.datos = pd.read_csv(url)

    #filas
    def primeras(self, n):
        return self.datos.head(n)

    def ultimas(self, n):
        return self.datos.tail(n)

    def aleatorio(self, n):
        return self.datos.sample(n)

    #columnas
    @property
    def nombres(self):
        return list(self.datos.columns)

    @property
    def t_datos(self):
        return list(self.datos.dtypes)

    @property
    def dimension(self):
        return self.datos.shape


url = "https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv"
vista = CSVReader(url)

# Ejemplos
print("Primeras 3 filas:", vista.primeras(3))
print("\nÚltimas 3 filas:", vista.ultimas(3))
print("\n3 filas aleatorias:", vista.aleatorio(3))

print("\nNombres de las columnas:", vista.nombres)
print("\nTipos de datos de las columnas:", vista.t_datos)
print("\nDimensiones:", vista.dimension)
"""

