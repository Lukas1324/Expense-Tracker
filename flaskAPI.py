from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

#class Message(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #amount = db.Column(db.Float, nullable=False)
    #content = db.Column(db.String(200), nullable=False)
    # = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

@app.route('/')
def home():
    return "<h2>Hello, Flask!</h2>"

if __name__ == '__main__':
    app.run(debug=True) 
