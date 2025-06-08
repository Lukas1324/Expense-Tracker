from Storage import Storage
from Ausgaben import Ausgaben

class Calc:
    def __init__(self, storage:Storage):
        self.storage = storage

    def calcTotal(self, ausgaben: list[Ausgaben]):
        total = 0
        for ausgabe in ausgaben:
            total += ausgabe.betrag
        return total
        