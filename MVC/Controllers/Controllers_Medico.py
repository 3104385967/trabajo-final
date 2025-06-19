from Models.conexionBD import ConexionBD
import tkinter as tk
from tkinter import messagebox
from Controllers.usuario import Usuario


class ControladorMedico():

    def __init__(self):
        self.id_usuario=None


    def ConsultarlistaCitas(self):
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

           
            cursor.execute("""
            SELECT c.fecha, c.hora, c.estado, c.id_paciente, u.nombre, u.apellido 
            FROM citas c
            JOIN pacientes p ON c.id_paciente = p.id_paciente
            JOIN usuarios u ON p.id_usuario = u.id_usuario
            WHERE c.id_medico = %s
        """, (self.id_usuario,))
            citas = cursor.fetchall()
            return citas
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron consultar las citas:\n{str(e)}")
            return []
        finally:
          conexion.cerrarConexion()

        
    def guardarReceta(self, id_paciente, id_medico, fecha, medicamento, dosis):
     try:
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO recetas (id_paciente, id_medico, fecha, medicamento, dosis)
            VALUES (?, ?, ?, ?, ?)
        """, (id_paciente, id_medico, fecha, medicamento, dosis))

        conn.commit()

     except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la receta:\n{str(e)}")

     finally:
        conexion.cerrarConexion()
   
    def consultarRecetas(self):
     try:
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT r.fecha, r.medicamento, r.dosis, u.nombre, u.apellido
            FROM recetas r
            JOIN pacientes p ON r.id_paciente = p.id_paciente
            JOIN usuarios u ON p.id_usuario = u.id_usuario
            WHERE r.id_medico = ?
        """, (self.id_usuario,))

        recetas = cursor.fetchall()
        return recetas

     except Exception as e:
        messagebox.showerror("Error", f"No se pudieron consultar las recetas:\n{str(e)}")
        return []

     finally:
        conexion.cerrarConexion()



