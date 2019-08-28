from Person import Person

class Employee(Person):
    "Common base class for all employees"
    
    emp_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.occupation = "employee"
        
        Employee.emp_count += 1
        
        print("\nExtra info for Employee class")
        print(f"properties: {self.__dict__}")
        print(f"doc: {self.__doc__}")
        print(f"class name: {__name__}")
        print(f"module name: {self.__module__}")
        print(f"base class: {Employee.__bases__}\n")
        
    def talk(self):
        print(f"I'm a {self.occupation}")
        
    def __del__(self):
        print(f"Object {__name__} is destroyed")
