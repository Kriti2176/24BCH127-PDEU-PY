lst = ['apple', 'banana', 'mango', 'grape', 'peach']
for i in range(len(lst)):
    s = ''
    for ch in lst[i]:
        if 'a' <= ch <= 'z':
            s += chr(ord(ch) - 32)
        else:
            s += ch
    lst[i] = s
print(lst)
