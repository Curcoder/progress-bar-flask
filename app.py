

from flask import Flask, render_template
# Import the data file with the skills list from the models package
from models import data as dt

app = Flask(__name__)


@app.route('/')
def home():
    # Add the skills list(dictionary) and make it callable
    skills = dt.skills
    return render_template('views/progressbars.html', skills=skills)


if __name__ == '__main__':
    app.run(debug=True)
