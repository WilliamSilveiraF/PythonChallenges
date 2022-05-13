class Ticket:
    def __init__(self):
        self.value = 10.0

class VIP(Ticket):
    pass
    def __init__(self):
        Ticket.__init__(self)
        self.additionalValue = 2.10

    def getValue(self):
        return self.value + self.additionalValue

class Normal(Ticket):
    pass
    def __init__(self):
        Ticket.__init__(self)

    def getValue(self):
        return self.value

class CamaroteInferior(VIP):
    pass
    def __init__(self, local):
        VIP.__init__(self)
        self.local = local

    def getLocal(self):
        return self.local

class CamaroteSuperior(VIP):
    pass
    def __init__(self, local):
        VIP.__init__(self)
        self.local = local
        self.additionalSuperiorValue = 50.0

    def getLocal(self):
        return self.local
    def getValue(self):
        return self.value + self.additionalValue + self.additionalSuperiorValue

while True:
    try:
        tp = int(input('[1] Normal Ticket\n[2] VIP Ticket\nChoice: '))
        if tp == 1:
            print('- Ingresso Normal')
            ticket = Normal()
            print(f'Total: {ticket.getValue()}')
        elif tp == 2:
            print('- Ingresso VIP')
            tpVIP = int(input('[1] Camarote Superior\n[2] Camarote Inferior\nChoice: '))
            if tpVIP == 1:
                camarote = CamaroteSuperior('H3')
            elif tpVIP == 2:
                camarote = CamaroteInferior('H3')
            print(f'Total: {camarote.getValue()}')
    except EOFError:
        break
upperSpecialTicker = CamaroteSuperior('Camarote Superior')

print(upperSpecialTicker.getLocal())