import os
from importlib import import_module
from Config import APP_PATH
from json import load
from typing import Any, Hashable, Iterable, Optional

class Core:   

    @staticmethod
    def loadModule(nameModule):

        response = None
        nombreControlador = "/" + nameModule + ".py"

        if os.path.exists(APP_PATH + nombreControlador):
            module = import_module(nameModule)
            class_ = getattr(module, nameModule)
            response = class_()

        return response
    
    @staticmethod
    def openJson(nombreJson):
        
        response = None
        
        direcciónArchivo = APP_PATH + "/Datos de Ususrio/" + nombreJson + ".json"

        if os.path.exists(direcciónArchivo):
            archivo = open(direcciónArchivo, mode = "r")
            contenido = load(archivo)
            archivo.close()
            response = contenido

        return response
    
    @staticmethod
    def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
        for dicc in it:
            if dicc[clave] == valor:
                return dicc
        return None
    
    