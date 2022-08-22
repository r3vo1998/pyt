class Horse():
    def __init__(self, n, v, o):
        self.name = n
        self.vozrast = v
        self.owner = o

class Rider():
    def __init__(self, name):
        self.name = name

piter = Rider("Питер Пен")
tema = Horse("Тим", "20", piter)
print(tema.owner.name)
