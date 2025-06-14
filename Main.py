from Calculation import Calc
from Storage import Storage
from Ausgaben import Ausgaben

def userInput():
    inpPreis = float(input("Wie viel hat es gekostet: "))
    inpGrund = input("Was hast du gekauft: ")
    mein_storage.appendAusgaben(Ausgaben(inpPreis, inpGrund))
    

def userConsole():
    while True:
        
        eingabe = int(input(
            "\nWas magst du machen:\n"
            "\033[35mEine Ausgabe eintragen (1)\033[0m, Die kompletten Kosten anzeigen lassen (2), Die Ausgaben in die SQL Datei einführen (3),\n"
            "Alle Ausgaben von der SQL holen (4), Alle Ausgaben printen (5), Das Programm schließen (6)\n"
            ))


        print("")
        if(eingabe == 1):
            userInput()
        elif(eingabe == 2):
            print(mein_calc.calcTotal())
        elif(eingabe == 3):
            mein_storage.insertToSQL()
        elif(eingabe == 4):
            mein_storage.getAllFromSQL()
        elif(eingabe == 5):
            mein_storage.printStorage()
        elif(eingabe == 6):
            mein_storage.closePipeline()
            return "Programm beendet"


mein_storage = Storage()
mein_calc = Calc(mein_storage)
print(userConsole())


