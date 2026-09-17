
# function is a block of reusable code

def greet():
    print("Welcome")

greet()

#function with arguments
def greet2(name):
    print(f"Hello {name}")

greet2("Deva")


def addition(*args):
    total = 0
    for num in args:
        total += num
    return total
print(addition(1,2,3,4))


# to get it as key . value pairs

def create_pofile(**kwargs):
    print("User profile")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
create_pofile(name="deva", age=20,job="software engineer")


#function with return
def add(a,b):
    return a+b

result = add(3,4)
print(result)