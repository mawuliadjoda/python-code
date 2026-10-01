class Vehicule:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"Vehicule name: {self.name}, Year: {self.year}"
    
class Car(Vehicule):
    def __init__(self, name, year, mileage):
        super().__init__(name, year)
        self.mileage = mileage
    def __str__(self):
        return f"Car name: {self.name}, Year: {self.year}, Mileage: {self.mileage}"
    

print(issubclass(Car, Vehicule))  # Output: True
print(issubclass(Vehicule, object))  #Output: True

print(Car.__base__)  # Output: (<class 'object'>,)