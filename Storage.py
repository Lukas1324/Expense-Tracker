from Ausgaben import Ausgaben
import sqlite3




class Storage:
    def __init__(self):
        self.ausgaben: list[Ausgaben] = []
        self.conn = sqlite3.connect("DB_Ausgaben.db")
        self.cursor = self.conn.cursor()


    ###SQL------------------------------------------------------------------------------------------------------------------------------------
    def getAllFromSQL(self):
        self.cursor.execute("Select betrag, grund, datetime, waehrung  From ausgaben")
        for betrag, grund, zeit, waehrung in self.cursor.fetchall():
            self.appendAusgaben(Ausgaben(betrag, grund, waehrung, zeit))

    def insertToSQL(self):
        for ausgabe in self.ausgaben:
            self.cursor.execute("INSERT INTO ausgaben (betrag, grund, datetime, waehrung) VALUES (?, ?)", (ausgabe.betrag, ausgabe.grund, ausgabe.datumUhrzeit, ausgabe.waehrung))
        
        self.conn.commit()  

    def closePipeline(self):
        self.conn.close()

    def deleteLastAusgabeInSQL(self):
        self.cursor.execute("Select * From ausgaben Order By id DESC Limit 1")
        delZeile = self.cursor.fetchone()[0]
        print(delZeile)

        self.cursor.execute("DELETE FROM ausgaben Where id = ?", (delZeile,))
        self.conn.commit()

    def sonderManipulationSQL(self):
        pass



    ###Lokale Liste---------------------------------------------------------------------------------------------------------------------------------------------       

    def clearLocalAusgaben(self):
        self.ausgaben = []

    def appendAusgaben(self, ausgabe):
        if(isinstance(ausgabe, Ausgaben)):
            self.ausgaben.append(ausgabe)
        else:
            print("Ist keine Ausgabe")


    def printStorage(self):
        for ausgabe in self.ausgaben:
            print(ausgabe.__str__())

    