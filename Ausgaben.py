from datetime import datetime

class Ausgaben:
    def __init__(self, betrag, grund, waehrung = "EUR", datumUhrzeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.betrag = betrag
        self.grund = grund
        self.waehrung = waehrung
        self.datumUhrzeit = datumUhrzeit
       
        
    
    def __str__(self):
        return f"[{self.datumUhrzeit}] {self.grund}: {self.betrag:.2f} {self.waehrung}"
