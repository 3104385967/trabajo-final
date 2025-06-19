import tkinter as tk
from tkinter import *
from tkinter import Listbox, END, messagebox
from Models.conexionBD import ConexionBD

class Registro:
    def __init__(self, ventana, accion, rol):
        self.ventana = ventana
        self.accion = accion
        self.rol = rol
        self.plantilla_registro(accion=self.accion, rol=self.rol)

    def plantilla_registro(self, accion, rol):
        ventanaPlantilla = Toplevel(self.ventana)
        ventanaPlantilla.title(f"{accion} {rol}")
        ventanaPlantilla.geometry("300x300")
        ventanaPlantilla.resizable(0, 0)

        if accion == "Registrar" or accion == "Modificar":
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

            if rol == "medico" and accion == "Registrar":
                Label(ventanaPlantilla, text="Especialidades:").place(x=10, y=160)
                Button(ventanaPlantilla, text="Agregar especialidad", command=self.crearVentanaEspecialidades).place(x=100, y=160)

        elif accion == "Eliminar":
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

        Label(ventanaespecialidades, text="Doctor").place(x=10, y=10)
        entry_nombre = Entry(ventanaespecialidades)
        entry_nombre.place(x=100, y=10)

        Label(ventanaespecialidades, text="Cédula").place(x=10, y=40)
        entry_cedula = Entry(ventanaespecialidades)
        entry_cedula.place(x=100, y=40)

        Label(ventanaespecialidades, text="Especialidades:").place(x=10, y=80)
        listbox = Listbox(ventanaespecialidades, width=30, height=8)
        listbox.place(x=10, y=110)

        # Cargar especialidades desde la BD
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT nombre_especialidad FROM especialidades")
            especialidades = cursor.fetchall()

            for esp in especialidades:
                listbox.insert(END, esp[0])

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la lista de especialidades:\n{str(e)}")
        finally:
            conexion.cerrarConexion()

        # Botón para asignar
        Button(
            ventanaespecialidades,
            text="Asignar especialidad",
            command=lambda: self.confirmar_asignacion(
                listbox,
                entry_nombre.get(),
                entry_cedula.get()
            )
        ).place(x=80, y=300)

    def confirmar_asignacion(self, listbox, nombre, cedula):
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Debe seleccionar una especialidad.")
            return

        especialidad = listbox.get(seleccion[0])

        confirmar = messagebox.askyesno(
            "Confirmar asignación",
            f"¿Desea asignar la especialidad '{especialidad}' al médico {nombre} con cédula {cedula}?"
        )

        if confirmar:
            messagebox.showinfo("Asignado", f"Especialidad '{especialidad}' asignada correctamente.")
            # Aquí puedes hacer un INSERT en especialidades_medicos si quieres
        else:
            messagebox.showinfo("Cancelado", "No se realizó la asignación.")
