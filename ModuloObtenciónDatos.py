import pandas as pd
path ='C:\\Users\\lucas\\Documents\\Archivos Laborales\\Busquedas y Postulaciones\\Busqueda laboral.ods'
nombreHoja = 'Datos Personales'

datos = pd.read_excel(path, engine='odf', sheet_name=nombreHoja)

for indice_fila, fila in datos.iterrows():
	print(indice_fila)
	print(fila[3])