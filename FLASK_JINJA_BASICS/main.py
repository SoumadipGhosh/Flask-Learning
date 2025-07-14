from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "Suyatra":89,
        "Souvik":87,
        "KunduVaipo":84,
        "Tanmoy":83
        
    }
    return render_template("index.html",marks=marks)

app.run(debug=True)