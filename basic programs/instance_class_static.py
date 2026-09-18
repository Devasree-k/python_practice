
# Instance means object method called through object creation
# Class level method is accessed through the class name
# Static method is like class level  - its a utility helper  and independent 


class Myclass:
    def instance_method(self):
        print("Instance method called")
    @classmethod
    def class_method(self):
        print("Class method called")
    @staticmethod
    def static_method():
        print("Static method called")

obj=Myclass()
obj.instance_method()
Myclass.class_method()
Myclass.static_method()


# Class method example

class Employee:
    company_name="Company name"

    @classmethod
    def change_company_name(cls,new_company_name):
        cls.company_name=new_company_name

Employee.change_company_name("Company1 name")
print(Employee.company_name)


# static method example

class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(3,4))






