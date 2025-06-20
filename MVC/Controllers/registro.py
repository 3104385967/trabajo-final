from Models.conexionBD import ConexionBD
from tkinter import messagebox
from tkinter import END

class Registro_funcionalidades():
    def __init__(self, rol, accion, cedula, nombre, apellido, correo, telefono, lista):
        self.rol=rol
        self.accion=accion
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.telefono=telefono
        self.lista=lista

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

    def registrar(self):
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        try:
            cursor.execute("select * from usuarios where cedula=%s",(self.cedula,))
            usuario_existente=cursor.fetchone()

            if usuario_existente:
                messagebox.showerror("Error","El numero de cedula ingresado ya existe")
                return
            
            consulta="insert into usuarios (cedula, nombre, apellido, telefono, email, rol) values (%s, %s, %s, %s, %s, %s)"
            valores=(self.cedula, self.nombre, self.apellido, self.telefono, self.correo, self.rol)
            cursor.execute(consulta,valores)#inserta los datos
            id_generado=cursor.lastrowid#guarda el id que se genera al insertar
            conn.commit()#lo hace real
            
            if self.rol=="medico":
                cursor.execute("insert into medicos (id_usuario) values (%s)", (id_generado,))
                id_medico=cursor.lastrowid
                conn.commit()
                
                if self.lista:
                    for esp in self.lista:
                        valores=(id_medico, int(esp[0]))
                        cursor.execute("insert into especialidades_medicos (id_medico, id_especialidad) values(%s, %s)", valores)
                    conn.commit()
                        
            elif self.rol=="paciente":
                cursor.execute("insert into pacientes (id_usuario, historial_medico) values (%s, %s)", (id_generado, None))
                conn.commit()
                
            messagebox.showinfo("Registro exitoso", f"El usuario: \n|{self.nombre}| |{self.apellido}|\nFue registrado correctamente ✅")
            return "si"
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar los datos:\n{str(e)}")
        finally:
            cursor.close()#termina las consultas
            conexion.cerrarConexion()

    def modificar(self):
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        try:
            cursor.execute("select id_usuario from usuarios where cedula=%s",(self.cedula,))
            usuario_existente=cursor.fetchone()

            if usuario_existente is None:
                messagebox.showerror("Error","El numero de cedula ingresado NO existe")
                return
            id_usuario = usuario_existente[0]
            consulta="update usuarios set nombre=%s, apellido=%s, telefono=%s, email=%s where id_usuario=%s"
            valores=(self.nombre, self.apellido, self.telefono, self.correo, id_usuario)
            cursor.execute(consulta,valores)
            conn.commit()
      
            messagebox.showinfo("Modificacion exitosa", f"El usuario con cedula: \n|{self.cedula}|\nFue modificado correctamente ✅")
            return "si"
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar los datos:\n{str(e)}")
        finally:
            cursor.close()#termina las consultas
            conexion.cerrarConexion()

    def eliminar(self):
        conexion = ConexionBD()
        conexion.crearConexion()
        conn = conexion.getConnection()
        cursor = conn.cursor()

        try:
            cursor.execute("select id_usuario from usuarios where cedula=%s",(self.cedula,))
            usuario_existente=cursor.fetchone()

            if usuario_existente is None:
                messagebox.showerror("Error","El numero de cedula ingresado NO existe")
                return
            
            consulta="delete from usuarios where id_usuario=%s"
            
            cursor.execute(consulta,usuario_existente,)
            conn.commit()
      
            messagebox.showinfo("Eliminacion exitosa", f"El usuario con cedula: \n|{self.cedula}|\nFue eliminado correctamente ✅")
            return "si"
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar los datos:\n{str(e)}")
        finally:
            cursor.close()#termina las consultas
            conexion.cerrarConexion()
