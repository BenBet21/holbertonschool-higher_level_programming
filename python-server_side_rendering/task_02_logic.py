from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('python-server_side_rendering/items.json', 'r') as file:
        data = json.load(file)
    return render_template('index.html', items=data['items'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('python-server_side_rendering/items.json', 'r') as file:
        data = json.load(file)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)