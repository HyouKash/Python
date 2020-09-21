class Point:
    def __init__(self, nom, x, y):
        self.x = x
        self.y = y
        self.nom = nom

    def distance(self):
        result = (self.x ** 2 + self.y ** 2)
        result = result ** 0.5
        return result

    def presenter(self):
        print(self.nom, ":", self.x, ",", self.y)


A = Point("A", 4, 6)
B = Point("B", 5, 8)
C = Point("C", 10, 9)


def dist(A, B):
    return ((B.x - A.x) ** 2 + (B.y - A.x)) ** 2


def test_triangle(A, B, C):
    if dist(A, B) ** 2 == dist(A, C) ** 2 + dist(C, B) ** 2:
        return True
    else:
        return False

print(test_triangle(A,B,C))