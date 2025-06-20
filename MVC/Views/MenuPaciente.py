import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from tkcalendar import Calendar
from PIL import Image, ImageTk
from Controllers.cita import Cita

class MenuPaciente():
    def menuCitas(self, event):
        self.menuCitas = Menu(self.ventana, tearoff=0)
        self.menuCitas.add_command(label="Agendar cita", command=lambda: self.plantillaCita("agendar"))
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

        Label(ventanaPlantilla, text="ID Paciente:").place(x=10, y=10)
        self.id_paciente = Entry(ventanaPlantilla)
        self.id_paciente.place(x=100, y=10)

        Label(ventanaPlantilla, text="ID Medíco:").place(x=10, y=40)
        self.id_medico = Entry(ventanaPlantilla)
        self.id_medico.place(x=100, y=40)

        Label(ventanaPlantilla, text="fecha:").place(x=10, y=70)
        self.fecha_entry = Entry(ventanaPlantilla)
        self.fecha_entry.place(x=100, y=70)

        

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

        Label(ventanaPlantilla, text="Hora:").place(x=10, y=130)
        self.hora_entry = Entry(ventanaPlantilla)
        self.hora_entry.place(x=100, y=130)


        accion = "Agendar" if accion == "agendar" else "Cancelar"
        btn = Button(ventanaPlantilla, text=accion.capitalize(), width=15, command=lambda: self.gestionarCita(accion))
        btn.place(x=120, y=200)

    def gestionarCita(self, accion):
        accion = accion.strip().lower()  
        id_paciente = (self.id_paciente.get())
        id_medico = (self.id_medico.get())
        hora = (self.hora_entry.get())
        fecha = (self.fecha_entry.get())

        if not id_paciente.isdigit():
            messagebox.showerror("Error", "El ID del paciente debe ser un número válido.")
            return

        if not id_medico or not fecha or not hora:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        cita = Cita()

        if accion == "agendar":
            cita.agendarCita(id_paciente, id_medico, fecha, hora)
        else:
            cita.cancelarCita(id_paciente, id_medico, fecha, hora)
    

    def plantillaDiagnosticos(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Historial")
        ventana.geometry("300x300")
        ventana.resizable(0, 0)
        
        Label(ventana, text="ID Paciente:").place(x=10, y=10)
        entrada = Entry(ventana)
        entrada.place(x=100, y=10)

        historial = Listbox(ventana, width=45, height=10)
        historial.place(x=10, y=40)

        def verHistorial():
            id_paciente = entrada.get()
            if not id_paciente.isdigit():
                messagebox.showerror("ID inválido", "Debe ingresar un número.")
                return
            
            historial.delete(0, END)
            datos = Cita().obtenerHistorial(id_paciente)
            if datos:
                for cita in datos:
                    fecha, hora, estado = cita
                    historial.insert(END, f"{fecha} - {hora} - {estado}")

            else:
                historial.insert(END, "No se tienen citas registradas.")


        Button(ventana, text="Cargar", command=verHistorial).place(x=80, y=240)
        Button(ventana, text="Cerrar", command=ventana.destroy).place(x=200, y=240)

   


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600, bg="#9beef0")
        self.ventana.title("Menú Paciente")

        
        imagen = Image.open(r"trabajo-final\MVC\Views\Icons\paciente.png")
        imagen = imagen.resize((700, 500))
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        self.lblImagen = Label(self.ventana, image=self.imagen_tk)
        self.lblImagen.place(x=50, y=50)

        self.iconoSolicitar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-bookmark-25.png")
        self.iconoHistoria = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-clock-25.png")
       
        self.btnCitas = tk.Button(self.ventana, text="Solicitar cita", image=self.iconoSolicitar, compound="left")
        self.btnCitas.place(x=0, y=0, width=400, height=25)
        self.btnCitas.bind("<Button-1>", self.menuCitas)

        self.btnHistorial = tk.Button(self.ventana, text="Historial", image=self.iconoHistoria, compound="left")
        self.btnHistorial.place(x=400, y=0, width=400, height=25)
        self.btnHistorial.bind("<Button-1>", self.menuDiagnosticos)

        

        self.ventana.mainloop()
