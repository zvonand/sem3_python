frac = eval(input ())
num = frac[0]
den = frac[1]

intpart = num // den
frpart = num % den

def gcd (a, b):
    return abs(a) if b == 0 else gcd(b, a % b)

i = gcd (frpart, den)

frpart = frpart // i
den = den // i

if intpart and frpart:
    print (str(intpart) + " " + str(frpart) + "/" + str(den))
elif intpart and ~frpart:
    print (str(intpart))
elif ~intpart and frpart:
    print (str(frpart) + "/" + str(den))
