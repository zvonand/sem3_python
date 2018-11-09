a = eval (input ())
a = list(a)

def find_max (lst):
    if lst:
        val = lst[0]
        for i in lst:
            if i > val:
                val = i
        return val
    else:
        return "NO"

max = find_max (a)

while max in a:
    a.remove(max)

print (find_max (a))
