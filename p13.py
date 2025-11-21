num = int(input("enter a number"))

boolean = True
for i in range(2 , num):
    if num % i == 0:
        print("num is not a prime number")
        boolean = False
        break
if boolean :
    print("num is prime")

string = "Rama went to school"
if "Rama" in string:
    print(string)
else:
    print("No")

