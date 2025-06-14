from Calculation import Calc
from Storage import Storage
from Ausgaben import Ausgaben







mein_storage = Storage()
mein_calc = Calc(mein_storage)

ausgabe = Ausgaben(9.4, "Pizza")
mein_storage.appendAusgaben(ausgabe)

mein_storage.getAllFromSQL()
mein_storage.printStorage()
mein_storage.sonderManipulationSQL()
print(mein_calc.calcTotal())
mein_storage.closePipeline()

