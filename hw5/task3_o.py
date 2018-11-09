#spiral digits
nm = list(eval(input())) #columns/rows
curr_point = [0, 0]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
curr_dir = 0
curr_num = 0
matrix = [0] * nm[0]
for i in range(nm[0]):
    matrix[i] = [-1] * nm[1]

def matPrint (m):
    for i in range (nm[1]):
        rst = str(m[i][0])
        for j in range (1, nm[0]):
            rst += " " + str (m[j][i])
        print (rst)

for i in range (nm[0] * nm[1]):
    matrix[curr_point[0]][curr_point[1]] = curr_num
    curr_num = (curr_num + 1) % 10
    next_0 = curr_point[0] + directions[curr_dir][0]
    next_1 = curr_point[1] + directions[curr_dir][1]

    while (next_0 >= nm[0]) or (next_0 < 0) or (next_1 >= nm[1]) or (next_1 < 0) or (matrix[next_0][next_1] >= 0):
        curr_dir = (curr_dir + 1) % 4
        next_0 = curr_point[0] + directions[curr_dir][0]
        next_1 = curr_point[1] + directions[curr_dir][1]
    curr_point = [next_0, next_1]

matPrint(matrix)
