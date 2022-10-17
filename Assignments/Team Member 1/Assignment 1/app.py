from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    email=request.form['email']
    number=request.form['no']
    if request.method == "POST":
	    return render_template('home.html',name=name1,mail=email,num1=number)

if __name__ == '__main__':
    app.run()
