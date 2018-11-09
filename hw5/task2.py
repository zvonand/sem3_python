arr = eval (input ())
length = len (arr)
looking_area = [0] * length
looking_area[0] = 1
changed = True

while changed:
    prev_val = looking_area.copy()
    if (looking_area[-1] == 1):
        break
    for i in range(length):
        if (looking_area[i] == 1):
            if ((i > 0)):
                looking_area[i-1] = 1
            if (i + arr[i] < length):
                looking_area[i + arr[i]] = 1
    changed = not (looking_area == prev_val)

if (looking_area[-1] == 1) or (looking_area[-1] == -1):
    print ("YES")
else:
    print("NO")
