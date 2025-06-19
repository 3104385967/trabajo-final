import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from tkcalendar import Calendar 

from .Registro import Registro

class MenuAdministrador():
        
    def menuRecepcionista(self, event):
        self.menuRecepcionista = Menu(self.ventana, tearoff=0)
        self.menuRecepcionista.add_command(label="Registrar Recepcionista", command=lambda: self.gestionar_recepcionistas("Registrar"))
        self.menuRecepcionista.add_command(label="Modificar Recepcionista", command=lambda: self.gestionar_recepcionistas("Modificar"))
        self.menuRecepcionista.add_command(label="Eliminar Recepcionista", command=lambda: self.gestionar_recepcionistas("Eliminar"))

        try:
            self.menuRecepcionista.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuRecepcionista.grab_release()

    def menuMedico(self, event):
        self.menuMedico = Menu(self.ventana, tearoff=0)
        self.menuMedico.add_command(label="Registrar Médico", command=lambda: self.gestionar_medicos("Registrar"))
        self.menuMedico.add_command(label="Modificar Médico", command=lambda: self.gestionar_medicos("Modificar"))
        self.menuMedico.add_command(label="Eliminar Médico", command=lambda: self.gestionar_medicos("Eliminar"))

        try:
            self.menuMedico.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuMedico.grab_release()

    def menuInforme(self, event):
        self.menuInforme = Menu(self.ventana, tearoff=0)
        self.menuInforme.add_command(label="Generar informe", command=lambda: self.plantillaInforme("Generar"))

        try:
            self.menuInforme.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuInforme.grab_release()

    def gestionar_recepcionistas(self, accion):
        rol="Recepcionista"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)    


    def gestionar_medicos(self, accion):
        rol="Medico"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)

    
    def plantillaInforme(self, accion):#Los informes se generan con las consultas registradas en la base de datos, por eso hay fechas para crear un excel con las citas que se han hecho en ese rango de fechas
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"Generar Informe")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="Informe").place(relx=0.5, y=10)

        Label(ventanaPlantilla, text="De que fecha:").place(x=8, y=40)#año,mes,dia
        fecha_1=Entry(ventanaPlantilla, state="disabled")
        fecha_1.place(x=100, y=40)

        Label(ventanaPlantilla, text="Hasta que fecha:").place(x=8, y=70)
        fecha_2=Entry(ventanaPlantilla, state="disabled")
        fecha_2.place(x=100, y=70)
  
        def abrir_calendario(fecha):
            fecha.config(state="normal")
            top_cal = Toplevel(ventanaPlantilla)
            top_cal.title("Seleccionar Fecha")
            cal = Calendar(top_cal, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(pady=10)

            def seleccionar_fecha():
                fecha.delete(0, END)
                fecha.insert(0, cal.get_date())
                fecha.config(state="disabled")
                top_cal.destroy()

            Button(top_cal, text="Seleccionar", command=seleccionar_fecha).pack(pady=5)

        Button(ventanaPlantilla, text="📅", command=lambda: abrir_calendario(fecha=fecha_1)).place(x=230, y=35)
        Button(ventanaPlantilla, text="📅", command=lambda: abrir_calendario(fecha=fecha_2)).place(x=230, y=65)

        if accion == "Generar":
            btn = Button(ventanaPlantilla, text="Generar", width=15)
        
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

        self.btnInformes = tk.Button(self.ventana, text="Generar Informes")
        self.btnInformes.place(x=532, y=0, width=266, height=25)
        self.btnInformes.bind("<Button-1>", self.menuInforme)

    
        self.ventana.mainloop()




