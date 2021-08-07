from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost/height_collector'

db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method != 'POST':
        return
    email = request.form["email_input"]
    if db.session.query(Data).filter(Data.email == email).count() != 0:
        return render_template('index.html',
                               text="Seems like we've got something from that email address already")
    height = request.form["height_input"]
    data = Data(email, height)
    db.session.add(data)
    db.session.commit()
    average_height = db.session.query(func.avg(Data.height)).scalar()
    average_height = round(average_height, 1)
    count = db.session.query(Data.height).count()
    #send_email(email, height, average_height, count)
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
