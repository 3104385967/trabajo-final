import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from tkcalendar import Calendar

#from Controllers.cita import Cita

class MenuPaciente():
    def menuCitas(self, event):
        self.menuCitas = Menu(self.ventana, tearoff=0)
        self.menuCitas.add_command(label="Agendar cita", command=lambda: self.plantillaCita("Agendar"))
        self.menuCitas.add_command(label="Cancelar cita", command=lambda: self.plantillaCita("cancelar"))

        try:
            self.menuCitas.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuCitas.grab_release()

    def menuDiagnosticos(self, event):
        self.menuDiagnosticos = Menu(self.ventana, tearoff=0)
        self.menuDiagnosticos.add_command(label="Ver Historial", command=self.plantillaDiagnosticos)

        try:
            self.menuDiagnosticos.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuDiagnosticos.grab_release()
    
    def plantillaCita(self, accion):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} Paciente")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="Nombre:").place(x=10, y=10)
        self.nombre_entry = Entry(ventanaPlantilla)
        self.nombre_entry.place(x=100, y=10)

        Label(ventanaPlantilla, text="Apellido").place(x=10, y=40)
        self.apellido_entry = Entry(ventanaPlantilla)
        self.apellido_entry.place(x=100, y=40)

        Label(ventanaPlantilla, text="Telefono:").place(x=10, y=70)
        self.telefono_entry = Entry(ventanaPlantilla)
        self.telefono_entry.place(x=100, y=70)

        Label(ventanaPlantilla, text="Hora:").place(x=10, y=130)
        self.hora_entry = Entry(ventanaPlantilla)
        self.telefono_entry.place(x=100, y=130)

        Label(ventanaPlantilla, text="Fecha:").place(x=10, y=100)
        self.fecha_entry = Entry(ventanaPlantilla)
        self.fecha_entry.place(x=120, y=100)

        def abrir_calendario():
            top_cal = Toplevel(ventanaPlantilla)
            top_cal.title("Seleccionar Fecha")
            cal = Calendar(top_cal, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(pady=10)

            def seleccionar_fecha():
                self.fecha_entry.delete(0, END)
                self.fecha_entry.insert(0, cal.get_date())
                top_cal.destroy()

            Button(top_cal, text="Seleccionar", command=seleccionar_fecha).pack(pady=5)

        Button(ventanaPlantilla, text="📅", command=abrir_calendario).place(x=280, y=98)



        accion = "Agendar" if accion == "Agendar" else "Cancelar"
        btn = Button(ventanaPlantilla, text=accion, width=15, command=lambda: self.accionGuardar(accion))
        btn.place(x=120, y=200)

    def plantillaDiagnosticos(self):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title("Historial")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

    
        btn = Button(ventanaPlantilla, text="Cerrar", width=15)
        btn.place(x=100, y=200)

    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600)
        self.ventana.title("Menú Paciente")

        self.btnCitas = tk.Button(self.ventana, text="Solicitar cita")
        self.btnCitas.place(x=0, y=0, width=400, height=25)
        self.btnCitas.bind("<Button-1>", self.menuCitas)

        self.btnHistorial = tk.Button(self.ventana, text="Historial")
        self.btnHistorial.place(x=400, y=0, width=400, height=25)
        self.btnHistorial.bind("<Button-1>", self.menuDiagnosticos)

        

        self.ventana.mainloop()
