from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "ThisIsMySecrectKey2022"
app.jinja_env.filters["zip"] = zip


@app.route("/", methods=["POST", "GET"])
def myindex():
    if "email" in session:
        return redirect(url_for('success_req'))
    else:
        # If the submit button is clicked -> request post
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # If email and password correct
            if email == 'admin@gmail.com' and password == 'pass':
                session['email'] = email
                return redirect(url_for('success_req'))

            # If email or password Incorrect
            else:
                return redirect(url_for('myindex'))

        return render_template("index.html")


@app.route("/success")
def success_req():
    notive = "You are logged in...!"
    return render_template('success.html', notive=notive)


@app.route("/logout")
def logout_req():
    session.pop("email")
    return redirect(url_for('myindex'))


@app.route("/code")
def mycode():
    # belajar looping
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # conditioning/ if-else
    moods = "sad"  # if happy she loves, if not she is sad

    # if already logged in
    if "email" in session:
        return render_template("codes.html", value=days, moods=moods)

    # if not logged in
    else:
        return redirect(url_for('myindex'))


@app.route("/table")
def mytable():
    data_json = {
        "no": [1, 2, 3, 4, 5, 6, 7, 8],
        "fruit": ["mango", "melon", "watermelon", "pinaple", "orange", "strawberry", "blueberry", "apple"],
        "animal": ["bear", "pig", "cat", "dog", "horse", "comodo", "lion", "wolf"]
    }
    if "email" in session:
        return render_template("table.html", datable=data_json)
    else:
        return redirect(url_for('myindex'))


@app.route("/about")
def myabout():
    if "email" in session:
        return render_template("about.html")
    else:
        return redirect(url_for('myindex'))


@app.route("/contact")
def mycontact():
    if "email" in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('myindex'))


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
        return "No values ?????? are stored...."


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
