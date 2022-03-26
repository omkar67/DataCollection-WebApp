import imp
from sqlalchemy.sql import func
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 
from sending_email import send_mail
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:1234@localhost/height_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="Data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/success",methods=["POST"])
def sucess():
    if request.method=="POST":
        email=request.form['email_name']
        height=request.form['height']
        
        insertion_data=Data(email,height)
        if db.session.query(Data).filter(Data.email_==email).count()==0:
            db.session.add(insertion_data)
            db.session.commit()
            
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            
            count=db.session.query(Data.height_).count()
            send_mail(email,height,average_height,count)



            return render_template("sucess.html",methods=["POST"])

    return render_template("index.html",text="Thank You, But You sir Have Already Participated")

if __name__=="__main__":
    app.debug=True
    app.run()


