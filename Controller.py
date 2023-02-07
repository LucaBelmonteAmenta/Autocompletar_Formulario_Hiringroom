from Core import Core
from Config import APP_PATH
from Model import *


# Impotamos Tkinter para crear una interfaz grafica basica para los mensajes
from tkinter import messagebox

# Importamos los recursos de Selenium para hacer Web Scraping
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

website_1 = "https://bghtechpartner.hiringroom.com/jobs/get_vacancy/63c94c26a52817326a8e8786?source=linkedinjobs"
website_2 = "https://hiringroom.com/jobs/get_vacancy/63c94c26a52817326a8e8786/candidates/new?source=linkedinjobs"
website_3 = "https://hiringroom.com/jobs/get_vacancy/63c94c26a52817326a8e8786/candidates/new?source=linkedinjobs#step3"

path_geckodriver =  APP_PATH + '\\Controladores de Navegadores\\geckodriver.exe'
path_IEDriverServer =  APP_PATH + '\\Controladores de Navegadores\\IEDriverServer.exe'
path_chromedriver =  APP_PATH + '\\Controladores de Navegadores\\chromedriver.exe'

path_foto_perfil = APP_PATH + '\\Datos de Ususrio\\Foto Perfil.png'
path_curriculum = APP_PATH + '\\Datos de Ususrio\\Curriculum Vitae 2023 (1).pdf'

path_datos = 'C:\\Users\\lucas\\Documents\\Archivos Laborales\\Busquedas y Postulaciones\\Datos para hiringroom.txt'

xpath_boton_CompletarFormularioManualmente = '//button[text()="Completar formulario manualmente"]'
xpath_boton_siguienteFormulario = '//button[text()="Continuar"]'
xpath_boton_añadirExperiencia = '//h5[text()="+ Añadir experiencia"]'
xpath_boton_añadirEducacion = '//h5[text()="+ Añadir educación"]'
xpath_boton_añadirMensajeAdicional = '//h5[text()="+ Añadir mensaje adicional"]'
xpath_boton_educacionSecundariaCompleta = '//label[text()="Sí"]'
xpath_boton_aceptarCondiciones = '//*[@for="termsConditions.hiring"]'

mensaje1 = "Antes de avanzar a la siguiente parte del formulario, revise lo ya completado"
titulo1 = "Primera parte del formulario completada"


class Controller():

    def __init__(self):
        self.View = Core.loadModule("View") 


    def main(self):
        self.View.main(self)


    def cargarControladorNavegador(self, navegador):
        
        driver = None

        match(navegador):
            case "Google Chrome":
                driver = webdriver.Chrome(executable_path = path_chromedriver)
            case "Mozilla Firefox":
                driver = webdriver.Firefox(executable_path = path_geckodriver)
            case "Microsoft Edge":
                driver = webdriver.Edge(executable_path = path_IEDriverServer)

        return driver


    def clickElement(self, text_boton):
        # El "boton" (o cual cualquiera que sea el WebElement) se busca en funcion de su texto
        pathElements = f"//*[text()='{text_boton}']"
        Elements = self.driver.find_element(by = By.XPATH , value=pathElements)
        Elements.click()


    def cargarArchivo(self, id_elemento, path_archivo):
        field = self.driver.find_element(by=By.ID, value=id_elemento)
        self.driver.execute_script("arguments[0].style.display = 'block';", field)
        field.send_keys(path_archivo)
    

    def cargarDatos(self, parameters):

        # parameters --> lista de diccionarios con 2

        for item in parameters:
            try:
                elemento_web = self.driver.find_element(by = By.ID, value = item["id_category"])
                elemento_web.send_keys(item["user_data"])

                if (elemento_web.get_attribute("aria-autocomplete") == "list"):
                    elemento_web.send_keys(Keys.ENTER)
            except:
                print("Error en -->", item["id_category"], " / ", item["user_data"])



    def AutocompletarFormulario(self, link, navegador):

        self.driver = self.cargarControladorNavegador(navegador)

        self.driver.get(link)

        elementos_input = self.driver.find_elements(by=By.TAG_NAME , value='input')
        elementos_textareas = self.driver.find_elements(by=By.TAG_NAME , value='textarea')
        elementos_h5 = self.driver.find_elements(by=By.TAG_NAME , value='h5')

        modulos_datos_usuario = Core.openJson("DatosUsuario")
        estudios = Core.buscar_dicc(modulos_datos_usuario, "Nombre Modulo", "Educations")
        experiencia_laboral = Core.buscar_dicc(modulos_datos_usuario, "Nombre Modulo", "Experiencia laboral")

        self.clickElement('Completar formulario manualmente')

        lista = modulos_datos_usuario[0]["Contenido"][0]

        self.cargarDatos()
      


        self.clickElement("Continuar")

        for estudio in estudios["Contenido"]:
            self.clickElement('+ Añadir educación')

            
            


        




        


# driver.quit()

#'//input[@name="phone"]'