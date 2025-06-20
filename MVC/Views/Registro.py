import tkinter as tk
from tkinter import *
from tkinter import Listbox, END, messagebox
from Controllers.registro import Registro_funcionalidades
from .Tooltip import Tooltip

class Registro:
    def __init__(self, ventana, accion, rol):
        self.ventana = ventana
        self.accion = accion
        self.rol = rol
        self.lista_esp_elegidas=[]

        self.ventanaPlantilla = Toplevel(self.ventana)
        self.ventanaPlantilla.title(f"{self.accion} {self.rol}")
        self.ventanaPlantilla.geometry("300x250")
        self.ventanaPlantilla.resizable(0, 0)
        self.ventanaPlantilla.transient(self.ventana)
        self.ventanaPlantilla.lift()

        if self.accion == "Registrar" or self.accion == "Modificar":
            Label(self.ventanaPlantilla, text="Cédula*:").place(x=10, y=10)
            self.txtCedula=Entry(self.ventanaPlantilla)
            self.txtCedula.place(x=100, y=10,width=160)
            self.tool_cedula=Tooltip(self.txtCedula, text="Ingrese su numero de Cédula")
            self.txtCedula.bind("<KeyRelease>", self.validar_cedula)

            Label(self.ventanaPlantilla, text="Nombre*:").place(x=10, y=40)
            self.txtNombre=Entry(self.ventanaPlantilla)
            self.txtNombre.place(x=100, y=40,width=160)
            self.tool_nombre=Tooltip(self.txtNombre, text="Ingrese su nombre o sus nombres")
            self.txtNombre.bind("<KeyRelease>", self.validar_nombre)

            Label(self.ventanaPlantilla, text="Apellido*:").place(x=10, y=70)
            self.txtApellido=Entry(self.ventanaPlantilla)
            self.txtApellido.place(x=100, y=70,width=160)
            self.tool_apellido=Tooltip(self.txtApellido, text="Ingrese su apellido o sus apellidos")
            self.txtApellido.bind("<KeyRelease>", self.validar_apellido)

            Label(self.ventanaPlantilla, text="Correo*:").place(x=10, y=100)
            self.txtCorreo=Entry(self.ventanaPlantilla)
            self.txtCorreo.place(x=100, y=100, width=160)
            self.tool_correo=Tooltip(self.txtCorreo, text="Ingrese su correo")
            self.txtCorreo.bind("<KeyRelease>", self.validar_correo)

            Label(self.ventanaPlantilla, text="Teléfono*:").place(x=10, y=130)
            self.txtTelefono=Entry(self.ventanaPlantilla)
            self.txtTelefono.place(x=100, y=130,width=160)
            self.tool_telefono=Tooltip(self.txtTelefono, text="Ingrese su numero de telefono")
            self.txtTelefono.bind("<KeyRelease>", self.validar_telefono)

            if rol == "medico" and self.accion == "Registrar":
                Label(self.ventanaPlantilla, text="Especialidades:").place(x=10, y=160)
                self.btnEspecialidad=Button(self.ventanaPlantilla, text="Agregar especialidad", state="disabled")
                self.btnEspecialidad.place(x=100, y=160)

                self.tool_especialidad=Tooltip(self.btnEspecialidad, text="Para poder agregar especialidades primero debe llenar \ntodos los campos de texto correctamente", background="#e74c3c")
                    

        elif self.accion == "Eliminar":
            Label(self.ventanaPlantilla, text="Cédula:").place(x=10, y=100)
            self.txtCedula=Entry(self.ventanaPlantilla)
            self.txtCedula.place(x=100, y=100)
            self.tool_cedula=Tooltip(self.txtCedula, text=f"Ingrese la cedula del {self.rol} que desea eliminar del sistema")
            self.txtCedula.bind("<KeyRelease>", self.validar_cedula)
            
        
        if self.accion == "Registrar":
            self.btn = Button(self.ventanaPlantilla, text="Registrar", width=15)
        elif self.accion == "Modificar":
            self.btn = Button(self.ventanaPlantilla, text="Modificar", width=15)
        elif self.accion == "Eliminar":
            self.btn = Button(self.ventanaPlantilla, text="Eliminar", width=15)

        self.btn.place(x=90, y=200)
        self.btn.config(state="disabled")
        self.tool_accion=Tooltip(self.btn, text=f"Para poder {self.accion} primero debe llenar \ntodos los campos correctamente ", background="#fa8a76")

    def validar_cedula(self, event):
        cedula=self.txtCedula.get()
        self.tool_cedula.hide_tooltip()

        if cedula.isdigit() or event.keysym == "BackSpace":
            if len(cedula)<=20:
                self.tool_cedula.update_tooltip("Ingrese su numero de cedula",background="#76fa99")
                self.estado_cedula="valido"
            
            elif len(cedula) > 20:
                self.tool_cedula.update_tooltip("el numero de cedula no debe tener más de 20 caracteres.", background="#fa8a76")
                self.estado_cedula="invalido"
        else:
            self.tool_cedula.update_tooltip("El numero de cedula debe tener SOLO números.\nNO se aceptan caracteres especiales ni espacios",background="#fa8a76")
            self.estado_cedula="invalido"

        self.tool_cedula.show_tooltip()

        if self.accion=="Eliminar":
            if self.estado_cedula=="valido":
                self.tool_accion.update_tooltip(text=f"Presione para {self.accion}", background="#76fa99")
                self.btn.config(state="normal")
                self.btn.bind("<Button-1>", self.eliminar_usuario)
            else:
                self.tool_accion.update_tooltip(text=f"Para poder {self.accion} primero debe llenar \ntodos los campos correctamente ", background="#fa8a76")
                self.btn.config(state="disabled")
                self.btn.unbind("<Button-1>")

            

    def validar_nombre(self, event):
        nombre=self.txtNombre.get()
        self.tool_nombre.hide_tooltip()

        if nombre.replace(" ", "").isalpha() or event.keysym == "BackSpace" or event.keysym=="space" :
            if len(nombre)<=20:
                self.tool_nombre.update_tooltip("Ingrese su nombre",background="#76fa99")
                self.estado_nombre="valido"
            
            elif len(nombre) > 20:
                self.tool_nombre.update_tooltip("El nombre NO puede tener mas de 20 caracteres.", background="#fa8a76")
                self.estado_nombre="invalido"

        else:
            self.tool_nombre.update_tooltip("El nombre debe tener SOLO letras.\nNO se aceptan caracteres especiales/numeros",background="#fa8a76")
            self.estado_nombre="invalido"

        self.tool_nombre.show_tooltip()
        
    def validar_apellido(self, event):
        apellido=self.txtApellido.get()
        self.tool_apellido.hide_tooltip()

        if apellido.replace(" ", "").isalpha() or event.keysym == "BackSpace" or event.keysym=="space" :
            
            if len(apellido)<=20:
                self.tool_apellido.update_tooltip("Ingrese su apellido",background="#76fa99")
                self.estado_apellido="valido"
            elif len(apellido) > 20:
                self.tool_apellido.update_tooltip("El apellido NO puede tener mas de 20 caracteres.", background="#fa8a76")
                self.estado_apellido="invalido"
        else: 
            self.tool_apellido.update_tooltip("El apellido debe tener SOLO letras.\nNO se aceptan caracteres especiales/numeros",background="#fa8a76")
            self.estado_apellido="invalido"

        self.tool_apellido.show_tooltip()


    def validar_correo(self,event):
        import re
        correo=self.txtCorreo.get()
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        self.tool_correo.hide_tooltip()
        if re.match(patron, correo):
            if len(correo)<=50:
                self.tool_correo.update_tooltip("Ingrese su correo",background="#76fa99")
                self.estado_correo="valido"
            elif len(correo) > 50:
                self.tool_correo.update_tooltip("El correo NO puede tener mas de 20 caracteres.", background="#fa8a76")
                self.estado_correo="invalido"
        else: 
            self.tool_correo.update_tooltip("Ingrese un correo con caracteres validos",background="#fa8a76")
            self.estado_correo="invalido"
        self.tool_correo.show_tooltip()

    def validar_telefono(self, event):
        telefono=self.txtTelefono.get()
        self.tool_telefono.hide_tooltip()

        if telefono.isdigit() or event.keysym == "BackSpace":
            if len(telefono)<=20:
                self.tool_telefono.update_tooltip("Ingrese su numero de telefono",background="#76fa99")
                self.estado_telefono="valido"
            
            elif len(telefono) > 20:
                self.tool_telefono.update_tooltip("el numero de telefono no debe tener más de 20 caracteres.", background="#fa8a76")
                self.estado_telefono="invalido"
        else:
            self.tool_telefono.update_tooltip("El numero de telefono debe tener SOLO números.\nNO se aceptan caracteres especiales ni espacios",background="#fa8a76")
            self.estado_telefono="invalido"

        self.tool_telefono.show_tooltip()

        if self.estado_cedula=="valido" and self.estado_nombre=="valido" and self.estado_apellido=="valido" and self.estado_correo=="valido" and self.estado_telefono=="valido":
            self.tool_accion.update_tooltip(text=f"Presione para {self.accion}", background="#76fa99")
            self.btn.config(state="normal")
            self.btn.bind("<Button-1>", self.registrar_usuarios)

            if self.rol=="medico" and self.accion=="Registrar":
                self.tool_especialidad.update_tooltip(text="Presione para agregar especialidad", background="#76fa99")
                self.btnEspecialidad.config(state="normal")
                self.btnEspecialidad.bind("<Button-1>", self.crearVentanaEspecialidades)
            
        else:
            self.tool_accion.update_tooltip(text=f"Para poder {self.accion} primero debe llenar \ntodos los campos correctamente ", background="#fa8a76")
            self.btn.config(state="disabled")
            self.btn.unbind("<Button-1>")

            if self.rol=="medico" and self.accion=="Registrar":
                self.tool_especialidad.update_tooltip(text="Para poder agregar especialidades primero debe llenar \ntodos los campos de texto correctamente", background="#e74c3c")
                self.btnEspecialidad.config(state="disabled")
                self.btnEspecialidad.unbind("<Button-1>")

            

    def crearVentanaEspecialidades(self,event):
        self.ventanaespecialidades = Toplevel(self.ventana)
        self.ventanaespecialidades.title("Especialidades")
        self.ventanaespecialidades.geometry("300x350")
        self.ventanaespecialidades.resizable(0, 0)
        self.ventanaespecialidades.transient(self.ventana)
        self.ventanaespecialidades.lift()

        Label(self.ventanaespecialidades, text="Doctor").place(x=10, y=10)
        txt1=Entry(self.ventanaespecialidades)
        txt1.place(x=100, y=10)
        txt1.insert(0,self.txtNombre.get())
        txt1.config(state="disabled")

        Label(self.ventanaespecialidades, text="Cédula").place(x=10, y=40)
        txt2=Entry(self.ventanaespecialidades)
        txt2.place(x=100, y=40)
        txt2.insert(0,self.txtCedula.get())
        txt2.config(state="disabled")

        Label(self.ventanaespecialidades, text="Especialidades:").place(x=10, y=80)
        self.listbox_especialidades = Listbox(self.ventanaespecialidades, width=30, height=8)
        self.listbox_especialidades.place(x=10, y=110)

        # Cargar especialidades desde la BD
        funcionalidad=Registro_funcionalidades(rol=None, accion=None, cedula=None,nombre=None,apellido=None,correo=None,telefono=None, lista=None)
        self.lista_especialidades=funcionalidad.cargar_especialidades()
        for esp in self.lista_especialidades:
                self.listbox_especialidades.insert(END, esp[1])
        
        # Botón para asignar
        btn_asignar=Button(self.ventanaespecialidades,text="Asignar especialidades")
        btn_asignar.place(x=80, y=250)
        btn_asignar.bind("<Button-1>", self.asignar_especialidad)

        btn_confi=Button(self.ventanaespecialidades,text="Confirmar especialidades seleccionadas")
        btn_confi.place(relx=0.5, y=300, anchor="center")
        btn_confi.bind("<Button-1>", self.confirmar_especialidades)

    def confirmar_especialidades(self,event):
        try:
            if len(self.lista_esp_elegidas)>1:
                esp="\n🌸".join(f"{nombre}" for _, nombre in self.lista_esp_elegidas)
                text=f"¿Desea asignar las especialidades\n\n{esp} ?\n\n🌸Si no acepta se borraran todas las especialidades seleccionadas"
            else:
                text=f"¿Desea asignar la especialidad\n\n{self.especialidad}?\n\n🌸Si no acepta se borraran todas las especialidades seleccionadas"
            
            confirmar = messagebox.askyesno(
                "Confirmar asignación",text)
            
            if confirmar:
                messagebox.showinfo("Confirmado", "Las especialidades han sido asignadas exitosamente")
                self.ventanaespecialidades.destroy()

            else:
                messagebox.showinfo("Eliminado", "Las especialidades elegidas se han eliminado\n vuelve a asignar las especialidades que deseas")
        except AttributeError:
            messagebox.showerror("error", "Debe seleccionar minimo una especialidad")   

    def asignar_especialidad(self, event):
        nombre =self.txtNombre.get()
        cedula=self.txtCedula.get()
        seleccion = self.listbox_especialidades.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Debe seleccionar una especialidad.")
            return

        self.especialidad = self.listbox_especialidades.get(seleccion[0])

        confirmar = messagebox.askyesno(
            "Confirmar asignación",f"¿Desea asignar la especialidad \n\n🌸{self.especialidad}\n\nAl médico {nombre} con cédula {cedula}?")

        if confirmar:
            for i in seleccion:
                    nombre= self.listbox_especialidades.get(i)
                    numero= self.lista_especialidades[i][0]
                    tupla=(numero,nombre)

                    if tupla in self.lista_esp_elegidas:
                        messagebox.showerror("error", f"La especialidad {self.especialidad} ya a sido seleccionada")
                    else:
                    
                        self.lista_esp_elegidas.append(tupla)
                        messagebox.showinfo("Asignado", f"Especialidad '{self.especialidad}' asignada correctamente.")      
        else:
            messagebox.showinfo("Cancelado", "No se realizó la asignación.")

    def registrar_usuarios(self, event):
        registro=Registro_funcionalidades(rol=self.rol, accion=self.accion,cedula=self.txtCedula.get(),nombre=self.txtNombre.get(), apellido=self.txtApellido.get(), correo=self.txtCorreo.get(), telefono=self.txtTelefono.get(), lista=self.lista_esp_elegidas)
        
        print(self.rol)
        print(self.accion)
        print(self.lista_esp_elegidas)

        if self.accion=="Registrar":
            primero=registro.registrar()
            if primero=="si":
                self.ventanaPlantilla.destroy()
        elif self.accion=="Modificar":
            primero=registro.modificar()
            if primero=="si":
                self.ventanaPlantilla.destroy()

    def eliminar_usuario(self,event):
        registro=Registro_funcionalidades(rol=self.rol, accion=self.accion,cedula=self.txtCedula.get(),nombre=None, apellido=None, correo=None, telefono=None, lista=None)
        print(self.txtCedula.get())
        if self.accion=="Eliminar":
            primero=registro.eliminar()
            if primero=="si":
                self.ventanaPlantilla.destroy()

        