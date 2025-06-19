import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import winsound
from .Tooltip import Tooltip
from .Registro import Registro
from Controllers.usuario import Usuario
from .MenuMedico import MenuMedico
from .MenuAdmi import MenuAdministrador
from .MenuRecepcionista import MenuRecepcionista
from .MenuPaciente import MenuPaciente


class Loggin():
    def validar_ingreso(self,event):
        usuario=Usuario(cedula=self.txtUsuario.get())
        rol=usuario.iniciar_sesion()
        if rol:
            self.ventana.destroy()
            if rol=="medico":
                MenuMedico()
            elif rol=="administrador":
                MenuAdministrador()
            elif rol=="paciente":
                MenuPaciente()
            elif rol=="recepcionista":
                MenuRecepcionista()
    
    def gestionar_admin(self, event):
        rol="administrador"
        accion="Registrar"
        self.registro=Registro(ventana=self.ventana, accion=accion, rol=rol)



    def limpiarCampos(self, event):
        self.txtUsuario.delete(0, END)


    def validarUsuario(self, event):
        usuario= self.txtUsuario.get()
        self.tool_usuario.hide_tooltip()
   
        if usuario.isdigit() or event.keysym == "BackSpace":
            if len(self.txtUsuario.get())<=20:

                self.tool_usuario.update_tooltip("Ingrese su numero de cedula",background="#76fa99")
                self.estado_usuario="valido"
            
            elif len(self.txtUsuario.get()) > 20:
                self.tool_usuario.update_tooltip("El usuario no debe tener más de 20 caracteres.", background="#fa8a76")
                self.estado_usuario="invalido"
        else:
            self.tool_usuario.update_tooltip("El usuario debe tener SOLO números.\nNO se aceptan caracteres especiales ni espacios",background="#fa8a76")
            self.estado_usuario="invalido"

        self.tool_usuario.show_tooltip()

        if self.estado_usuario=="valido":
            self.btnIngresar.config(state="normal")
        elif self.estado_usuario=="invalido":
            self.btnIngresar.config(state="disabled")


    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtUsuario.config(show='*')
            self.btnVer.config(bg="#e74c3c")
            self.bandera = False
        else:
            self.txtUsuario.config(show='')
            self.btnVer.config(bg="#83e73c")
            self.bandera = True

    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Inicio de Sesión")

        self.bandera = False
      
        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(x=70, y=125, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana, show="*")
        self.txtUsuario.place(relx=0.5, y=140, anchor="center",width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarUsuario)

        self.tool_usuario=Tooltip(self.txtUsuario, text="Ingrese su numero de cedula")
        
        self.btnAyuda = tk.Button(self.ventana, text="Ayuda")
        self.btnAyuda.place(x=320, y=50)

        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled")
        self.btnIngresar.place(x=140, y=200, width=70, height=25)
        self.btnIngresar.bind("<Button-1>",self.validar_ingreso )

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
        self.btnLimpiar.place(x=230, y=200, width=70, height=25)
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)

        self.btnVer = tk.Button(self.ventana, text="Ver", bg="#e74c3c")
        self.btnVer.place(x=310, y=128, width=30, height=25)
        self.btnVer.bind("<Button-1>", self.verCaracteres)

        self.btn_registrar_admi=tk.Button(self.ventana, text="Registrar administrador")
        self.btn_registrar_admi.place(relx=0.5, y=270, anchor="center", width=150, height=25)
        self.btn_registrar_admi.bind("<Button-1>", self.gestionar_admin)

        self.estado_usuario=None

        self.ventana.mainloop()