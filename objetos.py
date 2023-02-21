
#1. importar la clase
from Personaje import *


#2.Instanciar un objeto
Heroe= Personaje()


#3. Acceder a sus atributos

print("ATRIBUTOS PERSONAJE")
print("El personaje pertenece a la raza: "+ Heroe.especie)
print("Se llama : "+ Heroe.nombre)
print("mide : "+ str(Heroe.altura) +  " Metros")
print("")

print("METODOS PERSONAJE")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)