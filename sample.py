# def square(x):
#     return x * x
#
# def test_square_positive():
#     assert square(5) == 25
#
# def test_square_negative():
#     assert square(-5) == 25
#
# def test_square_zero():
#     assert square(0) == 0




# def reverse(string: str) -> str:
#     pass
#
# def test_reverse_blank():
#     assert reverse("") == ""
#
# def test_reverse_hello():
#     assert reverse("hello") == "elloh"
#
# def test_reverse_space():
#     assert reverse(" hello world") == "dlrow ollew"

from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"

app.run()
@app.route("/profile/")
@app.route("/profiles/")
def profile():
    return "Profile Page!"

@app.route("/profiles/<name>")
def profile_dynamic(name):
    return f"Profile Page! {name}"