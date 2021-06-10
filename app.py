from flask import Flask,render_template
import pymongo
from pymongo import database

app = Flask(__name__)


#database
client = pymongo.MongoClient("mongodb://13.233.190.38:27017/")
db = client['database']
col = db['user']



#Routes
from user import routes

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")