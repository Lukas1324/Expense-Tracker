from flask import Flask, render_template, redirect, url_for, request, send_file
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
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        label = request.form['label']   
        testStorage.insertAusgabeToSQL(AusgabenDTO(None, amount, description, date.strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d | %H:%M:%S'), label))
        
    return render_template('add-expenses.html')

@app.route('/export-csv')
def export_csv():
    fileName = "db_export.csv"
    path = r'C:\Users\lukiz\VS Programme\Just For Fun\Expense-Tracker\db_export.csv'
    testStorage.dbToCSV(fileName)  # Exportiere die Datenbank in eine CSV-Datei
    return send_file(path, as_attachment=True, download_name=fileName)


if __name__ == '__main__':
    app.run(debug=True) 
