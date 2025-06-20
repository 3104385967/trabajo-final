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
        ventanaPlantilla.title(f"{accion} Cita")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)
        ventanaPlantilla.transient(self.ventana)
        ventanaPlantilla.lift()


        if accion=="agendar":
            Label(ventanaPlantilla, text="Cedula Paciente:").place(x=10, y=20)
            self.txtCedula = Entry(ventanaPlantilla)
            self.txtCedula.place(x=110, y=20)

            Label(ventanaPlantilla, text="fecha:").place(x=60, y=50)
            self.fecha_entry = Entry(ventanaPlantilla, state="disabled")
            self.fecha_entry.place(x=110, y=50)

            Label(ventanaPlantilla, text="Hora:").place(x=60, y=80)
            self.hora_entry = Entry(ventanaPlantilla)
            self.hora_entry.place(x=110, y=80)

            Label(ventanaPlantilla, text="Medícos:").place(x=10, y=130)
            self.listbox = Listbox(ventanaPlantilla, width=30, height=8)
            self.listbox.place(x=60, y=110)

            cita=Cita()
            self.lista_medicos=cita.cargar_medicos()

            for med in self.lista_medicos:
                    self.listbox.insert(END, med[2])

            def abrir_calendario():
                self.fecha_entry.config(state="normal")
                top_cal = Toplevel(ventanaPlantilla)
                top_cal.title("Seleccionar Fecha")
                cal = Calendar(top_cal, selectmode='day', date_pattern='yyyy-mm-dd')
                cal.pack(pady=10)

                def seleccionar_fecha():
                    self.fecha_entry.delete(0, END)
                    self.fecha_entry.insert(0, cal.get_date())
                    self.fecha_entry.config(state="disabled")
                    top_cal.destroy()

                Button(top_cal, text="Seleccionar", command=seleccionar_fecha).pack(pady=5)

            Button(ventanaPlantilla, text="📅", command=abrir_calendario).place(x=250, y=50)

        elif accion=="cancelar":
            Label(ventanaPlantilla, text="Cedula Paciente:").place(x=10, y=120)
            self.txtCedula = Entry(ventanaPlantilla)
            self.txtCedula.place(x=110, y=120)

        accion = "Agendar" if accion == "agendar" else "Cancelar"
        btn = Button(ventanaPlantilla, text=accion.capitalize(), width=15, command=lambda: self.gestionarCita(accion,ventana=ventanaPlantilla))
        btn.place(relx=0.5, y=280, anchor="center")

    
    def gestionarCita(self, accion):
        accion = accion.strip().lower()  
        cedula_paciente = (self.txtCedula.get())
        if accion =="agendar":
            hora = (self.hora_entry.get())
            fecha = (self.fecha_entry.get())
            try:
                medico=self.listbox.curselection()
                nombre_medico=self.listbox.get(medico[0])
                print(nombre_medico)
            except IndexError:
                messagebox.showwarning("Error","Debe elegir un medico")
            if  not fecha or not hora:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

        if not cedula_paciente.isdigit():
            messagebox.showerror("Error", "la cedula del paciente debe ser un número válido.")
            return
        cita = Cita()

        if accion == "agendar":
            cita.agendarCita(medico=nombre_medico,fecha=fecha, hora=hora, cedula=cedula_paciente)
    
        else:
            cita.cancelarCita(cedula=cedula_paciente)
    

    def plantillaDiagnosticos(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Historial")
        ventana.geometry("300x300")
        ventana.resizable(0, 0)
        ventana.transient(self.ventana)
        ventana.lift()

        Label(ventana, text="cedula Paciente:").place(x=10, y=10)
        entrada = Entry(ventana)
        entrada.place(x=100, y=10)

        historial = Listbox(ventana, width=45, height=10)
        historial.place(x=10, y=40)

        def verHistorial():
            cedula_paciente = entrada.get()
            if not cedula_paciente.isdigit():
                messagebox.showerror("cedula inválida", "Debe ingresar un número.")
                return
            
            historial.delete(0, END)
            datos = Cita().obtenerHistorial(cedula=cedula_paciente)
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
