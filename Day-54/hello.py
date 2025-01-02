from flask import Flask 
import time

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hi"

if __name__ == "__main__":
    app.run()




def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

def say_bye():
    print("bye")

def greet():
    print("Hi Welcome to Chennai!!")

say_hello()

say_bye()


