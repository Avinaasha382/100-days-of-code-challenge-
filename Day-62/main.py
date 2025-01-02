from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,TimeField,SelectField
from wtforms.validators import DataRequired,URL
import csv
import pandas as pd
import os 
import dotenv

dotenv.load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("secret_key")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = URLField(label="Cafe Location on Google Maps(URL)", validators=[DataRequired(),URL()])
    opening_time =TimeField(label="Opening Time e.g. 8AM", validators=[DataRequired()]) 
    closing_time =TimeField(label="Closing Time e.g. 5.30PM", validators=[DataRequired()])
    coffee_rating =  SelectField(label="Coffee Rating", choices=[(1,"☕️"),
                                                                 (2,"☕️☕️",),
                                                                 (3,"☕️☕️☕️"),
                                                                 (4,"☕️☕️☕️☕️")])
    wifi_strength_rating = SelectField(label="Coffee Rating", choices=[(1,"💪"),
                                                                 (2,"💪💪",),
                                                                 (3,"💪💪💪"),
                                                                 (4,"💪💪💪💪")])
    
    power_socket_availability = SelectField(label="Coffee Rating", choices=[(1,"🔌"),
                                                                 (2,"🔌🔌",),
                                                                 (3,"🔌🔌🔌"),
                                                                 (4,"🔌🔌🔌🔌")])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        df = pd.read_csv("cafe-data.csv")
        print(form)
        print(df.columns)

        coffee_rating = ""
        wifi_strength = ""
        power_socket_availability = ""


        for _ in range(int(form.coffee_rating.data)):
            coffee_rating+="☕️"

        for _ in range(int(form.coffee_rating.data)):
            wifi_strength+="💪"
        
        for _ in range(int(form.power_socket_availability.data)):
            power_socket_availability+='🔌'
       

        

        data = [form.cafe.data,form.location.data,form.opening_time.data,
                       form.closing_time.data,coffee_rating,wifi_strength,
                       power_socket_availability]
        print(data)
        df.loc[len(df)] = data
        df.to_csv("cafe-data.csv",index=False)
        return redirect("/cafes")
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
