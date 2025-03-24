from abc import ABC, abstractmethod

class Balwan(ABC):

    @abstractmethod
    def tworzenie(self):
        pass

    @abstractmethod
    def eliminacja(self):
        pass

class CyrkNaKolkach(Balwan):

    def tworzenie(self):
        return "Balwan powstal"
    def eliminacja(self):
        return "Balwan umarl"

class Cyrk(CyrkNaKolkach):
    pass

person = Cyrk()
print(person.tworzenie())
print(person.eliminacja())
