name = "venkat"
print(name[0])
print(name[1] , name[3])
#Slicing
print(name[1:4])
#reversing a string
print(name[::-1])
#Upper
print(name.upper())
#Lower
print(name.lower())
#Substring
name1 = "varma"
name2 = "   chaitanya    Varma  "
if name1.lower() in name2.lower():
    print("the SubString exits")
else:
    print("Not exists")

#Str.strip # ignoring spaces from front and back
print(name2.strip())
print(name2.lstrip())
print(name2.rstrip())

name = name.replace(name , "reddy")
print(name)

#split
print(name.split())

#join list of Strings
li = ["apple","banana","cat"]
print("".join(li))

#To count vowels
vow_cnt = 0
for i in name:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        vow_cnt += 1

for i in name:
    if i in "aAeEiIoOuU":
        vow_cnt += 1
print(f"the vowels in the {name} word are ",vow_cnt)

freq = {}
for i in name:
    freq[i] = freq.get(i,0) + 1
print(freq)

#Check is Palindrome
name2 = 'nitin'
if name2 == name2[::-1]:
    print(f"{name2} is palindrome")
else:
    print(f"{name2} is not palindrome")

#Remove duplicates form the String
set1 = set()
for i in name:
    set1.add(i)

print("".join(set1))

str_num = "a1b2c3"
num = ""
for i in str_num:
    if i.isdigit():
        num += i

print(num)

#a1b2c3 ==> abbccc
alpha = ""
for i in range(len(str_num)):
    if str_num[i].isdigit():
        alpha += str_num[i - 1] * int(str_num[i])

print(alpha)

#Find first non-repeating character
str1 = "aabbccd"

for i in range(len(str1)):
    is_Unique = True
    for j in range(len(str1)):
        if i != j and str1[i] == str1[j]:
            is_Unique = False
            break
    if is_Unique:
        print("the first Non-repeating letter is ",str1[i])


#
sentence = "the apples are in red"
print(sentence.split())
for i in sentence.split():
    for j in range(len(i)):
        word = i[0].upper() + i[1:]
        print(word)
        break
#Reverse each word in sentence
for i in sentence.split():
    print(i[::-1] , end=" ")


#checking two strings anagrams
def anagrams(q1 , q2):
    if len(q1) != len(q2):
        print("q1 and q2 are not anagrams")
        return False
    q1 = sorted(q1)
    q2 = sorted(q2)
    for i in range(len(q1)):
        if q1[i] != q2[i]:
            print("q1 and q2 are not anagrams")
            return False
    print("q1 and q2 are  anagrams")
    return True

print()
q1 = "anagram"
q2 = "gramana"
print(anagrams(q1 , q2))

#Covert string to List of characters
name = "venkat"
charList = []
for ch in name:
    charList.append(ch)
print(charList)

name1 = "venkat"
name2 = "venkat"
for i in range(len(name1)):
    for j in range(len(name2)):
        if name1[i] == name2[j]:
            print(name1[i] , end= "")
print()

#Longest Word in Sentence
sentence = "My name is venkat Narayana Reddy"
str1 = ""
for i in sentence.split():
    if len(i) > len(str1):
        str1 = i
print(str1)