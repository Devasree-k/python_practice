
# Conditional statements

#only if condition
age=18

if age>=18:
    print("You are eligible to vote")


#if__else conditions
    
if age>=19:
    print("Eligible to vote")
else :
    print("Not eligible to vote")

#if__elif__else conditions

mark=int(input("Enter your mark  : "))

if mark>=90:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=40:
    print("Grade C")
else:
    print("Fail")


# nested if __else

age = int(input("Enter your age  :"))

if age >=18:
    print("Do you have license if 'yes' type 'y' if 'not' then type 'n'")
    has_license = input("Enter 'y' or 'n' :")
    if has_license == 'y':
        print("You can drive")
    else:
        print("Please take license first")
else:
    print("You are too young to drive")



# Use case example with discount rates....

order_amount =1000
days="sat"
membership ="no"

if(order_amount>=1000 and days in['sat','sun']) or membership=='gold':
    print("20% discount")
else:
    print("no discount")







    
