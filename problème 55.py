def test_palindrome(n):
    chaine = str(n)
    for i in range (int(len(chaine)/2)):
        if chaine[i]!=chaine[len(chaine)-1-i]:
            return(False)
    return(True)


def inversion_nombre(n):
    chaine = str(n)
    chaine = chaine[::-1] # inverse les éléments de la chaîne
    k = int(chaine)
    return(k)



def test_lychrel(n,k):  #k est le nombre d'itérations, n le chiffre maximal à tester
    compte = 0
    i=0
    L=[]
    
    while i<=n:
        j=0
        m=i
        
        while j<=k:        
            if test_palindrome(m) == False :
                m=m+inversion_nombre(m)
                j=j+1
            else :
                break

        if j==k+1:
            compte = compte + 1
            L.append(i)
        i=i+1

    return(compte,L)


print(test_lychrel(10000,50))