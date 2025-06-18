import tkinter as tk
from tkinter import *

class Registro:
    def plantilla_registro(self, accion, rol):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion}{rol}")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)
        if accion=="Registrar" or accion=="Modificar":

            Label(ventanaPlantilla, text="Cédula:").place(x=10, y=10)
            Entry(ventanaPlantilla).place(x=100, y=10)

            Label(ventanaPlantilla, text="Nombre:").place(x=10, y=40)
            Entry(ventanaPlantilla).place(x=100, y=40)

            Label(ventanaPlantilla, text="Apellido:").place(x=10, y=70)
            Entry(ventanaPlantilla).place(x=100, y=70)

            Label(ventanaPlantilla, text="Correo:").place(x=10, y=100)
            Entry(ventanaPlantilla).place(x=100, y=100)

            Label(ventanaPlantilla, text="Teléfono:").place(x=10, y=130)
            Entry(ventanaPlantilla).place(x=100, y=130)

            if rol=="Medico":
                Label(ventanaPlantilla, text="Especialidades:").place(x=10, y=160)
        
        elif accion=="Eliminar":

            Label(ventanaPlantilla, text="Cédula:").place(x=10, y=100)
            Entry(ventanaPlantilla).place(x=100, y=100)
        
        

        if accion == "Registrar":
            btn = Button(ventanaPlantilla, text="Registrar", width=15)
        elif accion == "Modificar":
            btn = Button(ventanaPlantilla, text="Modificar", width=15)
        elif accion == "Eliminar":
            btn = Button(ventanaPlantilla, text="Eliminar", width=15)

        btn.place(x=90, y=200)

    def __init__(self, ventana, accion, rol):
        self.ventana=ventana
        self.accion=accion
        self.rol=rol
        self.plantilla_registro(accion=self.accion, rol=self.rol)