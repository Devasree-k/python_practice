

# Loopings

#for loop   - iteration is known

names = ["anu", "priya", "hari", "janani"]
for test in names:
    print(test.upper())



#while loop   - iteration is not known 

correct_pin='1234'
entered_pin=''
while entered_pin != correct_pin:
    entered_pin=input("enter your correct pin:")
print("Successful")



#break to end the loop 

for i in range (10):
    if i==5:
        break
    print(i)

# continue will skip the value that doesn't satisfy the condition 

arr=[10,-5,7,-2,0]
for num in arr:
    if num<0:
        continue
    print(num)

# pass is the placeholder

arr=[10,-5,7,-2,0]
for num in arr:
    pass # for future logic like placeholder....






