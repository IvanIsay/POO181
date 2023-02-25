
class Personaje:
    
    #Creamos al constructor
    def __init__(self, esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #Metodos Personaje
    
    def correr(self,status):
        if(status):
            print("el personaje "+ self.__nombre + " esta corriendo" )
        else: 
            print("el personaje "+ self.__nombre + " se detuvo" )   
    
    
    def lanzarGranada(self):
        print("Se lanzo Granada ") 
        
    def recargarArma(self, municiones):
        cargador= 5
        cargador = cargador + municiones
        print("El arma tiene ahora "+ str(cargador) +"balas") 
        
     #Ejemplo de metodo Privado   
    def __pensar(self):
        print("Toy pensando...........")
        
        
        
        
        
     
     #Declaramos los Getters y Setters de los atributos privados
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie= esp
       
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura= alt
                 
    