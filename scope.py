#Variable scope

#Local Scope

def user():
    name="Deva"
    print("Name is :", name)
user()


#Enclosed scope

def card():
    discount=10  #enclosed

    def checkout():
        print("Applying discount :",discount)

    checkout()
    card()


#Global

user="Anu"
def homePage():
    print("Welcome : ", user)
def profile():
    print("Welcome your Profile name is : ",user)
profile()
homePage()

#bulid in variable and functions like len, case , etc....,

print(__file__)


""" This is one type of multiline comments  """

''' This is one type of multiline comments  '''




