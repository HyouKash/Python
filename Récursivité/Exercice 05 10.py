#Exercice Tour d'Hanoi

def hanoi(n, A,B,C):     
    if n == 1:
        print(A + " vers " + C)
    else :
        hanoi(n-1,A,C,B)
        print(A + " vers " + C)
        hanoi(n-1, B, A, C)

hanoi(5, "A","B","C")

