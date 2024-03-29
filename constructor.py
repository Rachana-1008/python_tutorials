class fruits:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("hello,my name is",self.name)

f1=fruits("apple")
f1.show()



class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show(self):
        print(f"hello,my name is {self.name} and i am {self.age} years old and my salary is {self.salary}")

e1=employee("samiksha",22,2000)
e1.show()

e2=employee("sakshi",22,5000)
e2.show()

class person:
    def __init__(self,name,gender,profession):
        self.name=name
        self.gender=gender
        self.profession=profession

    def show(self):
        print(f"my name is {self.name} and i am {self.gender} and i am a {self.profession}")
    def work(self):
        print(f"{self.name} working as a {self.profession}")
  
p1=person("Samiksha","Female","Softwrae Engineer")
p1.show()
p1.work()

p2=person("Sakshi","Female","Electrical Engineer")
p2.show()
p2.work()

class myself:
    def __init__(self,name,education,university,domain):
        self.name=name
        self.education=education
        self.university=university
        self.domain=domain

    def show(self):
        print(f"my name is {self.name} and i am studying {self.education} in  {self.university}, and i am specialized in {self.domain} domain.")
 
  
m1=myself("Samiksha","MCA","sanjay ghodawat university","python")
m1.show()




