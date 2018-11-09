def squares (w, h, *par):
    mat = ["".ljust (h, ".") for _ in range (w)]
    #par = list(par)
    #par.reverse ()
    for rect in par:
        #X, Y, side, symb
        for wid in range (rect[0], rect[0] + rect[2]):
            mat[wid] = mat[wid][:rect[1]] + len(mat[wid][rect[1] : (rect[1] + rect[2])]) * rect[3] + mat[wid][(rect[1] + rect[2]):]



    for i in range (h):
        toprnt = ""
        for j in range (w):
            toprnt += mat[j][i]
        print (toprnt)

#squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))
#squares(14,14,(0,0,14,'#'), (7,7,3,'.'))
