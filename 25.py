class Car:
    def __init__(self):
        self.name = "Тойота"

toyota = Car()
toyota_chr = toyota
print(toyota is toyota_chr)

nissan = Car()
print(toyota is nissan)
