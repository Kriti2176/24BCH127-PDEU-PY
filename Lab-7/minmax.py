data = {"HR": [10000, 12000], "IT": [20000, 25000, 22000], "Sales": [15000]}
for dept in data:
    print(dept, "Min:", min(data[dept]), "Max:", max(data[dept]))
