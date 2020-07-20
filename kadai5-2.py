from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

datelist=[]
numlist=[]
n=0

@app.route('/')
def index():
    return render_template('kadai5-2.html',n=n)

@app.route('/',methods=['POST'])
def send():
    num=request.form.get('num')
    if num != '':
        numlist.append(num)
        dt=datetime.datetime.now()
        dt=dt.strftime('%m/%d %H:%M')
        datelist.append(dt)
        n=int(len(numlist))

    return render_template('kadai5-2.html',numlist=numlist,datelist=datelist,n=n)

if __name__=='__main__':
    app.debug = True
    app.run()
