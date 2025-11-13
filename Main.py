from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO

### Make Login and then ceck if for user there is a database or create new one
app = Flask(__name__)
testStorage = Storage("test")  # Beispiel für einen Benutzernamen


####Läd so lange wsl weil die Daten erst von SQL gezogen werden müssen. Die sollten direkt geladen werden, bevor man auf die Seite geht

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-expenses.html', methods=['GET'])
def view_expenses():

    expenses = testStorage.getAllFromSQL()
    return render_template('view-expenses.html', expenses=expenses)  # An das Template übergeben

@app.route('/add-expenses.html', methods=['GET','POST'])
def add_expenses():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        testStorage.insertAusgabeToSQL(AusgabenDTO(None, amount, description, date.strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
    return render_template('add-expenses.html')

if __name__ == '__main__':
    app.run(debug=True) 
