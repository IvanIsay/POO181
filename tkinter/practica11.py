
from tkinter import Tk,Frame,Button

#1.Instaciamos un Objeto Ventana
ventana= Tk()
ventana.title(" Practica 11:3 Frames")
ventana.geometry("600x400")

#2.Definimos Secciones de la ventana
seccion1=Frame(ventana,bg="#b32d00")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="#2952a3")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="#ff99cc")
seccion3.pack(expand=True,fill='both')
#3.botones
botonAzul= Button(seccion1,text="boton azul",fg="blue")
botonAzul.place(x=60, y=60)

botonAmarillo= Button(seccion2,text="boton amarillo",bg="#ffff1a")
botonAmarillo.grid(row=0, column=0)

botonNegro= Button(seccion2,text="boton negro",fg="white",bg="black")
botonNegro.grid(row=1, column=1)

botonVerde= Button(seccion3,text="boton Verde",bg="#239023")
botonVerde.pack()





#Main de ejecucion de la ventana
ventana.mainloop()