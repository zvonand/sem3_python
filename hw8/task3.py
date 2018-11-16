class Stack:

    def __init__(self):
        self.stack = []

    def push (self, value):
        self.stack.append(value)

    def pop (self):
        return self.stack.pop(len (self.stack) - 1)

inp = input ()
inplst = inp.split()
stack = Stack ()
for inp in inplst:
    if inp[1:].isdigit() and inp[0] == '-':
        inp = -1 * eval (inp[1:])
    elif inp.isdigit():
        inp = eval (inp)
    if (type(inp) != int) and (inp != '+') and (inp != '-') and (inp != '*'):
        continue
    if type(inp) == int:
        stack.push(inp)
    else:
        a = stack.pop()
        b = stack.pop()
        if inp == '+':
            a = b + a
            stack.push (a)
        elif inp == '-':
            a = b - a
            stack.push (a)
        else:
            a = b * a
            stack.push (a)

print (stack.pop ())
