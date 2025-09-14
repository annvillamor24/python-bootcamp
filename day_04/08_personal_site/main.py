from flask import Flask, render_template, request, redirect

app = Flask(__name__)
from datetime import datetime

@app.route("/")
def index():
    now = datetime.now()
    return render_template("landing.html", hour=now.hour, minute=now.minute)



@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    return "Hobby Page! <br> 1. Reading books <br> 2.Riding motorbikes <br> 3. Watching Videos "


@app.route("/opinion/<topic>")
def opinion(topic):
    return "Opinion Page!<br> 1. Politics <br> 2.Music <br> 3. Instrument"



@app.route("/opinion/food/")
def food():
    foods = ["Sinigang", "Pastas", "Karrage", "Adobo","Igado"]
    return render_template("food.html", foods=foods)



@app.route("/skills/")
def skills():
    skill_levels = {
        "Painting": "Intermediate",
        "Dancing": "Abysmal",
        "Singing": "Poor",
        "Translation": "Proficient",
        "Eating": "Professional"
    }
    return render_template("skills.html", skills=skill_levels)


todo_items = ["eat", "clean", "gym"]

@app.get("/todo/")
def get_todo():
    return render_template("todo.html", todos=todo_items)


@app.post("/todo/")
def post_todo():
    if request.form["todo"]:
        data_received = request.form["task"]
        todo_items.append(data_received)


app.run()