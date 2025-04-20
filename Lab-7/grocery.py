price = {"apple": 30, "banana": 10, "milk": 50}
qty = {"apple": 2, "banana": 5, "milk": 1}
total = 0
for item in qty:
    total += price.get(item, 0) * qty[item]
print("Total Bill:", total)
