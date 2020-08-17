from flask import Flask,render_template,request,redirect
import mysql.connector as db
import os
import json

db_param={
    'user':'mysql',
    'host':'localhost',
    'password':'',
    'database':'itemdb'
}

app = Flask(__name__)

ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])
app.config['UPLOAD_FOLDER']='./static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    conn=db.connect(**db_param)
    cur=conn.cursor()
    stmt='SELECT * FROM list'
    cur.execute(stmt)
    rows=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',list=rows)

if __name__=='__main__':
    app.debug = True
    app.run()
