
# Step 1: Function for converting list of names into dictionary
def list_to_dict(names):
    #Adding numbers into dict from 1 to end
    indexed_dict = {}
    for i, name in enumerate(names, start=1):  # index + values
        indexed_dict[i] = name.upper()        # Storing upper case letters
    return indexed_dict

#Function for reversing dict
def reverse_dict(original_dict):
    #Storing values
    reversed_dict = {}
    for key, value in original_dict.items():
        reversed_dict[value] = key
    return reversed_dict

#List of names
names_list = ["Satish","Mahi","Santu","Naveen"]

#transforming in dict
indexed_dictionary = list_to_dict(names_list)

# reversing dictionary
reversed_dictionary = reverse_dict(indexed_dictionary)

# indexed dictionary
print(indexed_dictionary)

# reversing dictionary
print(reversed_dictionary)