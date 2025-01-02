from flask import Flask 

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_text_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route("/")
@make_bold
@make_text_underline
def bye():
    return "Heyy..!"


if __name__ == "__main__":
    app.run(debug=True)