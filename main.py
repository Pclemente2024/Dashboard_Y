from flask import Flask
from flask import render_template as render
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route("/")
def main(name=None):
    url_for('static', filename='style.css')
    return render('index.html', name='Yandri')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f'Metodo POST'
    else:
        return f'Metodo no es Post'
        

if __name__ == "__main__":
    app.run(debug=True)