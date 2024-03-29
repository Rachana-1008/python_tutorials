class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows.")

dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

dog_instance.make_sound()  
cat_instance.make_sound()  

