from flask import Flask, request, render_template, redirect, url_for
from flask.templating import render_template_string
import requests
app = Flask(__name__)

project_list = [
    {"name": "Github Finder", "img": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        "desc": "First App made with Flask"},
    {"name": "Google", "img": "https://rotulosmatesanz.com/wp-content/uploads/2017/09/2000px-Google_G_Logo.svg_.png",
        "desc": "Yeah, I made google"},
    {"name": "AWS", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1200px-Amazon_Web_Services_Logo.svg.png", "desc": "No biggie"},
    {"name": "My Chair", "img": "https://i.pinimg.com/564x/f0/58/ea/f058eac53a6d60cb4dcc96e3447ed128.jpg",
        "desc": "Did I tell you I'm also a carpenter?"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", data=project_list)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/github")
def github():
    return render_template("github.html")


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
