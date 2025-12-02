#String ==> collection of characters , numbers , special characters which are represented in " " double quotes

#variable
name = "venkat"
print(name)
name = 'varma'
print(name)
li = list(name)
print(li)
#String indexing
print(name[0])
print(len(name))
print(name[::-1])
print(name[1:6:2])
#List = collection of elements it follows sequencing  and mutable , indexing , duplicates
li = [1, "venkat", 2]
print(li)
li.append(3)
print(li)

#tuple - collections of elements indexing , immutable , duplicates
tu = (1 , 2, "venkat" , 3)
print(tu[2])

#set = collections of element , unique elements , mutable , non indexing
set1 = set()
print(type(set1))
set1 = {1 , 2, 3 }
set1.add(1)
print(set1)
set1.update([20 , 3])
print(set1)

#dict = key-Value pairs
dict1 = {1: "https:192.168.1.41",2 : "https:192.168.1.42"}
print(dict1[1])


for key in dict1.keys():
    print(dict1[key])

print(dict1.get(4))
