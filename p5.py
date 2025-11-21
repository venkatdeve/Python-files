import re

text = "My phone number is 9876543210"


#re.match() matches Only the Start of the String


print(re.match(r"My",text))

#re.findall() returns all matches as a list
print(re.search(r"\d+",text))

for i in text:
    if re.search(r"\d+", i):
        print(i , end="")