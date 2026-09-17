
#Abstraction - Hiding the implementation

# to import the abstraction 
from abc import ABC, abstractmethod

class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def checkout(self):    # abstract class may have non-abstract methods 
        pass


class WebApp(FeaturePlan):
    def login(self):    # all the abstract methods must be overrided and functionality must be written here
        print("Web app login") 

    def logout(self):
        print("Web app logout")

    def checkout(self):      # not mandatory to override the non-abstract method that wont make any error
        print("Web app checkout")

app=WebApp()
app.login()
app.logout()
app.checkout()

