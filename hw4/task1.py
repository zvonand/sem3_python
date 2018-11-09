def moar (a, b, n):
    ca, cb = 0, 0
    for i in a:
        ca += (i%n == 0)
    for i in b:
        cb += (i%n == 0)
    return (ca > cb)

#i1 = eval(input())
#i2 = eval(input())
#n = eval(input())
#print (moar (i1, i2, n))
