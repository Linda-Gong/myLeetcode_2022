process = [4, 10, 4, 8, 1, 2]
lst = process[1:-1]
m = 2

val_max = 0
for i in range(len(lst)-m):
    val = sum(lst[i:i+m])
    if val > val_max:
        val_max = val
print(sum(lst) - val_max)


a = [chr(x) for x in range(ord('a'), ord('z')+1)]
