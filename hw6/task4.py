from collections import Counter
inp = [0, 0]
inp[0] = input ()
inp[1] = input ()
inp[0] = inp[0].lower ()
inp[1] = inp[1].lower ()
excl = [0, 0]
colons = [0, 0]
ques = [0, 0]
points = [0, 0]
pp = [0, 0]
ps = [0, 0]

for j in range (2):
    points[j] = inp[j].count('.')
    ques[j] = inp[j].count('?')
    excl[j] = inp[j].count('!')
    colons[j] = inp[j].count(',')
    pp[j] = inp[j].count(':')
    ps[j] = inp[j].count(';')

for i in range (2):
    inp[i] = inp[i].replace("!", " ")
    inp[i] = inp[i].replace(":", " ")
    inp[i] = inp[i].replace(";", " ")
    inp[i] = inp[i].replace(".", " ")
    inp[i] = inp[i].replace(",", " ")
    inp[i] = inp[i].replace("?", " ")
spl = [inp[0].split(' '), inp[1].split(' ')]
var = (excl[0] == excl[1]) and (colons[0] == colons[1]) and (ques[0] == ques[1]) and (points[0] == points[1]) and (pp[0] == pp[1]) and (ps[0] == ps[1])

#for i in range (2):
#    if var:
#        for j in spl[i]:
#            if not (j in spl[(i+1)%2]):
#                var = False
#                break
if var:
    var = Counter(spl[0]) == Counter(spl[1])
print (var)
