fl = open("sample.txt", "r")
text1 = fl.read()
text = text1.lower()
print("Name Found: ", text.count("prahar"))
fl.close()
 
def moon(n):
    for i in range(n, 0, -1):
        print("*"*i)
moon(5)
