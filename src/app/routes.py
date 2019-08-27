from flask import render_template, request, redirect, url_for, flash, jsonify  # For flask implementation
from bson import ObjectId, json_util # For ObjectId to work
# from pymongo import MongoClient
import json
from app.forms import LoginForm
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

import os

import app.app as app2
app = app2.app

title = "ANOIA - Makerspace Inventory System"
heading = "Scrap wood inventory (demo implementation)"

try:
    if (os.environ['DEBUG']):
        app.config["MONGO_URI"] = "mongodb://"+os.environ['DBUSERNAME']+":"+os.environ['DBUSERPW']+"@localhost:27017/test?authSource=admin"
except:
    app.config["MONGO_URI"] = "mongodb://"+os.environ['DBUSERNAME']+":"+os.environ['DBUSERPW']+"@mongo:27017/test?authSource=admin"
mongo = PyMongo(app)  # Select the database
db = mongo.db
todos = db.todos  # Select the collection name
users = db.users


def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        users.insert({ "name":form.username.data, "pwdhash":generate_password_hash(form.password.data)})  
        return redirect('/')
    user_l = users.find()
    return render_template('login.html', h="Login Page", form=form, users=user_l)


@app.route("/list")  
def lists ():  
    # Display the all Tasks
    todos_l = todos.find()  
    a1="active"  
    return render_template('index.html',a1=a1,todos=todos_l,t=title, h=heading)


@app.route("/")
def welcome():
    # redirect to first type of list
    return redirect("/type/material")


@app.route("/type/<string:itype>")
def tasks (itype):
    # Display the materials list
    todos_l = todos.find({"type":itype})
    a2="active"
    dummy = {}
    template_name = itype + ".html"
    return render_template(template_name, a2="active", todos=todos_l, t=title, h=heading, type=itype, sample=todos_l[0])


@app.route("/done")  
def done ():  
    # Done-or-not ICON
    onj_id = request.values.get("_id")
    task = todos.find({"_id": ObjectId(onj_id)})
    if task[0]["done"] == "yes":
        todos.update({"_id": ObjectId(onj_id)}, {"$set": {"done": "no"}})
    else:  
        todos.update({"_id": ObjectId(onj_id)}, {"$set": {"done": "yes"}})
    redir=redirect_url()
    return redirect(redir)  


@app.route("/action/material", methods=['POST'])
def action_mat ():
    # Adding a Task
    desc = request.values.get("desc")
    length = request.values.get("length")
    width = request.values.get("width")
    thick = request.values.get("thickness")
    mat = request.values.get("material")
    comment = request.values.get("comments")
    todos.insert({"desc":desc, "length":length, "width":width, "thickness":thick, "material":mat, "comments":comment, "status":"in Stock", "type":"material"})
    return redirect("/type/material")

@app.route("/action/manual", methods=['POST'])
def action_man ():
    # Adding a Task
    desc = request.values.get("desc")
    materials = request.values.get("materials")
    tags = request.values.get("tags")
    danger = request.values.get("danger")
    location = request.values.get("loacation")
    comment = request.values.get("comments")
    todos.insert({"desc":desc, "materials":materials, "tags":tags, "danger":danger, "locations":location, "comments":comment, "status":"available", "type":"manual"})
    return redirect("/type/manual")

@app.route("/remove")  
def remove ():  
    # Deleting a Task with various references
    key=request.values.get("_id")  
    todos.remove({"_id": ObjectId(key)})
    return redirect("/")  


@app.route("/update")  
def update ():  
    id = request.values.get("_id")
    task = todos.find({"_id": ObjectId(id)})
    return render_template('update.html', tasks=task, h=heading, t=title)


@app.route("/action3", methods=['POST'])  
def action3():
    # Updating a Task with various references
    name = request.values.get("name")
    desc = request.values.get("desc")
    date = request.values.get("date")
    pr = request.values.get("pr")
    id = request.values.get("_id")
    todos.update({"_id": ObjectId(id)}, {'$set': {"name": name, "desc": desc, "date": date, "pr": pr}})
    return redirect("/")


@app.route('/getdetail', methods=['POST'])
def get_detail():
    print('request for id ' + request.form['id'])
    task = todos.find({"_id": ObjectId(request.form['id'])})
    print('sending object ')
    entry = task[0]
    entry['ID'] = str(task[0]['_id'])[0:5]
    #entry.pop('_id', None)
    print(entry)
    # serialize with json_util (which understands ObjectID), the de-serialize with default json
    # flask will then re-serialize with flask.jsonify (to add response header)
    return json.loads(json_util.dumps(entry))


@app.route("/search", methods=['GET'])  
def search():  
    # Searching a Task with various references
    key = request.values.get("key")
    refer = request.values.get("refer")
    if key == "_id":
        todos_l = todos.find({refer: ObjectId(key)})
    else:  
        todos_l = todos.find({refer: key})
    return render_template('searchlist.html', todos=todos_l, t=title, h=heading)
