from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key= "dojo_survey_secret"

@app.route("/", methods=["GET"])
def showSurvey():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def submitDojoSurvey():
    userData = {
        "username": request.form["username"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comments": request.form["comments"]
    }
    session["userData"]=userData
    return redirect("/result")

@app.route("/result", methods=["GET"])
def showSurveyResult():
    if "userData" not in session:
        return redirect("/")
    return render_template("info.html")

@app.route("/", methods=["POST"])
def resetData():
    session.clear()
    return redirect("/")
if(__name__=="__main__"):
    app.run(debug=True)