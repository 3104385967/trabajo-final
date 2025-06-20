from Models.conexionBD import ConexionBD
import tkinter as tk 
from tkinter import messagebox 


class Cita():
    def __init__(self):
        self.id_cita = None
        self.id_medico = None
        self.fecha = None
        self.hora = None
        

    def agendarCita(self, medico, fecha, hora, cedula):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()
        
        try:
            # Obtener id_usuario del médico
            cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre=%s AND rol=%s", (medico, "medico"))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", f"No se encontró el médico '{medico}'.")
                return
            id_usuario_medico = result[0]

            # Obtener id_medico
            cursor.execute("SELECT id_medico FROM medicos WHERE id_usuario=%s", (id_usuario_medico,))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "El médico no está registrado en la tabla 'medicos'.")
                return
            id_medico = result[0]

            # Obtener id_usuario del paciente
            cursor.execute("SELECT id_usuario FROM usuarios WHERE cedula=%s AND rol=%s", (cedula, "paciente"))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "La cédula ingresada no corresponde a un paciente registrado.")
                return
            id_usuario_paciente = result[0]

            # Obtener id_paciente
            cursor.execute("SELECT id_paciente FROM pacientes WHERE id_usuario=%s", (id_usuario_paciente,))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "El usuario no está registrado como paciente.")
                return
            id_paciente = result[0]

            # Insertar la cita
            cursor.execute(
                "INSERT INTO citas (id_paciente, id_medico, fecha, hora, estado) VALUES (%s, %s, %s, %s, %s)", 
                (id_paciente, id_medico, fecha, hora, "pendiente")
            )
            con.commit()
            messagebox.showinfo("Éxito", "La cita fue agendada adecuadamente.")
            
            
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible agendar la cita: {e}")
        finally:
            cursor.close()
            miConexion.cerrarConexion()


    def cancelarCita(self, cedula):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()
          
        try:

            # Obtener id_usuario del paciente
            cursor.execute("SELECT id_usuario FROM usuarios WHERE cedula=%s AND rol=%s", (cedula, "paciente"))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "La cédula ingresada no corresponde a un paciente registrado.")
                return
            id_usuario_paciente = result[0]

            # Obtener id_paciente
            cursor.execute("SELECT id_paciente FROM pacientes WHERE id_usuario=%s", (id_usuario_paciente,))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "El usuario no está registrado como paciente.")
                return
            id_paciente = result[0]
                
            cursor.execute("UPDATE citas SET estado = 'cancelada' WHERE id_paciente = %s ", (id_paciente,))
            con.commit()
            messagebox.showinfo("Éxito", "La cita fue cancelada correctamente.")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cancelar la cita: {e}")
        finally:
            miConexion.cerrarConexion()

    def obtenerHistorial(self,cedula):
        miConexion = ConexionBD()
        miConexion.crearConexion()
        con = miConexion.getConnection()
        cursor = con.cursor()

        try:
             # Obtener id_usuario del paciente
            cursor.execute("SELECT id_usuario FROM usuarios WHERE cedula=%s AND rol=%s", (cedula, "paciente"))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "La cédula ingresada no corresponde a un paciente registrado.")
                return
            id_usuario_paciente = result[0]

            # Obtener id_paciente
            cursor.execute("SELECT id_paciente FROM pacientes WHERE id_usuario=%s", (id_usuario_paciente,))
            result = cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "El usuario no está registrado como paciente.")
                return
            id_paciente = result[0]
            
            cursor.execute("SELECT fecha, hora, estado FROM citas WHERE id_paciente = %s", (id_paciente,))
            return cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible obtener el historial: {e}")
            return []
        finally:
            miConexion.cerrarConexion()

    def cargar_medicos(self):
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM usuarios where rol=%s",("medico",))
            medicos = cursor.fetchall()

            return medicos
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la lista de medicos:\n{str(e)}")
        finally:
            conexion.cerrarConexion()
                    
 
    


        
    
