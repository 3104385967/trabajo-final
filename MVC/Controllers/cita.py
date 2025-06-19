from Models.conexionBD import ConexionBD
import tkinter as tk 
from tkinter import messagebox 


class Cita():
    def __init__(self):
        self.id_cita = None
        self.id_paciente = None
        self.id_medico = None
        self.fecha = None
        self.hora = None
        

    def agendarCita(self, id_paciente, id_medico, fecha, hora):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()

        
        try:
            cursor.execute("INSERT INTO citas (id_paciente, id_medico, fecha, hora, estado) VALUES (?, ?, ?, ?, ?)", 
                        (id_paciente, id_medico, fecha, hora, "pendiente"))
            con.commit()
            messagebox.showinfo("Éxito", "La cita fue agendada adecuadamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible agendar la cita: {e}")
        finally:
            miConexion.cerrarConexion()


    def cancelarCita(self, id_paciente, id_medico, fecha, hora):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()
        
          
        try:
            cursor.execute("UPDATE citas SET estado = 'cancelada' WHERE id_paciente = ? AND id_medico = ? AND fecha = ? AND hora = ?", (id_paciente, id_medico, fecha, hora))
            con.commit()
            messagebox.showinfo("Éxito", "La cita fue cancelada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cancelar la cita: {e}")
        finally:
            miConexion.cerrarConexion()

    def obtenerHistorial(self, id_paciente):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()

        try:
            cursor.execute("SELECT fecha, hora, estado FROM citas WHERE id_paciente = ?", (id_paciente,))
            return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible obtener el historial: {e}")
            return []
        finally:
            miConexion.cerrarConexion()
                    
 
    


        
    
