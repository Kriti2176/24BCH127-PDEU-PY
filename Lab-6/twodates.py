from datetime import date
d1 = (10, 4, 2024)
d2 = (18, 4, 2025)
days = (date(d2[2], d2[1], d2[0]) - date(d1[2], d1[1], d1[0])).days
print("Days between:", days)
