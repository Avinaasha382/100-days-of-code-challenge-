import requests 
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hi</h1>"

@app.route("/guess/<name>")
def guesser(name):
    response = requests.get(url="https://api.agify.io",params={"name":name})
    response.raise_for_status()
    guess_age = response.json()["age"]

    response = requests.get(url="https://api.genderize.io",params={"name":name})
    response.raise_for_status()
    guess_gender = response.json()["gender"]

    return render_template("guess.html",person_name=name,age=guess_age,gender=guess_gender)



if __name__ == "__main__":
    app.run(debug=True)