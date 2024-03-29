class College:
    def __init__(self, c_name, c_address):
        self.c_name = c_name
        self.c_address = c_address

    def show_info(self):
        print(f"College Name: {self.c_name}")
        print(f"Address: {self.c_address}")

class Staff(College):
    def __init__(self, c_name, c_address, s_id, s_name, designation):
        College.__init__(self, c_name, c_address)
        self.s_id = s_id
        self.s_name = s_name
        self.designation = designation

    def display_info(self):
        College.show_info(self)
        print(f"Staff ID: {self.s_id}")
        print(f"Staff Name: {self.s_name}")
        print(f"Staff Designation: {self.designation}")

class Student(Staff):
    def __init__(self, c_name, c_address, s_id, s_name, designation, st_id, st_name, st_branch):
        Staff.__init__(self, c_name, c_address, s_id, s_name, designation)
        self.st_id = st_id
        self.st_name = st_name
        self.st_branch = st_branch

    def show(self):
        Staff.display_info(self)
        print(f"Student ID: {self.st_id}")
        print(f"Student Name: {self.st_name}")
        print(f"Student Branch: {self.st_branch}")

s1=Student("sanjay ghodawat university","Kolhapur",22,"mrunal","program coordinator",22221491016,"Rachana","McA")
s1.show()

