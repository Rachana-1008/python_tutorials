'''class p1():
    def p1_info(self):
        print("parent class")
class p2():
    def p2_info(self):
        print("second class")
+
class c1(p1,p2):
    def c1_info(self):
        print("child class")
        
obj = c1()
obj.p1_info()
obj.p2_info()
obj.c1_info()'''

'''class Person:
    def __init__(self, name, age,tname):
        self.name = name
        self.tname = tname
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class Faculty(Person):
    def teach(self):
        print(f"{self.tname} is teaching to {self.name}")

class TeachingAssistant(Student, Faculty):
    pass

ta = TeachingAssistant("samiksha", 25,"mrunal")

ta.display_info()   
ta.study()           
ta.teach()    '''

class Engine:
    def start_engine(self):
        print("Engine is starting.")

class Wheels:
    def rotate_wheels(self):
        print("Wheels are rotating.")

class Lights:
    def turn_on_lights(self):
        print("Lights are turning on.")

class Car(Engine, Wheels, Lights):
    def drive(self):
        print("Car is driving.")

car_instance = Car()

car_instance.start_engine()    
car_instance.rotate_wheels()   
car_instance.turn_on_lights()  
car_instance.drive()         



        
