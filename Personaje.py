
class Personaje:
    
    #Creamos al constructor
    def __init__(self, esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
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
        print("El arma tiene ahora "+ str(cargador) +"balas") 
          
    