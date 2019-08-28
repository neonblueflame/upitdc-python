# If the module isn't found, Python searches each directory 
# in the env var PYTHONPATH (Linux) then, in default path, 
# which is /usr/local/lib/python in Linux
from Person import Person
from Employee import Employee

# Creating person 1
person1 = Person()
print(type(person1))
print(person1)

person1.name = "Person1"
person1.thought = "Hello"

print(person1.name)
print(person1.thought)

# Adding new property
person1.age = 10
print(person1.age)

person1.talk()

# Deleting property
del person1.name

try:
    print(person1.name)
except AttributeError as e:
    print(e)

# Creating person2, which is an employee
person2 = Employee("Person2", 1000)
print(type(person2))
print(person2)

print(hasattr(person2, "age"))
print(getattr(person2, "name"))

print(setattr(person2, "age", 8))
print(person2.age)

print(delattr(person2, "salary"))

try:
    print(person2.salary)
except AttributeError as e:
    print(e)

try:
    for prop in person2:
        print(prop)
except TypeError as e:
    print(e)

# Replacing default occupation value
person2.talk()
person2.occupation = "Programmer"
person2.talk()
    
print(Employee.emp_count)

# Creating person 3
person3 = Person()
person3.name = "Zombie"

person3.thought = "Braiiinss!"
person3.talk()

person3.__inner_thought = "zZZ..."
try:
    person3.__inner_talk()
except AttributeError as e:
    print(e)

print(f"person3 properties: {person3.__dict__}")

person3._Person__inner_thought = "zZZ..."
try:
    person3._Person__inner_talk()
except AttributeError as e:
    print(e)
