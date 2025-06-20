from Models.conexionBD import ConexionBD
import tkinter as tk 
from tkinter import messagebox 
from openpyxl import Workbook
from tkinter.filedialog import asksaveasfilename


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

    def generar_informe(self, fecha1, fecha2):
        try:
            conexion = ConexionBD()
            conexion.crearConexion()
            conn = conexion.getConnection()
            cursor = conn.cursor()

            #fecha  nombre_paciente  nombre_medico  estado de la cita
            cursor.execute("""
                            SELECT c.fecha, up.nombre, um.nombre, c.estado
                            FROM citas c
                            JOIN pacientes p ON c.id_paciente = p.id_paciente
                            JOIN medicos m ON c.id_medico = m.id_medico
                            JOIN usuarios up ON p.id_usuario = up.id_usuario
                            JOIN usuarios um ON m.id_usuario = um.id_usuario
                            WHERE c.fecha BETWEEN %s AND %s
                            ORDER BY c.fecha ASC
                        """,(fecha1,fecha2))
            consultas=cursor.fetchall()
            if not consultas:
                messagebox.showerror("Error","No hay citas registradas en ese rango de fechas")
                return
            # Crear archivo Excel
            wb = Workbook()
            ws = wb.active
            ws.title = "Consultas Médicas"
            encabezados = ["Fecha", "Paciente", "Médico", "Estado_cita"]
            ws.append(encabezados)

            # Escribir los datos
            for fila in consultas:
                ws.append(fila)
                
            # Guardar archivo

            ruta = asksaveasfilename(
                                        defaultextension=".xlsx",
                                        filetypes=[("Archivos de Excel", "*.xlsx")],
                                        title="Guardar informe como"
                                    )
            
            if ruta:
                wb.save(ruta)
                messagebox.showinfo("Éxito", f"El informe fue guardado correctamente en:\n{ruta}")
            else:
                messagebox.showinfo("Cancelado", "No se guardó ningún archivo.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el informe de consultas:\n{str(e)}")
        finally:
            cursor.close()
            conexion.cerrarConexion()

                    
 
    


        
    
