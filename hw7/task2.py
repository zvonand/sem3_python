currpair = list(eval(input()))
dct = {}
num = -1
while currpair[0] != 0 or currpair[1] != 0:
    if currpair[0] > num:
        num = currpair[0]
    if currpair[1] > num:
        num = currpair[1]


    if currpair[0] in dct:
        if not (currpair[1] in dct[currpair[0]]):
            dct[currpair[0]].append(currpair[1])
    else:
        dct[currpair[0]] = [currpair[1]]

    if currpair[1] in dct:
        if not (currpair[0] in dct[currpair[1]]):
            dct[currpair[1]].append(currpair[0])
    else:
        dct[currpair[1]] = [currpair[0]]

    currpair = list(eval(input()))


out = ""
for key, val in dct.items():
     if len(val) == num:
        out += str(key) + " "
print (out)


