# Importujemy modul abc (Abstract Base Classes)
from abc import ABC, abstractmethod
# Definiujemy klase abstrakcyjna Base dziedziczaca po ABC
class Base(ABC):
    #Definiujemy metode abstrakcyjna area, ktora musza implementowac klasy dziedziczace
    @abstractmethod
    def area(self):
        pass
    # Definiujemy inna metode abstrakcyjna perimeter
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Base):
    def __init__(self, length, width):
        # Przypisanie atrybutow instancji
        self.length = length
        self.width = width
    # Implementujemy wymagana metode area
    def area(self):
        # Zwracamy pole powierzchni prostokata
        return self.length * self.width
    # Implementujemy wymagana metode perimeter
    def perimeter(self):
        # Zwracamy obwod prostokata
        return 2 * (self.length + self.width)

rect = Rectangle(4,5)
print("Pole prostokata: ", rect.area()) # Pole prostokata
print("Obwod prostokata:", rect.perimeter()) # Obwod prostokata

