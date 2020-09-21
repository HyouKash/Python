#EX 1 : Eleve
class Eleve:
    def __init__(self, nom, classe, note):
        self.nom = nom
        self.classe = classe
        self.note = note

    def affiche(self):
        print("Eleve :", self.nom, ",", self.classe, ",", self.note)


def compare(eleve1, eleve2):
    if eleve1.note > eleve2.note:
        return eleve1.nom
    else:
        return eleve2.nom


A = Eleve("George", "TG9", 14)
B = Eleve("Diego", "TG9", 13)


# EX 2: TriangleRect

class TriangleRect:
    def __init__(self, cote1, cote2, hypothenuse):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenuse = hypothenuse


# EX 3 : Chrono

class Chrono:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def affiches(self):
        print(self.heures, "heures,", self.minutes, "minutes,", self.secondes, "secondes")

    def avance(self, s):
        self.secondes += s
        if self.secondes > 59:
            self.minutes += self.secondes // 60
            self.secondes = self.secondes % 60
            if self.minutes > 59:
                self.heures += self.minutes // 60
                self.minutes = self.minutes % 60
                return self.heures, self.minutes, self.secondes
            else:
                return self.heures, self.minutes, self.secondes
        else:
            return self.heures, self.minutes, self.secondes


A = Chrono(4, 23, 55)