from Models.conexionBD import ConexionBD
import tkinter as tk 
from tkinter import messagebox 

from Views.MenuPaciente import MenuPaciente

class Cita():
    def __init__(self):
        self.id_cita = None
        self.id_paciente = None
        self.id_medico = None
        self.fecha = None
        self.hora = None
        

    def agendarCita(self, nombre, apellido, telefono, fecha, hora):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        
        try:
            cursor.execute("INSERT INTO cita (nombre, apellido, telefono, fecha, hora) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, telefono, fecha, hora))
            con.commit()
            messagebox.showinfo("La cita fue agendada adecuadamente.")
        except Exception as e:
            messagebox.showerror("No fue posible agendar la cita: {e}")
        finally:
            miConexion.cerrarConexion()


    def cancelarCita(self, nombre, apellido, telefono, fecha, hora):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        
          
        try:
            cursor.execute("DELETE FROM cita WHERE nombre = ? AND apellido = ? AND telefono = ? AND fecha = ? AND hora = ?", (nombre, apellido, telefono, fecha, hora))
            con.commit()
            messagebox.showinfo("La cita fue cancelada adecuadamente.")
        except Exception as e:
            messagebox.showerror("No fue posible cancelar la cita: {e}")
        finally:
            miConexion.cerrarConexion()
            
 
    


        
    
