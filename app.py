from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    bar_data = {'HTML': 95, 'CSS': 90, 'Javascript': 40, 'Python': 75, 'Flask': 60}
    return render_template('progressbars.html', bar_data=bar_data)


if __name__ == '__main__':
    app.run(debug=True)
