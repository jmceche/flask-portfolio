from flask import Flask, request, render_template, redirect, url_for
import requests
import data
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", data=data.project_list)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html", data=data.my_skills)


@app.route("/github")
def github():
    resp = requests.get("https://api.github.com/users/jmceche")
    user_data = resp.json()
    return render_template("github.html", data=user_data)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
