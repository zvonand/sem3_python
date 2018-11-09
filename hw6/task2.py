from sys import exit
inp = input ()
msk = input ()
if len (msk) > len (inp):
    print (-1)
    exit()
curr_si = 0
found = False
allat = True
atmove = 0
for i in msk:
    if i != "@":
        allat = False
        break
if not allat:
    while msk[0] == "@":
        atmove += 1
        msk = msk[1:]

while (not found) and (len (msk) + curr_si <= len (inp)) and (curr_si != -1) and not allat:   #TODO: if @ is first

    lkup = inp.find (msk.split("@")[0], curr_si + 1)
    if (lkup == -1) or (len (msk) + curr_si >  len(inp)):
        curr_si = -1
        break
    found = True
    for i in range (len(msk)):
        if (inp[lkup + i] != msk[i]) and (msk[i] != "@"):
            found = False
    curr_si = lkup
if curr_si != -1:
    curr_si -= atmove
print (curr_si)
