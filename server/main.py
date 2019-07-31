from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_index():
    return render_template('index.html', token="Hello Flask+react")


app.run(debug=True)