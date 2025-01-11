from flask import Flask, render_template, request, redirect, url_for
import sqlite3


connect_db = sqlite3.connect("Bookstore.db",check_same_thread=False)
cursor = connect_db.cursor()



app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    cursor.execute("SELECT * FROM Books")
    data = cursor.fetchall()
    print(data)
    print("hi")
    return render_template("index.html",books=data,isEmpty = (len(data) == 0))


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    
    elif request.method == "POST":
        book_data = request.form
        title = book_data["title"]
        author = book_data["author"]
        rating = book_data["rating"]

        cursor.execute(f"""INSERT INTO Books (title,author,rating)
                   VALUES ('{title}','{author}', '{rating}')""")
        
        connect_db.commit()
        return redirect("/")

@app.route("/edit/<id>",methods=["GET","POST"])
def update_rating(id):
    if request.method == "GET":
        return render_template("update_rating.html",id=id)
    
    elif request.method == "POST":
        new_rating = request.form["rating"]
        cursor.execute(f"""UPDATE  Books 
                    SET rating = {new_rating} 
                        WHERE id = {id} """)
        connect_db.commit()
        return redirect("/")

@app.route("/delete/<id>",methods=["GET"])
def delete_book(id):
    cursor.execute(f"DELETE FROM Books WHERE id = {id}")
    connect_db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

