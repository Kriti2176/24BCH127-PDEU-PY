stack = []
while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        stack.append(input("Enter value: "))
    elif ch == 2:
        if stack: print("Popped:", stack.pop())
        else: print("Stack empty")
    elif ch == 3:
        print("Stack:", stack)
    else: break
