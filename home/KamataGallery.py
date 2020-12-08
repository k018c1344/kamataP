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

#----------------------------   画面表示

@app.route('/')
#初期画面
def index():
    return render_template('index.html')

@app.route('/photo')

def photo():
    return render_template('photo.html')

@app.route('/enter')

def enter():
    return render_template('enter.html')

@app.route('/login')
#ログイン画面遷移
def login():
    if 'user_name' in session:
        #ログインした後ログアウトされていない場合
        name=str(session['user_name'])
        return render_template('mypage.html',name=name)
    return render_template('message.html')

@app.route('/login',methods=['POST'])
#ログイン処理
def login_send():
    name=request.form.get('user_name')
    pw=request.form.get('password')
    if name=="" or pw=="":
        return redirect('/login')
    if request.form.get('user_name'):
        session['user_name']=request.form.get('user_name')
    return render_template('mypage.html',name=name)

@app.route('/new')
#新規登録画面遷移
def new():
    return render_template('message-new.html')

@app.route('/new',methods=['POST'])
#新規登録処理
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
#ログアウト処理
def logout():
    session.pop('user_name',None)
    return redirect('/')

@app.route('/send',methods=['POST'])
#画像送信処理
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
