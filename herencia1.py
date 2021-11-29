class Vehicle:
    def __init__(self, brand, color, tipo):
        self.tipo = tipo
        self.brand = brand
        self.color = color
      
    def __str__(self):
        return "tipo de vehículo {},marca {}, color {}".format(self.tipo, self.brand, self.color)
    
    
class Car(Vehicle):
    def __init__(self, brand, color, tipo):
        self.tipo = tipo
        self.brand = brand
        self.color = color
        
    def __str__(self):
        return  "tipo de vehículo {},marca {}, color {}".format(self.tipo, self.brand, self.color)     
         
class Motorcycle(Vehicle):
    def __init__(self, brand, color, tipo):
        self.tipo = tipo
        self.brand = brand
        self.color = color

    def __str__(self):
        return  "tipo de vehículo {}, marca {}, color {}".format(self.tipo,self.brand, self.color) 
      
car = Car("Toyota","azul", "auto")
motorcycle = Motorcycle("HYUNDAI", "rojo", "moto")
print(car)
print(motorcycle)