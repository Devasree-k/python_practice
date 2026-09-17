
#access specifier  - public (default), private (uses __ ), protected (uses _ )

class Parent:
    def __init__(self):
        self.public_var="Public"
        self.__private_var="Private"
        self._protected_var="Protected"

    def access_from_same_class(self):
        print("Inside the Parent class : ")
        print("Public", self.public_var)
        print("Private", self.__private_var)
        print("Protected", self._protected_var)

class Child(Parent):
    def access_from_childclass(self):
        print("Inside the child class:")
        print("Public", self.public_var)
        try:
            print("Private", self.__private_var)
        except AttributeError:
            print("Error")
        # print("Private", self.__private_var)
        print("Protected", self._protected_var)

class Stranger:

    def access_from_other_class(self,obj):
        print("Inside the Stranger class:")
        print("Public", obj.public_var)
        try:
            print("Private", obj.__private_var)
        except AttributeError:
            print("CANNOT ACCESS Error")
        print("Protected", obj._protected_var)


p=Parent()
c=Child()
s=Stranger()
p.access_from_same_class()

c.access_from_childclass()

s.access_from_other_class(p)




