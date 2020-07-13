from flask import Flask,render_template

app = Flask(__name__)

@app.route('/user/<username>/')
def profile(username):
    return render_template('index.html',message=username)

if __name__=='__main__':
    app.debug = True
    app.run()
