from Ausgaben import AusgabenDTO
import sqlite3
from Tables import tabellen




class Storage:
    def __init__(self, name):
        self.ausgaben: list[AusgabenDTO] = []
        self.conn = sqlite3.connect("DB_Ausgaben_" + name + ".db")
        self.cursor = self.conn.cursor()


    ###SQL------------------------------------------------------------------------------------------------------------------------------------
    def getAllFromSQL(self):
        self.cursor.execute("Select id, amount, content, date, created_at  From ausgaben")
        for id, amount, content, date, created_at in self.cursor.fetchall():
            self.appendAusgaben(AusgabenDTO(id, amount, content, date, created_at))
        return self.ausgaben
        

    def insertToSQL(self):
        for ausgabe in self.ausgaben:
            self.cursor.execute("INSERT INTO ausgaben (amount, content, date, created_at) VALUES (?, ?, ?, ?)", (ausgabe.amount, ausgabe.content, ausgabe.date, ausgabe.created_at))
        
        self.conn.commit()  

    def closePipeline(self):
        self.conn.close()

##### Ab hier funktioniert es nicht mehr, ist noch mit dem alten System
    def deleteLastAusgabeInSQL(self):
        self.cursor.execute("Select * From ausgaben Order By id DESC Limit 1")
        delZeile = self.cursor.fetchone()[0]
        print(delZeile)

        self.cursor.execute("DELETE FROM ausgaben Where id = ?", (delZeile,))
        self.conn.commit()

    def sonderManipulationSQL(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ausgaben (id INTEGER PRIMARY KEY AUTOINCREMENT, betrag REAL, grund TEXT, waehrung TEXT, zeit TEXT)")
        self.conn.commit()

    def createTables(self):
        for table in tabellen:
            self.cursor.execute(table)
        self.conn.commit()


    ###Lokale Liste---------------------------------------------------------------------------------------------------------------------------------------------       

    def clearLocalAusgaben(self):
        self.ausgaben = []

    def appendAusgaben(self, ausgabe):
        if(isinstance(ausgabe, AusgabenDTO)):
            self.ausgaben.append(ausgabe)
        else:
            print("Ist keine Ausgabe")


    def printStorage(self):
        for ausgabe in self.ausgaben:
            print(ausgabe.__str__())




    