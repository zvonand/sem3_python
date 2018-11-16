def toint (func):
    def returnable (*t):
        t = list (t)
        for i in range (len(t)):
            if type (t[i]) == float:
                t[i] = int (t[i])
        t = tuple (t)
        ret = func (*t)
        if type (ret) == float:
            ret = int (ret)
        return ret
    return returnable
