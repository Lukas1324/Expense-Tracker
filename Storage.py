from Ausgaben import Ausgaben

class Storage:
    def __init__(self):
        self.ausgaben = []

    def appendAusgaben(self, ausgabe):
        print(type(ausgabe))
        if(isinstance(ausgabe, Ausgaben)):
            print("Ist Ausgaben")
            self.ausgaben.append(ausgabe)
        else:
            print("Ist keine Ausgabe")
