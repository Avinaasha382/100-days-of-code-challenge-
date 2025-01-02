from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5
import os 
import dotenv

dotenv.load_dotenv()

class LoginForm(FlaskForm):
    email = StringField(label="Email",validators=[Email(message="Not a valid email address")])
    password = PasswordField(label="Password",validators=[DataRequired(),Length(min=8,message="Field must be atleast 8 characters long")])
    login = SubmitField(label="Log In")



app = Flask(__name__)
app.secret_key = os.getenv("secret_key")

bootstrap = Bootstrap5(app)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_email = login_form.email.data
        user_password = login_form.password.data

        print(user_email)
        print(user_password)
        
        if user_email == "admin@email.com" and user_password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        return render_template("login.html",form=login_form)





if __name__ == '__main__':
    app.run(debug=True)
