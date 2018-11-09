import math
n = eval (input ())
n += 1

ubound = round (n ** 0.5)

prime = False

while not prime:
    n -= 1
    curr = True
    for i in range (2, ubound + 1):
        curr = (n % i != 0)
        if not curr:
            break
    if curr:
        prime = True

print (n)
