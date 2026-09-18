

# with open("file_handling\input_file.csv","r") as infile, open ("file_handling\_output.txt", "w") as outfile:

#     for line in infile:
#         print(line.strip())
#         outfile.write(line)



# to view only the age column in the csv file 

# import csv

# with open("file_handling\input_file.csv","r")as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row["age"])


# to view only the certain column without their name but but using the index value of the column

with open("file_handling\input_file.csv","r")as file:
    lines=file.readlines()
    for line in lines[1:]:
        column=line.strip().split(",")
        print(column[2])
