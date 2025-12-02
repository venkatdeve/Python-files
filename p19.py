name = "My name is Satya"
print(name[::-1])
i = len(name) - 1
print(i)
while i >= 0:
    print(name[i] , end="")
    i -= 1

#give 10 prime numbers
li = []
for i in range(2 , 100):
    for j in range(2 , i):
        if i % j == 0:
            break
    else:
        li.append(i)
print(li)

