class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth.")

class Bird(Animal):
    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

class Bat(Mammal, Bird):
    def make_sound(self):
        print(f"{self.name} squeaks.")

bat_instance = Bat("Batty")

bat_instance.make_sound()  
bat_instance.give_birth() 
bat_instance.lay_eggs()   
