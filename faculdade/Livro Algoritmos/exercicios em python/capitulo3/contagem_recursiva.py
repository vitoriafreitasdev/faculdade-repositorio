def regressiva(i):
    print (i)
    if i >= 10:
        return #caso base
    else:    
        regressiva(i+1) #caso recursivo 
    
regressiva(1)