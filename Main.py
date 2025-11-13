from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO

### Make Login and then ceck if for user there is a database or create new one
app = Flask(__name__)
testStorage = Storage("test")  # Beispiel für einen Benutzernamen


####Aufgaben fürs nächste mal:
# Die Datenbank mit viewexpenses und addexpenses verbinden

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-expenses.html', methods=['GET'])
def view_expenses():

    expenses = testStorage.getAllFromSQL()
    print(expenses) # Alle Einträge holen
    return render_template('view-expenses.html', expenses=expenses)  # An das Template übergeben

@app.route('/add-expenses.html', methods=['GET','POST'])
def add_expenses():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        
        # Erstelle eine neue Ausgabe und füge sie zur Liste hinzu
        ausgabe = AusgabenDTO(None, amount, description, date, datetime.now())
        testStorage.appendAusgaben(ausgabe)
        testStorage.insertToSQL()  # Speichere alle in der Liste zur Datenbank
        testStorage.clearLocalAusgaben()  # Leere die Liste
        
        return redirect(url_for('view_expenses'))
    
    return render_template('add-expenses.html')

if __name__ == '__main__':
    app.run(debug=True)
