from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://zhkwgjdxcmdlgi:6c45f70d358e5cdf7a4a325d3b2c7f35ba306685c33890351a825f34a33971c3@ec2-184-73-25-2.compute-1.amazonaws.com:5432/ddknmu3tmglcmt"
db = SQLAlchemy(app)
connection = psycopg2.connect(database="tiendas_api", user="postgres", password="12345")


class Tiendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    direccion = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(80))
    phone = db.Column(db.Integer())

    def __init__(self, name, direccion, city, state, phone):
        self.name = name
        self.direccion = direccion
        self.city = city
        self.state = state
        self.phone = phone

  
@app.route('/')
def home():
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM public.tiendas')
    data = cursor.fetchall()
    return render_template("index.html", tiendas = data)


@app.route("/Chihuahua", methods = ['GET'])
def datoChi():
    cursor2=connection.cursor()
    cursor2.execute("select * from public.tiendas where state = 'Chihuahua'")
    data = cursor2.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/Sonora", methods = ['GET'])
def datoSono():
    cursor3=connection.cursor()
    cursor3.execute("select * from public.tiendas where state = 'Sonora'")
    data = cursor3.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/Tabasco", methods = ['GET'])
def datoTabas():
    cursor4=connection.cursor()
    cursor4.execute("select * from public.tiendas where state = 'Tabasco'")
    data = cursor4.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/NuevoLeon", methods = ['GET'])
def datoNuevo():
    cursor5=connection.cursor()
    cursor5.execute("select * from public.tiendas where state = 'Nuevo Leon'")
    data = cursor5.fetchall()
    return render_template("index.html", tiendas = data)


if __name__ == '__main__':
    app.run(debug=True)

 
