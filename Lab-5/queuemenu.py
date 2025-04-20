queue = []
while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        queue.append(input("Enter value: "))
    elif ch == 2:
        if queue: print("Dequeued:", queue.pop(0))
        else: print("Queue empty")
    elif ch == 3:
        print("Queue:", queue)
    else: break
