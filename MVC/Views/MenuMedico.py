import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
from Controllers.Controllers_Medico import  ControladorMedico
from Controllers.usuario import Usuario
from PIL import Image, ImageTk

class MenuMedico():
    def menuCitas(self, event):
        self.menuCitas = Menu(self.ventana, tearoff=0)
        self.menuCitas.add_command(label="Consultar citas", command=self.plantillaCitas)

        try:
            self.menuCitas.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuCitas.grab_release()

    

    def menuReceta(self, event):
        self.menuReceta = Menu(self.ventana, tearoff=0)
        self.menuReceta.add_command(label="Generar receta", command=self.plantillaReceta)

        try:
            self.menuReceta.tk_popup(event.x_root, event.y_root)
        finally:
            self.menuReceta.grab_release()

    

    def plantillaCitas(self):
        ventanaPlantilla = Toplevel(self.ventana, bg="#9beef0")
        ventanaPlantilla.title("Consultar Citas")
        ventanaPlantilla.geometry("550x300")
        ventanaPlantilla.resizable(0, 0)
        listbox = Listbox(ventanaPlantilla, width=80, height=20)
        listbox.pack(pady=20, padx=10)

        self.iconoCerrar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-close-window-25.png")

        controlador = ControladorMedico()
        controlador.id_usuario = self.id_usuario 

        citas = controlador.ConsultarlistaCitas()

        if citas:
         for cita in citas:
         
            fecha, hora, estado, id_paciente, nombre_pac, apellido_pac = cita
            listbox.insert(END, 
                f"Fecha: {fecha} | Hora: {hora} | Estado: {estado} | "
                f"Paciente: {nombre_pac} {apellido_pac} (ID: {id_paciente})")
        else:
           listbox.insert(END, "No hay citas registradas para este médico.")
        
        btn_cerrar = Button(ventanaPlantilla, text="Cerrar", width=115, image=self.iconoCerrar, compound="left", command=ventanaPlantilla.destroy)
        btn_cerrar.place(x=200, y=250)


    
    def plantillaReceta(self):
        ventanaPlantilla = Toplevel(self.ventana, bg="#9beef0")
        ventanaPlantilla.title("Generar receta")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        self.iconoGenerar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-seo-text-25.png")

        Label(ventanaPlantilla, text="ID Paciente:").place(x=10, y=40)
        entry_pac = Entry(ventanaPlantilla)
        entry_pac.place(x=120, y=40)

        Label(ventanaPlantilla, text="ID Medico:").place(x=10, y=70)
        entry_med = Entry(ventanaPlantilla)
        entry_med.place(x=120, y=70)
        entry_med.insert(0, str(self.id_usuario)) #LLenlo automaticamente



        Label(ventanaPlantilla, text="Fecha:").place(x=10, y=100)
        entry_fecha = Entry(ventanaPlantilla)
        entry_fecha.place(x=120, y=100)

        Label(ventanaPlantilla, text="Medicamentos:").place(x=10, y=130)
        entry_medica = Entry(ventanaPlantilla)
        entry_medica.place(x=120, y=130)

        Label(ventanaPlantilla, text="Dosis:").place(x=10, y=160)
        entry_dosis = Entry(ventanaPlantilla)
        entry_dosis.place(x=120, y=160)

        def guardarReceta():
            id_paciente = entry_pac.get()
            id_medico = entry_med.get()
            fecha = entry_fecha.get()
            medicamento = entry_medica.get()
            dosis = entry_dosis.get()

            if not id_paciente or not id_medico or not medicamento or not dosis:
                messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos.")
                return

            controlador = ControladorMedico()
            controlador.guardarReceta(id_paciente, id_medico, fecha, medicamento, dosis)
            messagebox.showinfo("Éxito", "Receta generada correctamente.")
            ventanaPlantilla.destroy()

        btn = Button(ventanaPlantilla, text="Generar", width=115,image=self.iconoGenerar, compound="left", command=guardarReceta)
        btn.place(x=100, y=200)

    def plantillaVerRecetas(self):
        ventanaRecetas = Toplevel(self.ventana, bg="#9beef0")
        ventanaRecetas.title("Recetas generadas")
        ventanaRecetas.geometry("550x300")
        ventanaRecetas.resizable(0, 0)

        listbox = Listbox(ventanaRecetas, width=80, height=12)
        listbox.pack(pady=20, padx=10)

        controlador = ControladorMedico()
        controlador.id_usuario = self.id_usuario

        recetas = controlador.consultarRecetas()

        if recetas:
            for receta in recetas:
                fecha, medicamento, dosis, nombre_pac, apellido_pac = receta
                listbox.insert(END, f"{fecha} | {medicamento} ({dosis}) - Paciente: {nombre_pac} {apellido_pac}")
        else:
          listbox.insert(END, "No hay recetas generadas.")

        Button(ventanaRecetas, text="Cerrar",compound="left", width=15, command=ventanaRecetas.destroy).pack(pady=5)

        
    

    def __init__(self,id_usuario=None):
        self.id_usuario=id_usuario 

        
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=800, height=600, bg="#9beef0")
        self.ventana.title("Menú Médico")

        imagen = Image.open(r"trabajo-final\MVC\Views\Icons\medico.png")
        imagen = imagen.resize((700, 500))
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        self.lblImagen = Label(self.ventana, image=self.imagen_tk)
        self.lblImagen.place(x=50, y=50)

        self.iconoConsultar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-dating-website-25.png")
        self.iconoGenerar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-seo-text-25.png")
        self.iconoVer = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-eye-25.png")

        self.btnConsultar = tk.Button(self.ventana, text="Consultar citas", image=self.iconoConsultar, compound="left")
        self.btnConsultar.place(x=0, y=0, width=266, height=25)
        self.btnConsultar.bind("<Button-1>", self.menuCitas)

        
        self.btnRecetas = tk.Button(self.ventana, text="Generar receta", image=self.iconoGenerar, compound="left")
        self.btnRecetas.place(x=266, y=0, width=266, height=25)
        self.btnRecetas.bind("<Button-1>", self.menuReceta)

        self.btnVerRecetas = tk.Button(self.ventana, text="Ver recetas", image=self.iconoVer, compound="left")
        self.btnVerRecetas.place(x=532, y=0, width=266, height=25)
        self.btnVerRecetas.bind("<Button-1>", lambda e: self.plantillaVerRecetas())


                

        self.ventana.mainloop()
