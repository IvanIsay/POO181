from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from controladorBD import *  #1. Presentamos los archivos Controlador & Vista

#2. Creamos 1 objeto de la Clase ControladorBD
controlador= controladorBD()

#3. Funcion para disparar el boton
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

#4. Funcion para disparar el boton de busqueda 
def ejecutaSelectU():
    usuario= controlador.consultarUsuario(varBus.get())
    for usu in usuario:
      cadena= str(usu[0])+ " " + usu[1]+ " "+ usu[2]+ " "+ str(usu[3])

    if(usuario):
        print(cadena)
    else:
        messagebox.showinfo("No encotrado","Ese Usuario no existe en la BD")


Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill='both',expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

# Pestaña1: Formulario de usuarios

titulo= Label(pestana1,text="Registro de usuarios", fg='blue',font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(pestana1, text= "Nombre: ").pack()
txtNom= Entry(pestana1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1, text= "Correo: ").pack()
txtCor= Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text= "Contraseña: ").pack()
txtCon= Entry(pestana1,textvariable=varCon).pack()

btnGuardar= Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()


# Pestaña2: Buscar usuario

titulo2= Label(pestana2,text="Buscar Usuario", fg='green',font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(pestana2, text= "Identificador Usuario: ").pack()
txtid= Entry(pestana2,textvariable=varBus).pack()
btnBus= Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus= Label(pestana2,text="Encontrado:", fg='blue',font=("Modern",15)).pack()
textEnc= tk.Text(pestana2,height=5,width=52).pack()




panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar Usuario')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuario')

Ventana.mainloop()