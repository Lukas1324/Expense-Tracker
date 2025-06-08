class Ausgaben:
    def __init__(self, betrag, grund, waehrung = "EUR"):
        self.betrag = betrag
        self.grund = grund
        self.waehrung = waehrung

    def printBetrag(self):
        print(f'Es hat {self.betrag} {self.waehrung} gekostet')

    def printAusgabe(self):
        print(f'Es hat {self.betrag} {self.waehrung} gekostet, der Grund war: {self.grund}')
