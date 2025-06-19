import tkinter as tk
from tkinter import *
from tkinter import Listbox, END,messagebox
from Models.conexionBD import ConexionBD
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

            if rol=="Medico" and accion=="Registrar":
                Label(ventanaPlantilla, text="Especialidades:").place(x=10, y=160)
                self.btn_espe = Button(ventanaPlantilla,text="agregar especialidad",command=lambda:self.crearVentanaEspecialidades()).place(x=100,y=160)
    
        
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
    def crearVentanaEspecialidades(self):
        ventanaespecialidades = Toplevel(self.ventana)
        ventanaespecialidades.title("Especialidades")
        ventanaespecialidades.geometry("300x350")
        ventanaespecialidades.resizable(0, 0)

    # CAMPOS DE ENTRADA
        Label(ventanaespecialidades, text="Doctor").place(x=10, y=10)
        entry_nombre = Entry(ventanaespecialidades)
        entry_nombre.place(x=100, y=10)

        Label(ventanaespecialidades, text="Cédula").place(x=10, y=40)
        entry_cedula = Entry(ventanaespecialidades)
        entry_cedula.place(x=100, y=40)

    # LISTBOX DE ESPECIALIDADES
        Label(ventanaespecialidades, text="Especialidades:").place(x=10, y=80)
        listbox = Listbox(ventanaespecialidades, width=30, height=8)
        listbox.place(x=10, y=110)

    # CARGA LAS ESPECIALIDADES DESDE LA BD
    try:
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        cursor.execute("SELECT nombre_especialidad FROM especialidades")
        especialidades = cursor.fetchall()

        for esp in especialidades:
          
          Listbox.insert(END, esp[0])  # esp[0] = nombre de la especialidad

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la lista de especialidades:\n{str(e)}")

    finally:
        conexion.cerrarConexion()

    # BOTÓN DE ASIGNAR
 
            
            

           
    def __init__(self, ventana, accion, rol):
        self.ventana=ventana
        self.accion=accion
        self.rol=rol
        self.plantilla_registro(accion=self.accion, rol=self.rol)