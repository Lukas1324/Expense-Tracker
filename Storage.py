from Ausgaben import AusgabenDTO
import sqlite3
from Tables import tabellen
import pandas as pd




class Storage:
    def __init__(self, name):
        self.ausgaben: list[AusgabenDTO] = []
        self.conn = sqlite3.connect("DB_Ausgaben_" + name + ".db", check_same_thread=False)
        self.cursor = self.conn.cursor()


    ###SQL------------------------------------------------------------------------------------------------------------------------------------
    def getAllFromSQL(self, filter_label = None, filter_month = None):
        self.clearLocalAusgaben()
        where_clauses = []
        parameters = []
        baseQuery = "Select id, amount, content, date, created_at, label From ausgaben "

        if filter_label:
            where_clauses.append("label = ?")
            parameters.append(filter_label)

        if filter_month:
            where_clauses.append("strftime('%Y-%m', date) = ?")
            parameters.append(filter_month)  # Ensure month is two digits



        if len(where_clauses) > 0:
            baseQuery += "WHERE " + " AND ".join(where_clauses)




        self.cursor.execute(baseQuery, tuple(parameters))
        for id, amount, content, date, created_at, label in self.cursor.fetchall():
            self.appendAusgaben(AusgabenDTO(id, amount, content, date, created_at, label))
        return self.ausgaben
          
    def insertAusgabeToSQL(self, ausgabe: AusgabenDTO):
        self.cursor.execute("INSERT INTO ausgaben (amount, content, date, created_at, label) VALUES (?, ?, ?, ?, ?)", (ausgabe.amount, ausgabe.content, ausgabe.date, ausgabe.created_at, ausgabe.label))
        self.conn.commit()

    def insertAllToSQL(self, listAusgaben: list[AusgabenDTO]):
        for ausgabe in listAusgaben:
            self.insertAusgabeToSQL(ausgabe)

    def dbToCSV(self, filename):
        df = pd.read_sql_query("SELECT * FROM ausgaben", self.conn)
        df.to_csv(filename, index=False, encoding='utf-8', sep=';')


    def closePipeline(self):
        self.conn.close()

    def deleteLastAusgabeInSQL(self):
        self.cursor.execute("DELETE From Ausgaben where id = (Select id FROM ausgaben Order By id DESC Limit 1)")
        self.conn.commit()

    def deleteAllInSQL(self):
        self.cursor.execute("DELETE FROM ausgaben")
        self.conn.commit()

    def sonderManipulationSQL(self, textManipulation):
        self.cursor.execute(textManipulation)
        self.conn.commit()

    def createTables(self):
        for table in tabellen:
            self.cursor.execute(table)
        self.conn.commit()


######Old Code

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




    