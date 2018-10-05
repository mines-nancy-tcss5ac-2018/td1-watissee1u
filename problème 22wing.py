fichier = open("p022_names.txt","r")

texte = fichier.read()


def tri(txt):
    L=txt.split(',')
    L.sort()
    return(L)


def score(chaine):
    s=0
    for i in range(1,len(chaine)-1):
        s=s+ord(chaine[i])-(ord('A')-1)
    return(s)



def total_score(L):
    somme=0
    for i in range(len(L)):
        somme=somme+((i+1)*score(L[i]))
    return(somme)


print(total_score(tri(texte)))


