
class Personaje:
    
    #atributos del personaje
    especie= "Humano"
    nombre= "Marcus fenix"
    altura= 1.90
    
    #Metodos Personaje
    
    def correr(self,status):
        if(status):
            print("el personaje "+ self.nombre + " esta corriendo" )
        else: 
            print("el personaje "+ self.nombre + " se detuvo" )   
    
    
    def lanzarGranada(self):
        print("Se lanzo Granada ") 
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador = cargador + municiones
        print("El arma tiene ahora "+ cargador +"balas") 
          
    