from flask import Flask, render_template
from models import data as dt

app = Flask(__name__)


@app.route('/')
def home():
    skills = dt.skills
    return render_template('progressbars.html', skills=skills)


if __name__ == '__main__':
    app.run(debug=True)
