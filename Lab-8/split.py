names = {"Amit", "Anu", "Bala", "Bobby", "Arun"}
a_set = {n for n in names if n.startswith("A")}
b_set = {n for n in names if n.startswith("B")}
print("A:", a_set)
print("B:", b_set)
