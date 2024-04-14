from app import app, views, models
from flask import Response, render_template, request, redirect, url_for


@app.route("/")
def index():
    return render_template("base.html")


@app.get("/registration")
def get_reg():
    return render_template("registration.html")


@app.post("/registration")
def post_reg():
    data = request.form["first_name"]
    return Response(f"{data}")
