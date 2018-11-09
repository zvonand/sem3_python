num = eval(input())
pow10 = 0
while 10 ** pow10 <= num:
    pow10 += 1

pow10 -= 1
pal = 1
if num >= 10 and num%10 == 0:
    print ("NO")
else:
    while pow10 >= 0:
        a = num // (10 ** pow10)
        b = num % 10
        pal = a == b
        if pal == 0:
            break
        else:
            pal = pal // pal
            num = num % (10 ** pow10)
            num = num // 10
            pow10 -= 2
    if pal:
        print ("YES")
    else:
        print("NO")
