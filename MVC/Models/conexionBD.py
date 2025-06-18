import mariadb as sql
from tkinter import messagebox

class ConexionBD():
    def __init__(self):
        self.__host = "localhost"
        self.__port = 3307
        self.__user = "root"
        self.__pasword = ""
        self.__database = "hospital"
        self.__connection= None

    def getConnection(self):
        return self.__connection
    
    def crearConexion(self):
        try:
            self.__connection= sql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__pasword,
                port=self.__port,
                database=self.__database
            )
        except sql.OperationalError as er:
            messagebox.showwarning("Advertencia", "Verifique su conexion a internet.\n Intente de nuevo mas tarde.\n O contacte al administrador del sistema")
               
    def cerrarConexion(self):
        if self.__connection:
            self.__connection.close()
            self.__connection=None 