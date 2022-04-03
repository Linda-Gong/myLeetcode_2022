from collections import deque
a = [1, 3, 5]
b = [8,8,8]
dq = deque(a)
print(dq)
while dq:
    for _ in range(len(dq)):
        print("len = ",)
        node = dq.pop()
        if node > 5:
            print("--:",  node)
        else:
            dq.extendleft(b)

        print("*****", dq)


