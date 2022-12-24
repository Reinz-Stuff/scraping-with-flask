from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "ThisIsMySecrectKey2022"


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


# Parsing nilai Int, String
@app.route("/parsing/<string:value>")
def myparsing(value):
    return f"The Value is: {value}"


# Argument parser
@app.route("/parsingargument")
def parsingargument():
    data = request.args.get("values")
    return f"The value of the parser argument is: {data}"


# parsing nilai url untuk men set nilai variable
@app.route("/page/<int:value>")
def session_1(value):
    session["myvalue"] = value
    return "Successfully set value...!"


@app.route("/page/view")
def view_session():
    try:
        data = session["myvalue"]
        return f"the value that has been set is: {data}"
    except KeyError:
        return "No values ​​ are stored...."


# logout / delete session
@app.route("/page/logout")
def logout_session_1():
    session.pop("myvalue")
    return "successfully logout session...."


# Redirect session
@app.route("/redirect-about")
def lets_redirect_about():
    return redirect(url_for('myabout'))


@app.route("/redirect-contact")
def lets_redirect_contact():
    return redirect(url_for('mycontact'))


if __name__ == '__main__':
    app.run(debug=True)
