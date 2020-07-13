from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def kadai3_2():
    list={'英語':87,'数学':90,'国語':45,'理科':76,"社会":31}
    return render_template('kadai3-2.html',list=list)

if __name__=='__main__':
    app.debug = True
    app.run()
