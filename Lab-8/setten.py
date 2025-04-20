import random
s = set(random.randint(15, 45) for _ in range(10))
print("Original set:", s)
print("Less than 30:", len([x for x in s if x < 30]))
s = {x for x in s if x <= 35}
print("After deletion:", s)
