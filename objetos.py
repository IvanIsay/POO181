
#1. importar la clase
from Personaje import *

#2.Solicitar atributos para el objeto
print("")
print("### Solicitud de datos Heroe ###")
espH= input("Escribe el especie del Heroe")
nomH= input("Escribe el nombre del Heroe")
altH= float(input("Escribe la altura del Heroe"))
cargaH= int(input("Cuantas bala se recargaran al heroe"))

print("")
print("### Solicitud de datos Villano ###")
espV= input("Escribe el especie del Villano")
nomV= input("Escribe el nombre del Villano")
altV= float(input("Escribe la altura del Villano"))
cargaV= int(input("Cuantas bala se recargaran al Villano"))


#3.Creamos 2 objetos de personaje
Heroe= Personaje(espH,nomH,altH)
Villano= Personaje(espV,nomV,altV)

#4. Acceder a atributos y metodos del cada OBJ

print("")
print("##  Atributos y Metodos del Heroe ##")
print("El personaje pertenece a la raza: "+ Heroe.especie)
print("Se llama : "+ Heroe.nombre)
print("mide : "+ str(Heroe.altura) +  " Metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)


print("")
print("##  Atributos y Metodos del villano ##")
print("El personaje pertenece a la raza: "+ Villano.especie)
print("Se llama : "+ Villano.nombre)
print("mide : "+ str(Villano.altura) +  " Metros")
print("")

Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)