from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def myindex():
    # belajar looping
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # conditioning/ if-else
    moods = "sad"  # if happy she loves, if not she is sad

    # set variable

    return render_template("index.html", value=days, moods=moods)


@app.route("/about")
def myabout():
    return render_template("about.html")


@app.route("/contact")
def mycontact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
