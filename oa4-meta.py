
n = 3
m = 4
queries = [[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]]

matrix = []
for i in range(1, n+1):
    matrix.append(list(range(i, i*(m+1), i)))

## get column

res = []
for x in queries:
    if x[0] == 0:
        res.append(min(min(matrix)))
    elif x[0] == 1:
        matrix.pop(x[1]-1)
    elif x[0] == 2:
        for i in range(len(matrix)):
            matrix[i].pop(x[1]-1)
            # matrix[i][x[1]-1] = None
            # matrix[i] = [x for x in matrix[i] if x]


print(res)


## get column
an_array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
column_one = [row[1] for row in an_array]
print(column_one)

column_matrix = []
for i in range(len(an_array[0])):
    col = [row[i] for row in an_array]
    column_matrix.append(col)

print(column_matrix)