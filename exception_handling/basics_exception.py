

# Below code shows error 

# a=10
# b=0
# result=a/b
# print("Result : " , result)


# But here the error is handled by exception handling

# Exception handling uses try, throw, except, finally to handle errors 
# Common errors
# ValueError, TypeError, IndexError , KeyError , AttributeError, ZeroDivisionError , FileNotFoundError  , ImportError /ModuleNotFoundError ,  NameError , SyntaxError, TndentationError , RecursionError , MemoryError .


# if we dont know the exception type then just give 'Exception' 


try:
    a=10
    b=0
    result=a/b
    print("Result : " , result)
except ZeroDivisionError:
    print("Can't divide by zero ")
finally:
    print("finally is printed")
