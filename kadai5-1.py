from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('kadai5-1.html')

@app.route('/send',methods=['POST'])
def send():
    name=request.form.get('name')
    address=request.form.get('address')
    return render_template('kadai5-1recevie.html',name=name,address=address)

if __name__=='__main__':
    app.debug = True
    app.run()
