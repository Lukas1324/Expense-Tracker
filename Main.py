from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-expenses.html', methods=['GET'])
def view_expenses():
    expenses = Message.query.order_by(Message.date.desc()).all()  # Alle Einträge holen
    return render_template('view-expenses.html', expenses=expenses)  # An das Template übergeben

@app.route('/add-expenses.html', methods=['GET','POST'])
def add_expenses():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        db.session.add(Message(amount=amount, content=description, date=date))
        db.session.commit()
        201
    return render_template('add-expenses.html')

if __name__ == '__main__':
    app.run(debug=True) 
