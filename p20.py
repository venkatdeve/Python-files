# def main():
# #     s = input().strip()
# #     freq = {}
# #     s = sorted(s)
# #     for i in s:
# #         freq[i] = freq.get(i , 0 ) + 1
# #     for key in freq.keys():
# #         print(key , freq[key])

numbers = [1 , 1 , 2 , 3 , 4 , 5 , 5 ,5]

i = 0
while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            numbers.pop(j)
        j += 1
    i += 1
print(numbers)
# if __name__ == "__main__":
#     main()






















