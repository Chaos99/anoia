
from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)


title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

#client = MongoClient("mongodb://root:123456@127.0.0.1:27017") #host uri
#db = client.test #Select the database
#todos = db.user #Select the collection name

def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


@app.route("/")
@app.route("/uncompleted")

def tasks ():
    #Display the Uncompleted Tasks
    #todos_l = todos.find({"done":"no"})
    a2="active"
    dummy = {}
    return render_template('index.html',a2="active", todos=dummy, t=title,h=heading)


if __name__ == "__main__":
    app.run()