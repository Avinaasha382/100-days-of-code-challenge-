from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

db = sqlite3.connect("Movies.db",check_same_thread=False)
cursor = db.cursor()

class AddMovieForm(FlaskForm):
    title = StringField(label="Title",validators=[DataRequired()])
    year = StringField(label="Year",validators=[DataRequired()])
    description = StringField(label="Description",validators=[DataRequired()])
    rating = StringField(label="Rating",validators=[DataRequired()])
    ranking = StringField(label="Ranking",validators=[DataRequired()])
    review = StringField(label="Review",validators=[DataRequired()])
    img_url = StringField(label="Image URL",validators=[DataRequired()])
    submit_button = SubmitField(label="Add Movie")

class UpdateMovieForm(FlaskForm):
    rating = StringField(label="Rating",validators=[DataRequired()])





#CREATE TABLE

# cursor.execute(""" CREATE TABLE MOVIES 
#                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                title VARCHAR(255) UNIQUE NOT NULL,
#                year INTEGER NOT NULL,
#                description VARCHAR(255) NOT NULL,
#                rating FLOAT NOT NULL,
#                ranking INTEGER NOT NULL,
#                review VARCHAR(255) NOT NULL,
#                img_url VARCHAR(100) NOT NULL )""")




@app.route("/")
def home():
    cursor.execute("SELECT * FROM MOVIES ORDER BY ranking ASC")
    all_movies = cursor.fetchall()
    print(all_movies)
    return render_template("index.html",movies=all_movies)

@app.route("/add",methods=["GET","POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate():
        movie_data = form.data
        cursor.execute(f""" INSERT INTO MOVIES (title,year,description,rating,ranking,review,img_url)
                       VALUES ('{movie_data["title"]}', 
                       {int(movie_data['year'])},
                       '{movie_data['description']}',
                       {float(movie_data["rating"])},
                       {int(movie_data['ranking'])},
                       '{movie_data['review']}',
                       '{movie_data['img_url']}')""")
        db.commit()
        return redirect("/")
        
        
    else:
        return render_template("add.html",form=form)

@app.route("/delete/<id>")
def delete_movie(id):
    cursor.execute(f"DELETE FROM MOVIES WHERE id = {id}")
    db.commit()
    print(id)
    return redirect("/")

@app.route("/update/<id>",methods=["GET","POST"])
def update_movie(id):
    form = UpdateMovieForm()
    if form.validate():
        new_rating = form.data["rating"]
        cursor.execute(f"""UPDATE MOVIES
                       SET rating = {new_rating}
                        WHERE id = {id} """)
        
        db.commit()
        return redirect("/")
    else:
        return render_template("edit.html",form=form,id=id)


if __name__ == '__main__':
    app.run(debug=True)
