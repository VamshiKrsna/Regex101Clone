import re
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    # GETS regex and text .
    return render_template('home.html')

@app.route('/',methods = ["POST"])
def regex():
    reg_ex = request.form['regex']
    test_str = request.form['test_string']

    matches = list(re.findall(reg_ex,test_str))

    return render_template('regex.html', matches = matches)


if __name__ == "__main__":
    app.run(debug=True)