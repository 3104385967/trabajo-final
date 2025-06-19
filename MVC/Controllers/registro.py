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
            cursor.execute("select * from usuarios")
            listausuarios = cursor.fetchall()

            for usuario in listausuarios:
                if usuario[1]==self.cedula:
                    messagebox.showerror("Error","El numero de cedula ingresado ya existe")
                    return
            cursor.close()

            consulta="insert into usuarios (cedula, nombre, apellido, telefono, email, rol) values (%s, %s, %s, %s, %s, %s)"
            valores=(self.cedula, self.nombre, self.apellido, self.telefono, self.correo, self.rol)
            cursor.execute(consulta,valores)#los inserta
            conn.commit()#lo hace real
            id_generado=cursor.lastrowid#guarda el id que se genera al insertar
            cursor.close()#termina el proceso

            if self.rol=="medico":
                cursor.execute("insert into medicos (id_usuario) values (%s)", (id_generado))
                id_medico=cursor.lastrowid
                conn.commit()
                cursor.close()
                if self.lista:
                    cursor.execute("insert into ")

            elif self.rol=="paciente":
                cursor.execute("insert into pacientes (id_usuario, historial_medico) values (%s, %s)", (id_generado, None))
                conn.commit()
                cursor.close()



            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar los datos:\n{str(e)}")
        finally:
            conexion.cerrarConexion()