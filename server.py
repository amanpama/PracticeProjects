from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key= 'secret'

@app.route("/")
def page():
    return render_template("index.html")

@app.route("/form1", methods=["post"] )
def form1():
    print(request.form["Name"])
    print(request.form["Location"])
    print(request.form["Language"])
    print(request.form["Comments"])
    session["Name"]=request.form["Name"]
    session["Location"]=request.form["Location"]
    session["Language"]=request.form["Language"]
    session["Comments"]=request.form["Comments"]
    return redirect("/formsubmitted")

@app.route("/formsubmitted")
def submitted():
    return render_template("formsubmitted.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port=5050)