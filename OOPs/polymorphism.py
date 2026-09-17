
#Polymorphism

# Same methid which acts differently in different scenarios

# there is no method over loading


# method overriding

class Parent:
    def house(self):
        print("Parent class")


class Child(Parent):
    def factory(self):
        print("Child class")

    def house(self):
        print("Child class")

c=Child()
c.house()
c.factory()
