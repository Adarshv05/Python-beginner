class Animal:
    a="Dog"

class Pets(Animal):
    b="Cat"

class Dog(Pets):
    def bark(self):
        print("Barkkkk Brrr")


Dog().bark()