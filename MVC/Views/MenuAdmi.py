import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from tkcalendar import Calendar
import tkinter as tk
from PIL import Image, ImageTk

from .Registro import Registro
from Controllers.cita import Cita


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
        rol="recepcionista"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)    


    def gestionar_medicos(self, accion):
        rol="medico"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)

    
    def plantillaInforme(self, accion):#Los informes se generan con las consultas registradas en la base de datos, por eso hay fechas para crear un excel con las citas que se han hecho en ese rango de fechas
        ventanaPlantilla = Toplevel(self.ventana, bg="#b9eaeb")
        ventanaPlantilla.title(f"Generar Informe")
        ventanaPlantilla.geometry("300x140")
        ventanaPlantilla.resizable(0, 0)
        ventanaPlantilla.transient(self.ventana)
        ventanaPlantilla.lift()

        self.iconoGenerar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-seo-text-25.png")

        Label(ventanaPlantilla, text="Informe").place(relx=0.5, y=20, anchor="center")

        Label(ventanaPlantilla, text="De que fecha:").place(x=8, y=40)#año,mes,dia
        self.fecha_1=Entry(ventanaPlantilla, state="disabled")
        self.fecha_1.place(x=100, y=40)

        Label(ventanaPlantilla, text="Hasta que fecha:").place(x=8, y=70)
        self.fecha_2=Entry(ventanaPlantilla, state="disabled")
        self.fecha_2.place(x=100, y=70)
  
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

        Button(ventanaPlantilla, text="📅", command=lambda: abrir_calendario(fecha=self.fecha_1)).place(x=230, y=35)
        Button(ventanaPlantilla, text="📅", command=lambda: abrir_calendario(fecha=self.fecha_2)).place(x=230, y=65)

        if accion == "Generar":
            btn = Button(ventanaPlantilla, text="Generar", width=120, image=self.iconoGenerar, compound="left")
        
        btn.place(x=90, y=100)
        btn.bind("<Button-1>", self.generar_informe)

    def generar_informe(self,event):
        informe=Cita()
        informe.generar_informe(fecha1=self.fecha_1.get(), fecha2=self.fecha_2.get())
        
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600, bg = "#9beef0")
        self.ventana.title("Menú Administrador")

        imagen = Image.open(r"trabajo-final\MVC\Views\Icons\adminis.png")
        imagen = imagen.resize((700, 500))
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        self.lblImagen = Label(self.ventana, image=self.imagen_tk)
        self.lblImagen.place(x=50, y=50)

        self.iconoRecep = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-receptionist-25.png")
        self.iconoMed = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-care-25.png")
        self.iconoInfo = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-new-copy-25.png")


        self.btnRecepcionista = tk.Button(self.ventana, text="Gestionar Recepcionista", image=self.iconoRecep, compound="left")
        self.btnRecepcionista.place(x=0, y=0, width=266, height=25)
        self.btnRecepcionista.bind("<Button-1>", self.menuRecepcionista)

        self.btnMedicos = tk.Button(self.ventana, text="Gestionar Médico", image=self.iconoMed, compound="left")
        self.btnMedicos.place(x=266, y=0, width=266, height=25)
        self.btnMedicos.bind("<Button-1>", self.menuMedico)

        self.btnInformes = tk.Button(self.ventana, text="Generar Informes", image=self.iconoInfo, compound="left")
        self.btnInformes.place(x=532, y=0, width=266, height=25)
        self.btnInformes.bind("<Button-1>", self.menuInforme)

    
        self.ventana.mainloop()




