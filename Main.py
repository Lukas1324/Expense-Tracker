from Calculation import Calc
from Storage import Storage
from Ausgaben import Ausgaben







mein_storage = Storage()
mein_calc = Calc(mein_storage)
"""""
ersteAusagbe = Ausgaben(10.0,"Lebensmittel")
zweiteAusagbe = Ausgaben(15.2,"Wasser")
mein_storage.appendAusgaben(ersteAusagbe)
mein_storage.appendAusgaben(zweiteAusagbe)
mein_storage.deleteLastAusgabeInSQL()
mein_storage.deleteLastAusgabeInSQL()
"""

mein_storage.getAllFromSQL()
mein_storage.printStorage()
mein_storage.closePipeline()
