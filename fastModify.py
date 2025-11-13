from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO

testStorage = Storage("test")  # Beispiel für einen Benutzernamen
testStorage.createTables()  # Tabellen erstellen, falls sie nicht existieren

#testStorage.appendAusgaben(AusgabenDTO(None, 50.0, "Lebensmittel", datetime(2024, 6, 1), datetime.now()))
#testStorage.insertToSQL()  # Daten in die Datenbank einfügen

testStorage.printStorage()
for ausgabe in testStorage.getAllFromSQL():
    print(ausgabe.getContent()) # Alle Einträge holen

