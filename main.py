from flask import Flask, render_template, request

app = Flask(__name__)

profiles = {
    1: {"name":"Andrew", "age":25},
    2: {"name": "Lera", "age": 20},
    3: {"name": "Maxim", "age": 10}
}

items = [
    {"name":"IPhone 17", "price":60000},
    {"name":"IPhone 16", "price":50000},
    {"name":"IPhone 17 PRO", "price":90000},
    {"name":"IPhone 17 PRO MAX", "price":120000}
]

@app.route('/')
def main():
    return render_template('main.html', items=items)

@app.route('/profile/<id>')
def user(id):
    return render_template('profile.html', id=id, profiles=profiles)

if __name__ == '__main__':
    app.run(debug=True)