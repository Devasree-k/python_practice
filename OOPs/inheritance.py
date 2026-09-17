
# Inheritance - basic advantage is code reusability


#single level inheritance

class Parent:
    def house(self):
        print("Parent class")


class Child(Parent):
    def factory(self):
        print("Child class")

c=Child()
c.house()
c.factory()


#multilevel inheritance

class grandParent:
    def car(self):
        print("Red car")
class Parent(grandParent):
    def house(self):
        print("Parent class")
class Child(Parent):
    def factory(self):
        print("Child class")

a=Child()
a.house()
a.factory()
a.car()


# hierarchical inheritance

class Parent:
    def house(self):
        print("Parent class")
class Child1(Parent):
    def factory(self):
        print("Child 1 factory")
class Child2(Parent):
    def shop(self):
        print("Child 2 shop")

a=Child1()
a.house()
a.factory()

b=Child2()
b.house()
b.shop()


#Multiple inheritance
class dad:
    def house(self):
        print("dad class")
class mom:
    def shop(self):
        print("mom class")
class daughter(dad,mom):
    def factory(self):
        print("Factory")
d=daughter()
d.shop()
d.factory()
d.house()


#hybrid -  combination of different types of inheritance





