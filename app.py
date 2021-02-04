from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def calculate():
    bmi=''
    if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
       Weight=float(request.form.get('weight'))
       Height=float(request.form.get('height'))
       bmi=round(Weight/((Height/100)**2),2)
    return render_template("index.html", bmi=bmi)
