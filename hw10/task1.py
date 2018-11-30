class DivStr (str):
    
    def __floordiv__ (self, a):
        stri = self.__str__ ();
        length = len (stri) // a
        lst = []
        for i in range (a):
            lst.append (stri[:length])
            stri = stri[length:]

        return lst

    def __mod__ (self, a):
        stri = self.__str__ ();
        length = len (stri) // a
        for i in range (a):
            stri = stri[length:]
        return stri
