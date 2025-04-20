import csv

data_dict = {}
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row["Subject1"]) + int(row["Subject2"]) + int(row["Subject3"])
        data_dict[row["Roll No"]] = {
            "name": row["Name"],
            "subjects": [int(row["Subject1"]), int(row["Subject2"]), int(row["Subject3"])],
            "total": total
        }

print(data_dict)
