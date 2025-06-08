from Ausgaben import Ausgaben
import sqlite3




class Storage:
    def __init__(self):
        self.ausgaben: list[Ausgaben] = []
        self.conn = sqlite3.connect("DB_Ausgaben.db")
        self.cursor = self.conn.cursor()

    def appendAusgaben(self, ausgabe):
        print(type(ausgabe))
        if(isinstance(ausgabe, Ausgaben)):
            print("Ist Ausgaben")
            self.ausgaben.append(ausgabe)
        else:
            print("Ist keine Ausgabe")


    def getAllFromSQL(self):
        self.cursor.execute("Select betrag, grund From ausgaben")
        for betrag,grund in self.cursor.fetchall():
            self.appendAusgaben(Ausgaben(betrag, grund))

    def insertToSQL(self):
        for ausgabe in self.ausgaben:
            self.cursor.execute("INSERT INTO ausgaben (betrag, grund) VALUES (?, ?)", (ausgabe.betrag, ausgabe.grund))
        
        self.conn.commit()

    def printStorage(self):
        for ausgabe in self.ausgaben:
            ausgabe.printAusgabe()

    def closePipeline(self):
        self.conn.close()