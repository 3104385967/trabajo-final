import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound

class MenuAdministrador():
        
    def menuRecepcionista(self, event):
        self.menuRecepcionista = Menu(self.ventana, tearoff=0)
        self.menuRecepcionista.add_command(label="Registrar Recepcionista", command=lambda: self.plantillaRecepcionista("Registrar"))
        self.menuRecepcionista.add_command(label="Modificar Recepcionista", command=lambda: self.plantillaRecepcionista("Modificar"))
        self.menuRecepcionista.add_command(label="Eliminar Recepcionista", command=lambda: self.plantillaRecepcionista("Eliminar"))

        try:
            self.menuRecepcionista.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuRecepcionista.grab_release()

    def menuMedico(self, event):
        self.menuMedico = Menu(self.ventana, tearoff=0)
        self.menuMedico.add_command(label="Registrar Médico", command=lambda: self.plantillaMedico("Registrar"))
        self.menuMedico.add_command(label="Modificar Médico", command=lambda: self.plantillaMedico("Modificar"))
        self.menuMedico.add_command(label="Eliminar Médico", command=lambda: self.plantillaMedico("Eliminar"))

        try:
            self.menuMedico.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuMedico.grab_release()

    def menuInforme(self, event):
        self.menuInforme = Menu(self.ventana, tearoff=0)
        self.menuInforme.add_command(label="Agregar informe", command=lambda: self.plantillaInforme("Agregar"))
        self.menuInforme.add_command(label="Modificar informe", command=lambda: self.plantillaInforme("Modificar"))
        self.menuInforme.add_command(label="Eliminar Informe", command=lambda: self.plantillaInforme("Eliminar"))

        try:
            self.menuInforme.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuInforme.grab_release()

    def plantillaRecepcionista(self, accion):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} Recepcionista")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

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

        if accion == "Registrar":
            btn = Button(ventanaPlantilla, text="Registrar", width=15, command=lambda: self.accionGuardar("registrar"))
        elif accion == "Modificar":
            btn = Button(ventanaPlantilla, text="Modificar", width=15, command=lambda: self.accionGuardar("modificar"))
        elif accion == "Eliminar":
            btn = Button(ventanaPlantilla, text="Eliminar", width=15, command=lambda: self.accionGuardar("eliminar"))

        btn.place(x=90, y=200)

    def plantillaMedico(self, accion):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} Doctor")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="Cédula:").place(x=10, y=10)
        Entry(ventanaPlantilla).place(x=100, y=10)

        Label(ventanaPlantilla, text="Nombre:").place(x=10, y=40)
        Entry(ventanaPlantilla).place(x=100, y=40)

        Label(ventanaPlantilla, text="Especialidad:").place(x=10, y=70)
        Entry(ventanaPlantilla).place(x=100, y=70)

        Label(ventanaPlantilla, text="Correo:").place(x=10, y=100)
        Entry(ventanaPlantilla).place(x=100, y=100)

        Label(ventanaPlantilla, text="Teléfono:").place(x=10, y=130)
        Entry(ventanaPlantilla).place(x=100, y=130)

        if accion == "Registrar":
            btn = Button(ventanaPlantilla, text="Registrar", width=15, command=lambda: self.accionGuardar("registrar"))
        elif accion == "Modificar":
            btn = Button(ventanaPlantilla, text="Modificar", width=15, command=lambda: self.accionGuardar("modificar"))
        elif accion == "Eliminar":
            btn = Button(ventanaPlantilla, text="Eliminar", width=15, command=lambda: self.accionGuardar("eliminar"))

        btn.place(x=90, y=200)

    def plantillaInforme(self, accion):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} Informe")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="Informe").place(relx=0.5, y=10)

        Label(ventanaPlantilla, text="ID:").place(x=10, y=40)
        Entry(ventanaPlantilla).place(x=100, y=40)

        Label(ventanaPlantilla, text="Fecha:").place(x=10, y=70)
        Entry(ventanaPlantilla).place(x=100, y=70)

        Label(ventanaPlantilla, text="Cantidad:").place(x=10, y=100)
        Entry(ventanaPlantilla).place(x=100, y=100)


        if accion == "Agregar":
            btn = Button(ventanaPlantilla, text="Registrar", width=15, command=lambda: self.accionGuardar("Agregar"))
        elif accion == "Modificar":
            btn = Button(ventanaPlantilla, text="Modificar", width=15, command=lambda: self.accionGuardar("modificar"))
        elif accion == "Eliminar":
            btn = Button(ventanaPlantilla, text="Eliminar", width=15, command=lambda: self.accionGuardar("eliminar"))

        btn.place(x=90, y=200)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600)
        self.ventana.title("Menú Administrador")

        self.btnRecepcionista = tk.Button(self.ventana, text="Gestionar Recepcionista")
        self.btnRecepcionista.place(x=0, y=0, width=266, height=25)
        self.btnRecepcionista.bind("<Button-1>", self.menuRecepcionista)

        self.btnMedicos = tk.Button(self.ventana, text="Gestionar Médico")
        self.btnMedicos.place(x=266, y=0, width=266, height=25)
        self.btnMedicos.bind("<Button-1>", self.menuMedico)

        self.btnInformes = tk.Button(self.ventana, text="Gestionar Informes")
        self.btnInformes.place(x=532, y=0, width=266, height=25)
        self.btnInformes.bind("<Button-1>", self.menuInforme)

        

        self.ventana.mainloop()




