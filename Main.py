from Calculation import Calc
from Storage import Storage
from Ausgaben import Ausgaben

mein_calc = Calc()
mein_storage = Storage()
ersteAusagbe = Ausgaben(10.0,"Lebensmittel")
zweiteAusagbe = Ausgaben(10.0,"Lebensmittel")
mein_storage.appendAusgaben(ersteAusagbe)
