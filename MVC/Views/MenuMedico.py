import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from Controllers.Controllers_Medico import ControladorMedico

class MenuMedico():
    def menuCitas(self, event):
        self.menuCitas = Menu(self.ventana, tearoff=0)
        self.menuCitas.add_command(label="Consultar citas", command=self.plantillaCitas)

        try:
            self.menuCitas.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuCitas.grab_release()

    def menuDiagnosticos(self, event):
        self.menuDiagnosticos = Menu(self.ventana, tearoff=0)
        self.menuDiagnosticos.add_command(label="Generar diagnostico", command=self.plantillaDiagnosticos)

        try:
            self.menuDiagnosticos.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuDiagnosticos.grab_release()

    def menuReceta(self, event):
        self.menuReceta = Menu(self.ventana, tearoff=0)
        self.menuReceta.add_command(label="Generar receta", command=self.plantillaReceta)

        try:
            self.menuReceta.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuReceta.grab_release()

    def plantillaDiagnosticos(self):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title("Generar Diagnostico")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="Especialidades")

        Listbox=Listbox(ventanaPlantilla,width=40, height=5)
        Listbox.pack(pady=5)

        especialidades=self.controlador.obtener_especialidades()
        if especialidades:
            for esp in especialidades:
                Listbox.insert(END, esp) #Al final de la lista
        else:
            Listbox.insert(END,"No se encontraron especialidades")


        btn = Button(ventanaPlantilla, text="Generar", width=15)
        btn.place(x=100, y=200)

    def plantillaCitas(self):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title("Lista de citas")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

    
        btn = Button(ventanaPlantilla, text="Cerrar", width=15)
        btn.place(x=100, y=200)
    
    def plantillaReceta(self):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title("Generar receta")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="ID:").place(x=10, y=10)
        Entry(ventanaPlantilla).place(x=100, y=10)

        Label(ventanaPlantilla, text="ID Pac:").place(x=10, y=40)
        Entry(ventanaPlantilla).place(x=100, y=40)

        Label(ventanaPlantilla, text="ID Medico:").place(x=10, y=70)
        Entry(ventanaPlantilla).place(x=100, y=70)

        Label(ventanaPlantilla, text="Fecha:").place(x=10, y=100)
        Entry(ventanaPlantilla).place(x=100, y=100)

        Label(ventanaPlantilla, text="Medicamentos:").place(x=10, y=130)
        Entry(ventanaPlantilla).place(x=100, y=130)

        Label(ventanaPlantilla, text="Dosis:").place(x=10, y=160)
        Entry(ventanaPlantilla).place(x=100, y=160)

        btn = Button(ventanaPlantilla, text="Generar", width=15)
        btn.place(x=100, y=200)

        
    

    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.controlador = ControladorMedico()
        self.controlador.id_usuario = id_usuario
        self.controlador.obtener_id_medico()
        
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600)
        self.ventana.title("Menú Médico")

        self.btnConsultar = tk.Button(self.ventana, text="Consultar citas")
        self.btnConsultar.place(x=0, y=0, width=266, height=25)
        self.btnConsultar.bind("<Button-1>", self.menuCitas)

        self.btnCitas = tk.Button(self.ventana, text="Generar diagnóstico")
        self.btnCitas.place(x=266, y=0, width=266, height=25)
        self.btnCitas.bind("<Button-1>", self.menuDiagnosticos)

        self.btnRecetas = tk.Button(self.ventana, text="Generar receta")
        self.btnRecetas.place(x=532, y=0, width=266, height=25)
        self.btnRecetas.bind("<Button-1>", self.menuReceta)

        

        self.ventana.mainloop()
