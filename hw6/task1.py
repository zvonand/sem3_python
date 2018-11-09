inp = input ()
a = inp.split ()
max = 0
not_met = True
while inp:
    for i in a:
        num = True
        sign = 1
        if i[0] == "-":
            sign = -1
            i = i[1:]
        if i.isdecimal ():
            i = int (i)
            if not_met:
                max = sign * i
                not_met = False
            elif sign * i > max:
                max = sign * i

    inp = input ()
    a = inp.split ()

print (max)
