from flask import Flask,request
from flask.json import jsonify
from app import db
import uuid

class User:
    def signup(self):
        user = {
            "_id":uuid.uuid4().hex(),
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password'),


        }
        db.users.insert_one(user)
        return jsonify(user), 200