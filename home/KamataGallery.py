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
    'database':'SampleDB'
}

app = Flask(__name__)

path='../static/files/'
app.config['SECRET_KEY']=os.urandom(24)

#----------------------------   画面表示 ----------------------------

@app.route('/')
#初期画面遷移
def index():
    return render_template('index.html')

@app.route('/photo')
#photo画面遷移
def photo():
    return render_template('photo.html')

@app.route('/fashion')
#初期画面遷移
def fashion():
    return render_template('index.html')

@app.route('/food')
#初期画面遷移
def food():
    return render_template('index.html')

@app.route('/music')
#初期画面遷移
def music():
    return render_template('index.html')

@app.route('/art')
#初期画面遷移
def art():
    return render_template('index.html')

app.route('/company')
#初期画面遷移
def company():
    return render_template('index.html')

@app.route('/enter')
#enter画面遷移
def enter():
    return render_template('enter.html')

#----------------------- 各種処理 ---------------------

@app.route('/login')
#ログイン画面遷移
def login():
    if 'user_ID' in session:
        #ログインした後ログアウトされていない場合
        id=str(session['user_ID'])
        name=str(session['user_ID'])
        return render_template('mypage.html',name=name)
    return render_template('message.html')

@app.route('/login',methods=['POST'])
#ログイン処理
def login_send():
    id=request.form.get('user_ID')
    pw=request.form.get('password')
    if id=="" or pw=="":
        return redirect('/login')
    conn=db.connect(**db_param)
    cur=conn.cursor()
    stmt='SELECT * FROM sample1 WHERE user_ID=%s AND password=%s'
    cur.execute(stmt,(id,pw))
    rows=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if len(rows)==0:
        return redirect('/login')
    else:
        if request.form.get('user_ID'):
            session['user_ID']=request.form.get('user_ID')
            FilePath=path+id
        return render_template('mypage.html',user_ID=session['user_ID'],FilePath=FilePath)

@app.route('/new')
#新規登録画面遷移
def new():
    return render_template('message-new.html')

@app.route('/new',methods=['POST'])
#新規登録処理
def new_send():
    id=request.form.get('user_ID')
    pw=request.form.get('password')
    if id=="" or pw=="":
        return redirect('/new')
    if request.form.get('user_ID'):
        session['user_ID']=request.form.get('user_ID')
    conn=db.connect(**db_param)
    cur=conn.cursor()
    stmt='SELECT * FROM sample1 WHERE user_ID=%s'
    cur.execute(stmt,(id,))
    rows=cur.fetchall()
    if len(rows)==0:
        cur.execute('INSERT ignore INTO sample1(user_ID,password) VALUES(%s,%s)',(id,pw))
        FilePath=path+id
        reference=os.path.exists(FilePath)
        if reference==False:
            os.mkdir(FilePath)
        conn.commit()
        cur.close()
        conn.close()
        return render_template('mypage.html',user_ID=id)
    else:
        return redirect('/new')

@app.route('/logout')
#ログアウト処理
def logout():
    session.pop('user_ID',None)
    return redirect('/')

@app.route('/send',methods=['POST'])
#ファイル送信処理
def upload():
    if 'user_ID' in session:
        id=str(session['user_ID'])
    else:
        return redirect('/login')

    file=request.files['file']
    FilePath=path+id
    file.save(FilePath+'/'+file.filename)
    result=file.filename+'を送信しました'
    return render_template('mypage.html',id=id,result=result)

if __name__=='__main__':
    app.debug = True
    app.run()
