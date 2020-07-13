from flask import Flask,render_template

app = Flask(__name__)

list=[]

@app.route('/user/<username>/')
def add_user(username):
    list.append(username)
    return render_template('kaida4_user.html',message=username)

@app.route('/list/')
def show_list():
    return render_template('kadai4_list.html',list=list)

if __name__=='__main__':
    app.debug = True
    app.run()
