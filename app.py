from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///gamesih.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Login_details(db.Model):
    Id = db.Column(db.Integer,primary_key =True)
    fname =db.Column(db.String(200))
    mname =db.Column(db.String(200))
    lname =db.Column(db.String(200))
    age =db.Column(db.Integer)
    phone =db.Column(db.String(13))
    address =db.Column(db.String(600))
    email = db.Column(db.String(200),nullable = False)
    password = db.Column(db.String(600),nullable = False)
    

## we will add more table in database as our requirement


with app.app_context():
     db.create_all()



@app.route('/', methods=['GET','POST'])
def main():
    
    return render_template('main.html')

@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passw = request.form['passw']
        info = Login_details.query.filter_by(email = email).first()
        if info == None :
            return render_template('error.html',data = "Email is not ragistered please sign up",links ="/signup" )
        elif(info.password != passw):
            return render_template('error.html',data =" Wrong pass word Try Again",links = "/login")
        else:
            return render_template('alogin.html',data =info,name=info.fname)
    return render_template('login.html')

@app.route('/signup',methods =['GET','POST'])
def signup():
    
    if request.method == 'POST':
        email = request.form['email']
        info = Login_details.query.filter_by(email = email)
        if (info!=None):
            return render_template('error.html',data = "User already ragistered please login",links ="/login")
        else:
            fname = request.form['firstname']
            mname = request.form['middlename']
            lname = request.form['lastname']
            age = request.form['age']
            phone = request.form['phone']
            address = request.form['address']
            passw = request.form['pass']
            newp = Login_details(fname=fname,mname=mname,lname=lname,age=age,phone=phone,address=address,email=email,password=passw)
            db.session.add(newp)
            db.session.commit()
            return render_template('login.html')
    
    return render_template('sign_up.html')



if __name__ == "__main__": 
    app.run(debug=True, port=8000)




