class vector:
    
    def __init__(self, *args):
        self.val = []
        args = list (*args)
        for i in args:
            self.val.append(i)

    def __add__(self, *args):
        args = list (*args)
        sm = []
        sm = self.val.copy()
        for i in range(len(args)):
            sm[i] += args[i]
        ret = vector(sm)
        return ret

    def __radd__(self, *args):
        args = list (*args)
        sm = []
        sm = self.val.copy()
        for i in range(len(args)):
            sm[i] += args[i]
        ret = vector(sm)
        return ret

    def __iter__(self):
        for i in self.val:
            yield i

    def __str__(self):
        st = ""
        for i in self.val:
            st += str(i) + ":"
        st = st[:-1]
        st += " "
        return st
