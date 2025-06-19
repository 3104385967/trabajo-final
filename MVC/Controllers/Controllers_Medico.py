from Models.conexionBD import ConexionBD
import tkinter as tk
from tkinter import messagebox


class ControladorMedico():
    def __init__(self):
        self.id_usuario=None
        self.id_medico=None

    def obtener_id_medico(self):
        conexion=ConexionBD()
        conexion.crearConexion()
        con=conexion.getConnection()
        cursor=con.cursor()


        try:
            cursor.execute("SELECT * FROM medicos")
            listaMedicos=cursor.fetchall() #Resulatdos Consulta

            for medico in listaMedicos:
                if medico[1] == self.id_usuario:
                    self.id_medico=medico[0] #idmedico
                    print(f"ID Medico encontrada:{self.id_medico}")
                    messagebox.showinfo("Bienvenido", "Acceso correcto como Medico")
                    conexion.cerrarConexion()
                    return
                
            messagebox.showwarning("Advertencia","Este usuario no esta registrado como Medico")

        except Exception as e:
            messagebox.showerror("ERROR",f"No se pudo obtener el ID del medico. Comuniquese con el soporte:\n{str(e)}")

        finally:
            conexion.cerrarConexion()

    def obtener_especialidades(self):
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT e.nombre_especialidad
                FROM especialidades_medicos em
                JOIN especialidades e ON em.id_especialidad = e.id_especialidad
                WHERE em.id_medico = ?
            """, (self.id_medico,))

            especialidades = [fila[0] for fila in cursor.fetchall()]
            return especialidades

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar las especialidades:\n{str(e)}")
            return []

        finally:
            conexion.cerrarConexion()
            