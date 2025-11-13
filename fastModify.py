from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO
from dataSetFile import dataSet

testStorage = Storage("test")  # Beispiel für einen Benutzernamen
testStorage.createTables()  # Tabellen erstellen, falls sie nicht existieren
#testStorage.insertAllToSQL(dataSet)  # Daten aus dem dataSetFile einfügen



