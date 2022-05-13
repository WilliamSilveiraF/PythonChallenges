class Worker:
    pass
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getID(self):
        return self.id
    def getName(self):
        return self.name

class Technical(Worker):
    pass
    def __init__(self, id, name, salaryBonus):
        Worker.__init__(self, id, name)
        self.salaryBonus = salaryBonus

class Adm(Worker):
    pass
    def __init__(self, id, name, turn, nightAdditional):
        Worker.__init__(self, id, name)
        self.turn = turn
        self.nightAdditional = nightAdditional


carlos = Technical('123123', 'Carlos', 100000)

lucas = Adm('847329472', 'Lucas', 'Noite', 100)

print(f'\nName: {carlos.getName()}\nId: {carlos.getID()}')
print(f'\nName: {lucas.getName()}\nId: {lucas.getID()}')