# Sitio: https://www.pythondiario.com
# Autor: Diego Caraballo

# Haciendo pruebas con BeautifulSoup y requests

# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import webbrowser

# Capturamos la url ingresada en la variable "url"
url = input("Ingrese la URL: ")

# Abrimos la pagina en una nueva perstaña del navegador
webbrowser.open_new_tab(url) 

# Capturamos el html de la pagina web y creamos un objeto Response
respuesta  = requests.get(url)
contenido = respuesta.text
print ("")

# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(contenido, 'lxml')

# Capturamos el titulo de la página y luego lo mostramos
# Lo que hace BeautifulSoup es capturar lo que esta dentro de la etiqueta title de la url
titulo = soup.title.text
print ("El titulo de la pagina es: " + titulo )
print (" ")

# Buscamos todas etiquetas HTML (a) y luego imprimirmos todo lo que viene despues de "href"
for link in soup.find_all('a'):
    print(link.get('href'))

print (" ")

# Imprimimos todo el HTML de la pagina
print (soup.prettify)