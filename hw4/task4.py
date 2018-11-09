n = eval (input ())
total = [0] * n
total[0], total[1], total[2] = 2, 4, 7

for i in range (3, n):
    total[i] = total[i-1] + total[i-2] + total[i-3]

print (total[-1])
