import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from tkcalendar import Calendar

from .Registro import Registro


class MenuRecepcionista():
    def menuPaciente(self, event):
        self.menuPaciente = Menu(self.ventana, tearoff=0)
        self.menuPaciente.add_command(label="Registrar Paciente", command=lambda: self.plantillaPaciente("Registrar"))
        self.menuPaciente.add_command(label="Modificar Paciente", command=lambda: self.plantillaPaciente("Modificar"))
        self.menuPaciente.add_command(label="Eliminar Paciente", command=lambda: self.plantillaPaciente("Eliminar"))

        try:
            self.menuPaciente.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuPaciente.grab_release()

    def menuCitas(self, event):
        self.menuCitas = Menu(self.ventana, tearoff=0)
        self.menuCitas.add_command(label="Agendar cita", command=lambda: self.plantillaCita("Agendar"))
        self.menuCitas.add_command(label="Cancelar cita", command=lambda: self.plantillaCita("cancelar"))

        try:
            self.menuCitas.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuCitas.grab_release()

    def plantillaPaciente(self, accion):
        rol="Paciente"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)

    
    def plantillaCita(self, accion):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} Paciente")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        Label(ventanaPlantilla, text="ID:").place(x=10, y=10)
        Entry(ventanaPlantilla).place(x=100, y=10)

        Label(ventanaPlantilla, text="ID Pac").place(x=10, y=40)
        Entry(ventanaPlantilla).place(x=100, y=40)

        Label(ventanaPlantilla, text="ID Medico:").place(x=10, y=70)
        Entry(ventanaPlantilla).place(x=100, y=70)

        Label(ventanaPlantilla, text="Hora:").place(x=10, y=130)
        Entry(ventanaPlantilla).place(x=100, y=130)

        Label(ventanaPlantilla, text="Fecha:").place(x=10, y=100)
        fecha_entry = Entry(ventanaPlantilla, state="disabled")
        fecha_entry.place(x=120, y=100)

        def abrir_calendario():
            fecha_entry.config(state="normal")
            top_cal = Toplevel(ventanaPlantilla)
            top_cal.title("Seleccionar Fecha")
            cal = Calendar(top_cal, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(pady=10)

            def seleccionar_fecha():
                fecha_entry.delete(0, END)
                fecha_entry.insert(0, cal.get_date())
                fecha_entry.config(state="disabled")
                top_cal.destroy()

            Button(top_cal, text="Seleccionar", command=seleccionar_fecha).pack(pady=5)

        Button(ventanaPlantilla, text="📅", command=abrir_calendario).place(x=280, y=98)



        accion = "Agendar" if accion == "Agendar" else "Cancelar"
        btn = Button(ventanaPlantilla, text=accion, width=15, command=lambda: self.accionGuardar(accion))
        btn.place(x=120, y=200)



    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600)
        self.ventana.title("Menú Recepcionista")

        self.btnPaciente = tk.Button(self.ventana, text="Gestionar paciente")
        self.btnPaciente.place(x=0, y=0, width=266, height=25)
        self.btnPaciente.bind("<Button-1>", self.menuPaciente)

        self.btnCitas = tk.Button(self.ventana, text="Agendar citas")
        self.btnCitas.place(x=266, y=0, width=266, height=25)
        self.btnCitas.bind("<Button-1>", self.menuCitas)

        

        self.ventana.mainloop()