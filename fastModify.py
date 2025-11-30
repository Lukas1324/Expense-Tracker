from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO
from dataSetFile import dataSet

testStorage = Storage("test")  # Beispiel für einen Benutzernamen
testStorage.createTables()  # Tabellen erstellen, falls sie nicht existieren
#testStorage.insertAllToSQL(dataSet)  # Daten aus dem dataSetFile einfügen

testStorage.dbToCSV('db_export.csv')  # Exportiere die Datenbank in eine CSV-Datei
print("Datenbank wurde in 'db_export.csv' exportiert.")



