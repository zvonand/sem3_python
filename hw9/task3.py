class Dots:
    bounds = []
    
    def __init__ (self, a, b):
        self.bounds = [a, b]

    def __getitem__ (self, arg):
        if type(arg) == int:
            dif = (self.bounds[1] - self.bounds[0]) / (arg - 1)
            ret = []
            for i in range (arg):
                ret.append (self.bounds[0] + i*dif)
            return ret
            
        else:
            
            start = arg.start
            stop = arg.stop
            step = arg.step
           
            if not step:
                dif = (self.bounds[1] - self.bounds[0]) / (stop - 1)
                return self.bounds[0] + start * dif
            else:
                if not start:
                    start = 0
                if not stop:
                    stop = step
                ret = []
                dif = (self.bounds[1] - self.bounds[0]) / (step - 1)
                for i in range (start, stop):
                    ret.append (self.bounds[0] + i * dif)
                return ret
