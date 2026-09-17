

# its more like list but is immutable 
# Tuples it is immutable means data can't be changed

data=("Deva","coimbatore","CS",84,"completed")
print(data)

#access using index
print(data[1])

#loop
for item in data:
    print(item)

print(len(data))
print(data.count("coimbatore"))
print(data.index("coimbatore"))
