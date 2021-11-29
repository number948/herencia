class Vehicle:
    def Brand(self):
        pass
    
    def Color(self):
        pass
        
    
    
class Auto(Vehicle):
    def Brand(self):
        print("TOYOTA")
    def Color(self):
        print("verde")
        
class Moto(Vehicle):
    def Brand(self):
        print("HONDA")
    def Color(self):
        print("rojo")
        
class Camion(Vehicle):
    def Brand(self):
        print("VOLVO")
    
    def Color(self):
        print("amarillo")
        
    
    
for Vehicle in Auto(), Moto(), Camion():
    Vehicle.Brand()
    Vehicle.Color()
    
    