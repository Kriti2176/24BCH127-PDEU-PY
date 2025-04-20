import random
lst = [random.randint(1, 30) for _ in range(50)]
print("Original:", lst)
lst = list(set(lst))
print("Unique:", lst)
