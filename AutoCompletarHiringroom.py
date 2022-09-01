# Impotamos Tkinter para crear una interfaz grafica basica para los mensajes
from tkinter import messagebox

# Importamos OpenPyXL para leer el archivo de excel


# Importamos los ecursos de Selenium para hacer Web Scraping
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


website = "https://hiringroom.com/jobs/get_vacancy/62fbab954906902587ddbce3/candidates/new?source=linkedinjobs"
path_geckodriver = 'C:\\Users\\lucas\\Documents\\Ejecutables\\geckodriver.exe'
path_datos = 'C:\\Users\\lucas\\Documents\\Archivos Laborales\\Busquedas y Postulaciones\\Datos para hiringroom.txt'

xpath_boton_CompletarFormularioManualmente = '//button[text()="Completar formulario manualmente"]'
xpath_boton_seleccionarFotoPerfil = '//input[@class="sc-bkbkJK sc-hTRkXV UgHUN enlJuL"]'
xpath_boton_siguienteFormulario = '//button[text()="Continuar"]'
xpath_boton_añadirExperiencia = '//h5[text()="+ Añadir experiencia"]'
xpath_boton_añadirEducacion = '//h5[text()="+ Añadir educación"]'
xpath_boton_añadirMensajeAdicional = '//h5[text()="+ Añadir mensaje adicional"]'
xpath_boton_educacionSecundariaCompleta = '//label[text()="Sí"]'
xpath_boton_aceptarCondiciones = '//*[@for="termsConditions.hiring"]'

mensaje1 = "Antes de avanzar a la siguiente parte del formulario, revise lo ya completado"
titulo1 = "Primera parte del formulario completada"

cantidad_estudios = 3
cantidad_experiencia = 1

def apretarBoton(pathBoton):
    boton = driver.find_element(By.XPATH , pathBoton)
    boton.click()
   
driver = webdriver.Firefox(executable_path = path_geckodriver)
driver.get(website)

apretarBoton(xpath_boton_CompletarFormularioManualmente)

with open(path_datos, mode="r", encoding="utf-8") as file:
    for x, line in enumerate(file):

        if ("Comienzo de la segunda parte:" in line):

            #messagebox.showinfo(message = mensaje1, title = titulo1)

            apretarBoton(xpath_boton_siguienteFormulario)
            apretarBoton(xpath_boton_educacionSecundariaCompleta)
            apretarBoton(xpath_boton_aceptarCondiciones)

            for x in range(0, cantidad_experiencia):
                apretarBoton(xpath_boton_añadirExperiencia)

            for x in range(0, cantidad_estudios):
                apretarBoton(xpath_boton_añadirEducacion)

            try:
                apretarBoton(xpath_boton_añadirMensajeAdicional)
            except NoSuchElementException: 
                print("No se encontró el botón para añadir un mensaje adicional")



        caracteristica = line
        separador = ' | '
        dividir = caracteristica.split(separador)
        
        try:
            gotdata = dividir[2]
            tipo_carga = dividir[0]
            id_caracteristica = dividir[1]
            valor_caracteristica = dividir[2]
        except IndexError:
            gotdata = 'Null'
            tipo_carga = 'Null'
            id_caracteristica = 'Null'
            valor_caracteristica = 'Null'

        if ((tipo_carga == "input") or (tipo_carga == "comboBox")):
            tipo_busqueda = By.ID
        elif (tipo_carga == "textarea"):
            tipo_busqueda = By.NAME
        elif ((tipo_carga == "bad_comboBox") or (tipo_carga == "bad_input")):
            tipo_busqueda = By.XPATH
        else:
            tipo_busqueda = By.CLASS_NAME

        try:
            id = id_caracteristica
            element = driver.find_element(tipo_busqueda , id)

            element.send_keys(valor_caracteristica)

            if ((tipo_carga == "comboBox") or (tipo_carga == "bad_comboBox")):
                element.send_keys(Keys.ENTER)

            print(id_caracteristica)
            print(valor_caracteristica)

        except NoSuchElementException:
            if(id_caracteristica != 'Null'):
                print('No se encontro el elemento: ' + id_caracteristica)


# driver.quit()

# C:\Users\lucas\Documents\Archivos Laborales

#'//input[@name="phone"]'