import csv

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([1, "Alice", 85, 90, 78])
    writer.writerow([2, "Bob", 80, 70, 88])
