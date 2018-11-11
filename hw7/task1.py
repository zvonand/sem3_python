curr = input ()
dictn = {}
only = True
mx = 0

while curr:
    lst = curr.split ()
    for i in lst:
        if i in dictn:
            dictn[i] += 1
        else:
            dictn[i] = 1
    curr = input ()
outstr = ""

for key, val in dictn.items():
    if val > mx:
        mx = val
        outstr = key
        only = True
    elif val == mx:
        only = False
if only:
    print (outstr)
else:
    print ("---")

