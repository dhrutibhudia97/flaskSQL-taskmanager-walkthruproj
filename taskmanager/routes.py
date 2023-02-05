from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager .models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


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


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # query the database and attempts to find specified record using data given
    # if not match is found it will trigger 404 error page.
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))
