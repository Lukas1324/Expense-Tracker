from Storage import Storage
from Ausgaben import Ausgaben
from datetime import datetime

class Calc:
    def __init__(self, storage:Storage):
        self.storage = storage

    def calcTotal(self):
        total = 0
        for ausgabe in self.storage.ausgaben:
            total += ausgabe.betrag
        return round(total, 2)
    
    def calcTotalThisMonth(self):
        total = 0
        for ausgabe in self.storage.ausgaben:
            if(ausgabe.monat == datetime.now().month and ausgabe.jahr == datetime.now().year):
                total += ausgabe.betrag
        return round(total, 2)
      

    def calcTotalThisYear(self):
        total = 0
        for ausgabe in self.storage.ausgaben:
            if(ausgabe.jahr == datetime.now().year):
                total += ausgabe.betrag
        return round(total, 2)






"""""
    def calcTotalFromCustom(self, year = None, month = None, day = None):
        if(day == None):
            if(month == None):
                if(year == None):
                    self.calcTotal
                else:
                    pass
            else:
                pass
        else:
            pass 
        return
"""