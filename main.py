from flask import Flask
from flask import render_template as render

app = Flask(__name__)

@app.route("/")
def main(name=None):
    return render('index.html', name='Yandri')

if __name__ == "__main__":
    app.run(debug=True)