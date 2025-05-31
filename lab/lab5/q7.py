class Dog:
    species = "Canis Familiaris"  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)


print(dog1.name)     # Buddy
print(dog2.name)     # Max
print(dog1.species)  # Canis Familiaris
print(dog2.species)  # Canis Familiaris

Dog.species = "Canis Lupus"       # Changing class variable
print(dog1.species)  # Canis Lupus
print(dog2.species)  # Canis Lupus

dog1.species = "whatever"
print(dog1.species)
print(Dog.species)
