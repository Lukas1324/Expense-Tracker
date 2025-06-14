from datetime import datetime

class Ausgaben:
    def __init__(self, betrag, grund, waehrung = "EUR", zeit = datetime.now().strftime("%d-%m-%Y | %H-%M")):
        self.betrag = betrag
        self.grund = grund
        self.waehrung = waehrung

        ##Datetime
        self.zeit = zeit
       
        
    
    def __str__(self):
        return f"{self.zeit} Uhr - {self.grund}: {self.betrag:.2f} {self.waehrung}"
