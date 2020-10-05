def hanoi(n, A,B,C):
    return n * hanoi(n-1, A, B,C)

print(hanoi(4, A,B,C))