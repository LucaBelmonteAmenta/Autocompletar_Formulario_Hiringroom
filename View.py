import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class View(tk.Tk):

    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    
    PAD = 10
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------


    def __init__(self):
        
        super().__init__()
        self.title("Auto-completar Formulario de Hiringroom")
        self.geometry("600x600")
        self.resizable(width=False, height=False)

        self.cargarRecursos()

        
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    
    def paste_select(self):
        global data
        texto_pegado = self.clipboard_get()
        self.entryLink.insert(0, texto_pegado)
        


    def cargarRecursos(self):

        # Cargar el Entry en le que se escribirá el link de hiringroom
        self.entryLink = ttk.Entry(self, font= ('Helvetica 10 bold'))
        self.entryLink.place(x=160, y=20, width=330) 

        # Cargar el boton para pegar el link de hiringroom en el Entry
        self.buttonPegar = ttk.Button(self, text='Pegar', command=self.paste_select)
        self.buttonPegar.place(x=500, y=18) 

        # Cargar el boton para iniciar el proceso de autocompletar el formulario
        self.buttonPegar = ttk.Button(self, text='Aceptar', command=self.iniciar_Autucompletado)
        self.buttonPegar.place(x=400, y=48) 

        # Cargar el Combobox que alberga los posibles navegadores a emplear
        navegadores = ["Google Chrome", "Mozilla Firefox", "Microsoft Edge"]
        self.comboNavegadores = ttk.Combobox(self, state="readonly", values=navegadores)
        self.comboNavegadores.place(x=120, y=50) 

        # Cargar los Labels descriptivos de los demas elementos
        self.labelLink = ttk.Label(self, text= "Link del formulario: ", font= ('Helvetica 10 bold'))
        self.labelLink.place(x=20, y=20) 
        self.labelNavegador = ttk.Label(self, text= "Navegadores: ", font= ('Helvetica 10 bold'))
        self.labelNavegador.place(x=20, y=50) 

    
    def iniciar_Autucompletado(self):
        link = self.entryLink.get()
        navegador = self.comboNavegadores.get()
        self.Controller.AutocompletarFormulario(link, navegador)




    def main(self, controller):
        self.Controller = controller
        self.mainloop()

    def close(self):
        return