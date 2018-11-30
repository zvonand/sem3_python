class LetterAttr:
    var = {} 
    def __init__ (self):
        self.var = {}

    def __getattr__ (self, name):
        if name in self.var.keys():
            return self.var[name]
        else:
            self.var[name] = name
            return name

    def __setattr__ (self, name, value):
        resu = ""
        for i in value:
            if i in name:
                resu += i
        self.var[name] = resu
