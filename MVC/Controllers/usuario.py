from tkinter import messagebox
from Models.conexionBD import ConexionBD


class Usuario():
    
    def __init__(self, cedula):
        self.cedula=cedula
        self.id_usuario=None
        self.nombre_usuario=None
        self.apellido_usuario=None
        self.rol=None

    def iniciar_sesion(self):
        conexion=ConexionBD()
        conexion.crearConexion()
        conn=conexion.getConnection()
        cursor= conn.cursor()

        try:
            consulta=("select * from usuarios")
            cursor.execute(consulta)
            listausuarios=cursor.fetchall()
            for usuario in listausuarios:
                if usuario[1]==self.cedula:
                    id_usuario= usuario[0]
                    self.nombre_usuario= usuario[2]
                    self.apellido_usuario= usuario[3]
                    self.rol= usuario[6]
                    if self.rol=="administrador":
                        messagebox.showinfo("informacion", f"Acceso correcto |Administrador|\nBienvenid@ {self.nombre_usuario} {self.apellido_usuario}")

                    elif self.rol=="recepcionista":
                        messagebox.showinfo("informacion", f"Acceso correcto |Recepcionista|\nBienvenid@ {self.nombre_usuario} {self.apellido_usuario}")

                    elif self.rol=="medico":
                        messagebox.showinfo("informacion", f"Acceso correcto |Medico|\nBienvenid@ {self.nombre_usuario} {self.apellido_usuario}")

                    elif self.rol=="paciente":
                        messagebox.showinfo("informacion", f"Acceso correcto |Paciente|\nBienvenid@ {self.nombre_usuario} {self.apellido_usuario}")


                    conexion.cerrarConexion()
                    return self.rol, id_usuario
            messagebox.showerror("Advertencia", "El numero de cedula ingresado no existe, verifique e intente nuevamente!" )

        except Exception as e:
            messagebox.showerror("ERROR",f"No se pudo ingresar. Comuniquese con el soporte:\n{str(e)}")

        finally:
            conexion.cerrarConexion()
    

    def obtener_info(self):
        return (self.id_usuario, self.cedula, self.nombre_usuario, self.apellido_usuario, self.rol)
            #tupla (id,cedula,nombre,apellido,rol)=usuario.obtener_info()
