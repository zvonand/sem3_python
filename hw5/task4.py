def LookSay ():
    result = [1]
    yield 1
    while 1:
        curr = result[0]
        next = []
        count = 1
        for i in result[1:] + [-1]:
            if i != curr:
                yield count
                yield curr
                next.extend([count, curr])
                count = 1
                curr = i
            else:
                count += 1
        result = next

#for i,l in enumerate(LookSay()):
#    print(f"{i}: {l}")
#    if i>50:
#        break
