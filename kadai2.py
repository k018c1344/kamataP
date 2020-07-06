from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')

def now():
    dt=datetime.datetime.now()
    strdt=dt.strftime('%m/%d %H:%M')
    return strdt

if __name__=='__main__':
    app.debug = True
    app.run()
