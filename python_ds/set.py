
# Set

# set is unordered and mutable

names = ["anu","priya","hari"]

to_set = set(names)   # To convert list into set


uber_cities1= {"chennai","coimbatore","chennai","Madurai"}
uber_cities2= {"chennai","bangalore","Delhi","coimbatore"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities1.difference(uber_cities2))

uber_cities1.add("Erode")
print(uber_cities1)

uber_cities1.remove("Madurai")
print(uber_cities1)

# cant use indexing in set

my_sets={1,2,3}
my_sets.remove(1)
print(my_sets)
my_sets.add(5)
print(my_sets)


#my_sets.remove(8)  # this will raise an error because 8 is not there in the list so we can use discard to remove an item safely from set

my_sets.discard(8)
print(my_sets)

