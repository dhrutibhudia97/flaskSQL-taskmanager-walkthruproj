from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager .models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# when user clicks "add category" button, this will use the
# GET method to render_"add_category"_template.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # once they submit the form if will call the same function but check
    # if request being made is a "POST" method, which posts data 2 database.
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
