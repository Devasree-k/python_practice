

# String handling and manipulations

#It can be number , character or combinations of them

name = "Deva"

print(name.lower())
print(name.upper())
print(name.capitalize())


mobile = "9789087655"
masked = mobile[:2] + "******" +mobile[-2:]
print(masked)


# To format the string properly
#title - function to make the first letter of everyword in sentence to be capital .

string1 = "this Is SampLe"
String2 = " SentenCE"

formatted = f"{string1.title()} - {String2.title()}"
print(formatted)

#replace

location = "Muthalipalayam"
change_location = input("Enter the changed location  : ")  #to get string input 
changed_location = location.replace(location,change_location)  # Replace function to replace the value 
print(changed_location)


#split - to seperate the words      .... and ..... strip - to remove the unwanted space in the sentence.

message = "Your user id is: US10234.Please keep it safe for further use."
user_id = message.split(":")[1].split(".")[0].strip()

print(user_id)


#to check whether a word is there in the sentence or not ?
Sentence = "You got Bonus points"
if "Bonus" in Sentence:
    print("Excellent Work")
else:
    print("Normal ")

#to check the position of particular work in the sentence
print("Position of got ", Sentence.find("got"))


word_count = len(Sentence.split(" "))
print(word_count)








