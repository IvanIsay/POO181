
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

#Ejemplo del uso del Set
Heroe.setNombre("Pepe pecas")

#4. Acceder a atributos y metodos del cada OBJ

print("")
print("##  Atributos y Metodos del Heroe ##")
print("El personaje pertenece a la raza: "+ Heroe.getEspecie() )
print("Se llama : "+ Heroe.getNombre() )
print("mide : "+ str(Heroe.getAltura() ) +  " Metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

#Ejemplo de lo que no se puede hacer
#Heroe.__pensar()


print("")
print("##  Atributos y Metodos del villano ##")
print("El personaje pertenece a la raza: "+ Villano.getEspecie() )
print("Se llama : "+ Villano.getNombre() )
print("mide : "+ str(Villano.getAltura() ) +  " Metros")
print("")

Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)