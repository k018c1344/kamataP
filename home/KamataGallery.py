from flask import Flask,render_template,request,redirect,session
import mysql.connector as db
import glob
import re
import os
import json

db_param={
    'user':'mysql',
    'host':'localhost',
    'password':'',
    'database':'kamatagallery'
}

app = Flask(__name__)

path='./files/'
app.config['SECRET_KEY']=os.urandom(24)

@app.route('/')
def index():
    if 'user_name' in session:
        name=str(session['user_name'])
        return render_template('mypage.html',name=name)
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('message.html')

@app.route('/login',methods=['POST'])
def login_send():
    name=request.form.get('user_name')
    pw=request.form.get('password')
    if name=="" or pw=="":
        return redirect('/login')
    if request.form.get('user_name'):
        session['user_name']=request.form.get('user_name')
    return render_template('mypage.html',name=name)

@app.route('/new')
def new():
    return render_template('message-new.html')

@app.route('/new',methods=['POST'])
def new_send():
    name=request.form.get('user_name')
    pw=request.form.get('password')
    if name=="" or pw=="":
        return redirect('/new')
    if request.form.get('user_name'):
        session['user_name']=request.form.get('user_name')
    FilePath=path+name
    reference=os.path.exists(FilePath)
    if reference==False:
        os.mkdir(FilePath)
    return render_template('mypage.html',name=name)

@app.route('/logout')
def logout():
    session.pop('user_name',None)
    return redirect('/')

@app.route('/send',methods=['POST'])
def upload():
    if 'user_name' in session:
        name=str(session['user_name'])
    file=request.files['file']
    FilePath=path+name
    file.save(FilePath+'/'+file.filename)
    result=file.filename+'を送信しました'
    return render_template('mypage.html',name=name,result=result)

if __name__=='__main__':
    app.debug = True
    app.run()
