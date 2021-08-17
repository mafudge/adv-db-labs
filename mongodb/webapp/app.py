import logging
import json
import datetime
import pymongo
from flask import Flask, escape, request, render_template, redirect, url_for

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
myclient = pymongo.MongoClient("mongodb://admin:SU2orange!@mongo:27017/")
mydb = myclient['demo']
feedbackcollection = mydb['feedback']

@app.route('/submitform', methods=['POST'])
def submitform():
    data = request.form.to_dict(flat=True)
    data['submission_datetime'] = str(datetime.datetime.now())
    data_str = json.dumps(data)
    logging.info(f"SUBMISSION: {data_str}")
    feedbackcollection.insert_one(data)
    return redirect("/")


@app.route("/", methods=['GET'])
def home():
    logging.info("Route: /")
    return render_template('index.html')

@app.route('/formv1', methods=['GET'])
def formv1():
    return render_template('formv1.html')

@app.route('/formv2', methods=['GET'])
def formv2():
    return render_template('formv2.html')