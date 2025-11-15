from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Storage import Storage
from Ausgaben import AusgabenDTO

### Make Login and then ceck if for user there is a database or create new one
app = Flask(__name__)
testStorage = Storage("test")  # Beispiel für einen Benutzernamen
testStorage.createTables()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-expenses.html', methods=['GET'])
def view_expenses():
    # 1. Filter-Daten aus der URL lesen (request.args)
    # .get() gibt None zurück, falls der Parameter fehlt (z.B. beim ersten Laden)
    filter_label = request.args.get('category')
    filter_month = request.args.get('month')
    expenses = testStorage.getAllFromSQL(filter_label=filter_label, filter_month=filter_month)
    return render_template('view-expenses.html', expenses=expenses)  # An das Template übergeben

@app.route('/add-expenses.html', methods=['GET','POST'])
def add_expenses():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = datetime.strptime(request.form['date'], '%d.%m.%Y')
        label = request.form['label']   
        testStorage.insertAusgabeToSQL(AusgabenDTO(None, amount, description, date.strftime('%d.%m.%Y'), datetime.now().strftime('%d.%m.%Y %h:%m:%s'), label))
        
    return render_template('add-expenses.html')

if __name__ == '__main__':
    app.run(debug=True) 
