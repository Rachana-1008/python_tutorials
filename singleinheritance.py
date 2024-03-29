'''class college:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(college):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} with ID {self.student_id} is studying.")

student_instance = Student("Alice", 20, "ST123")

student_instance.display_info()  
student_instance.study() '''    

class College:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(College):
    def study(self):
        print(f"{self.name} is studying.")

student = Student("Samiksha", 20)

student.display_info()  
student.study()         