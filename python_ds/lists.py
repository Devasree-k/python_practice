# lists

# list is mutable (changeable) , can contain multiple datatypes ,

playlist = ["Believer","Pookal_Pookum","Nenjodu"]

print("Playlist", playlist)

# List methods

playlist.append("azhage azhage")

playlist.insert(0,"Kadhaipoma")

playlist.remove("Pookal_Pookum")

playlist.pop()

playlist.sort()

playlist.reverse()

playlist[1]="Kanmani"   #list is mutable 

print("count",playlist.count("Believer"))
print("top 2 songs ", playlist[:2])
print("last 2 locations ", playlist[-2:])
print(playlist)

#list iteration

for songs in playlist:
    print(songs)

#check is item exists

if "Believer" in playlist:
    print(playlist.index("Believer"))


#list with multiple datatypes
print("List data :")
data = ["Deva",20,85.4]
for a in data:
    print(a)



# we can use enumerate if we want to know the index position of the data .... Enumerate will return the data along with the index value so we need two variables

locations=["Coimbatore","Chennai","Bangalore"]
for i,locations in enumerate(locations):
    print(f"location {i}:{locations}")

