from flask import Flask, render_template, request
from main import update_html

# Flask website
app = Flask(__name__)

# Home
@app.route('/')
def home():

    return render_template('index.html')

# Results
@app.route('/', methods=['POST'])

def results():

    new_text = request.form['user_entry']

    # main.py
    update_html(new_text)

    # Render results page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

