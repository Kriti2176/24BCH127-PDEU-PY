import random
lst = [random.randint(-50, 50) for _ in range(30)]
print("All:", lst)
pos = [x for x in lst if x > 0]
neg = [x for x in lst if x < 0]
print("Positive:", pos)
print("Negative:", neg)
