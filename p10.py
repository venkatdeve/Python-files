#Dictionary = to store key : val pairs dictionary is used

#Creating an empty dict
dict1 = {1:"venkat",2:"varma"}
print(dict1)
dict1[3] = "ganesh"
print(dict1)
print(dict1)
#if I access a key that doesn't exist it gives KeyError
dict1[4] = "venkat"
if 4 in dict1:
    print(dict1.get(4))
else :
    print("element 4 is not there")
print(dict1)
dict1[5] = "vishnu"
print(dict1)
if 6 in dict1:
    print(dict1[6])
else:
    print("there is no salary")

print(dict1)
print(dict1.values())
print(dict1.items())
print(dict1.keys())
for i in dict1.keys():
    dict1[i] = i + 1
print(dict1)