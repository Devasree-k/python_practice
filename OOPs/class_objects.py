
# maintainability, reusability , readability

#class is a blue-print of object

class Greeting:
    def say_hello(self):
        print("hello")

s1=Greeting()
s1.say_hello()


#constructor - automatically called when object is created

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name} , Age :{self.age}")

s1=Student("Anu",23)
s1.display()

# other example for constructor

class Employee:
    def __init__(self,name,aadhaar):
        self.name=name
        self.aadhaar=aadhaar
    def enter_office(self):
        print("enter office")
    def open_bank_account(self):
        print(f"Bank account opened fpr {self.name} with aadhaar {self.aadhaar}")


emp1=Employee("Keerthi",23)
emp1.enter_office()
emp1.open_bank_account()