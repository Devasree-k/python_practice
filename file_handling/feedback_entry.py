feedback=input("Enter your feedback : ")

with open("file_handling\_feedback.txt","a")as log:
    log.write(feedback + "\n")

print("Thanks! Your feedback is saved. ")