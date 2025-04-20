import random

odd = [random.randrange(1, 100, 2) for _ in range(5)]
even = [random.randrange(0, 100, 2) for _ in range(4)]
print("Odd:", odd)
print("Even:", even)

odd[2:3] = even  # Replace 3rd odd with all evens
print("Modified List:", odd)

flat_sorted = sorted(odd)
print("Flattened & Sorted:", flat_sorted)
