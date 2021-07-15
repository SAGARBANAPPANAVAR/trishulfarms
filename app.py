from flask import Flask,render_template, redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/about us')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = False)
