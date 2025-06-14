from datetime import datetime

class Ausgaben:
    def __init__(self, betrag, grund, waehrung = "EUR", jahr = datetime.now().year, monat = datetime.now().month, tag = datetime.now().day, stunde = datetime.now().hour):
        self.betrag = betrag
        self.grund = grund
        self.waehrung = waehrung

        ##Datetime
        self.jahr = jahr
        self.monat = monat
        self.tag = tag
        self.stunde = stunde
       
        
    
    def __str__(self):
        return f"[{self.jahr}-{self.monat}-{self.tag} | {self.stunde} Uhr] {self.grund}: {self.betrag:.2f} {self.waehrung}"
