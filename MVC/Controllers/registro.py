from Models.conexionBD import ConexionBD
from tkinter import messagebox
from tkinter import END

class Registro_funcionalidades():
    def __init__(self):
        pass

    def cargar_especialidades(self):
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM especialidades")
            especialidades = cursor.fetchall()

            return especialidades
            

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la lista de especialidades:\n{str(e)}")
        finally:
            conexion.cerrarConexion()