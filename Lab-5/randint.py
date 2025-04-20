import random
lst = [random.randint(1, 100) for _ in range(20)]
print(lst)
n = int(input("Enter number to search: "))
for i in range(len(lst)):
    if lst[i] == n:
        print("Found at index", i)
