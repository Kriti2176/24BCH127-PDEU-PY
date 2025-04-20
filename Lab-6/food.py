items = [("Burger", 50), ("Pizza", 150), ("Fries", 40)]
items.sort(key=lambda x: x[1], reverse=True)
print(items)
