circle = eval(input ())
curr = eval(input())
belong = 1
while curr != (0, 0):
    if (curr[0] - circle[0]) ** 2 + (curr[1] - circle[1]) ** 2 > circle[2] ** 2:
        belong = 0
    curr = eval(input())
print ("YES" if belong else "NO")
