from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # Metodo para crear conexiones 
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/lOkY/Documents/GitHub/POO181/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se puedo conectar")
    
    #Metodos para Guardar Usuarios   
    def guardarUsuario(self,nom,cor,con):
        
        #1. usamos una conexion
        conx= self.conexionBD()
        
        #2. Validar parametros Vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas", "Formulario Incompleto")
        else: 
            # 3.Preparamos Cursor,Datos,QuerySQL
            cursor= conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert= "insert into TBRegistrados(nombre,correo,contra) values(?,?,?)" 
            
            #4. Ejecutar Insert y cerramos Conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito","Usuario Guardado")  
            
            
    # Metodo para encriptar Constraseñas        
    def encriptarCon(self,con):
        conPlana= con
        
        #preparamos contraseña en bytes y la SAL
        conPlana= conPlana.encode() # convertimos con a bytes
        sal= bcrypt.gensalt()
        
        #Encryptamos la contraseña
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        #enviamos la contraseña Encryptada
        return conHa
            


