#Exercice Syracuse :

def syracuse(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        return str(n) + ' ' + str(syracuse(n // 2))
    else:
        return syracuse(n * 3 + 1)

print(syracuse(14))        
    
#Exercice Turtle :

from turtle import *

def recu(t):
    for i in range(4):
        forward(t)
        left(90)
    penup()
    forward(t/2)
    left(45)
    pendown()
    recu(t/2**0.5)
    
penup()
pendown()
recu(200)


    