from flask import Flask,render_template,request

app = Flask(__name__)
app.config['UPLOAD_FORDER']='./static/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send',methods=['POST'])
def send():
    img_file=request.files['img_file']
    img_file.save(app.config['UPLOAD_FORDER']+img_file.filename)
    return '<p>'+img_file.filename+'を送信しました</p>'

if __name__=='__main__':
    app.debug = True
    app.run()
