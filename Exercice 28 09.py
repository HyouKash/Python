#Ex récursivité : 

def facto(n):
    if n == 0 :
        return 1
    else : 
        return n * facto(n-1)
    
#En impératif :
    
def facto_normale(n):
    for k in range(1,n):
        n *= k
    return n

def factor(n):
    res = n
    n = n - 1
    while n != 0:
        res = res * n
        n = n - 1
    return res

#Récursivité puissance :

def puissance(x,n):
    if n == 0:
        return 1
    else:
        return x*puissance(x,n-1)

#Récursivité boucle :
    
def boucle(i,k):
    if i == k:
        return k
    else:
        return str(i) + ' ' + str(boucle(i+1,k))
