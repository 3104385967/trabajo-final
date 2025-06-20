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
from PIL import Image, ImageTk


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
            self.btnIngresar.bind("<Button-1>",self.validar_ingreso )
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
        self.ventana.config(width=440, height=350, bg="#b9eaeb")
        self.ventana.title("Inicio de Sesión")

        self.bandera = False

        
        self.iconoAyuda = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-help-25.png")
        self.iconoIngresar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-login-25.png")
        self.iconoLimpiar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-trash-25.png")
        self.iconoVer = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-eye-25.png")
        self.iconoRegistrar = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-add-user-25.png")
        self.iconoUsuario = tk.PhotoImage(file=r"trabajo-final\MVC\Views\Icons\icons8-user-25.png")


        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:", image=self.iconoUsuario, compound="left")
        self.lblUsuario.place(x=60, y=129, width=80, height=25)

        self.txtUsuario = tk.Entry(self.ventana, show="*")
        self.txtUsuario.place(relx=0.5, y=140, anchor="center",width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarUsuario)

        self.tool_usuario=Tooltip(self.txtUsuario, text="Ingrese su numero de cedula")
        
        self.btnAyuda = tk.Button(self.ventana, text="Ayuda", image=self.iconoAyuda, compound="left")
        self.btnAyuda.place(x=330, y=50)

        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled", image=self.iconoIngresar, compound="left")
        self.btnIngresar.place(x=140, y=200, width=80, height=25)
        Tooltip(self.btnIngresar, text="Presione para ingresar")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=self.iconoLimpiar, compound="left")
        self.btnLimpiar.place(x=230, y=200, width=80, height=25)
        self.btnLimpiar.bind("<Button-1>", self.limpiarCampos)
        Tooltip(self.btnLimpiar, text="Presione para limpiar")

        self.btnVer = tk.Button(self.ventana,image=self.iconoVer, bg="#ed69a3" )
        self.btnVer.place(x=310, y=128, width=30, height=25)
        self.btnVer.bind("<Button-1>", self.verCaracteres)
        Tooltip(self.btnVer, text="Presione para los ver caracteres")

        self.btn_registrar_admi=tk.Button(self.ventana, text="Registrar administrador", image=self.iconoRegistrar, compound="left")
        self.btn_registrar_admi.place(relx=0.5, y=270, anchor="center", width=160, height=25)
        self.btn_registrar_admi.bind("<Button-1>", self.gestionar_admin)
        Tooltip(self.btn_registrar_admi, text="Presione para registrar un administrador")

        self.estado_usuario=None

        self.ventana.mainloop()