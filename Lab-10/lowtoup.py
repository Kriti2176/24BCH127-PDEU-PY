with open("source.txt", "r") as source, open("target.txt", "w") as target:
    for line in source:
        target.write(line.upper())
