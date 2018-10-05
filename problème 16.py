# propject Euler Problem 16

def somme_chiffres(k,n):
    A=str(k**n)
    a=0
    for i in range (len(A)):
        a=a+int(A[i])
    return(a)


assert somme_chiffres(2,1000) == 1366
print(somme_chiffres(2,1000))


    
