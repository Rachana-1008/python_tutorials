class Company:
    def __init__(self,c_name,c_address):
        self.c_name=c_name.upper()
        self.c_address=c_address.upper()
    def com_info(self):
        print(f"COMPANY NAME:{self.c_name}")
        print(f"COMAPANY ADDRESS:{self.c_address}")

class Manager(Company):
    def __init__(self,c_name,c_address,m_id,m_name,m_dept):
        Company.__init__(self,c_name,c_address)
        self.m_id=m_id
        self.m_name=m_name.upper()
        self.m_dept=m_dept.upper()
    def manager_info(self):
        Company.com_info(self)
        print(f"MANAGER ID:{self.m_id}")
        print(f"MANAGER NAME:{self.m_name}")
        print(f"MANAGER DEPARTMENT:{self.m_dept}")


class Employee(Company):
    def __init__(self,c_name,c_address,emp_id,emp_name,emp_pos,emp_salary):
        Company.__init__(self,c_name,c_address)
        self.emp_id=emp_id
        self.emp_name=emp_name.upper()
        self.emp_pos=emp_pos.upper()
        self.emp_salary=emp_salary
    def employee_info(self):
        Company.com_info(self)
        print(f"EMPLOYEE ID: {self.emp_id}")
        print(f"EMPLOYEE NAME: {self.emp_name}")
        print(f"EMPLOYEE POSITION: {self.emp_pos}")
        print(f"EMPLOYEE SALARY: {self.emp_salary}")

m1=Manager("sumago","pune",54,"snehal","it project manager")
e1=Employee("sumago","pune",142,"Rachana","project developer",80000)

m1.manager_info()
e1.employee_info()
       






        