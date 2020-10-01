#Exercice Syracuse :

def syracuse(n):
    if n == 1:
        return n
    elif n % 2 == 0:
        return str(n) + ' ' + str(syracuse(n // 2))
    else:
        return syracuse(n * 3 + 1)

print(syracuse(6))        
    
#Exercice Turtle :

from turtle import *

ang = 40

def trace(n,l):
    
    if n == 0 :
        return None
    else :
        forward(l)
        left(ang)
        trace(n-1,0.7*l)
        right(2*ang)
        trace(n-1,0.7*l)
        left(ang)
        forward(-l)

        
penup()        
goto(0,-80)
pendown()
left(90)
speed(0)

trace(5,100)