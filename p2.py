#number even or odd


number = 100
if number % 2 == 0:
    print("Even" , number)
else:
    print("Odd",number)

#numbers even or odd
li_odd = ()
li_even = ()
print(type(li_odd))
for number in range(1 , 101):
    if number % 2 == 0:
        li_even += (number,)
    else:
        li_odd += (number,)

print("List of Odd numbers =" , li_odd)
print("List of Even numbers =",li_even)
