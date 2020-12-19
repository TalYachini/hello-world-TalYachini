from flask import Flask, redirect,url_for

app = Flask(__name__)


@app.route('/Tal')
def about_func():
    return 'Hello, my name is Tal Yachini'

@app.route('/home')
@app.route('/')
def home():
    return 'Welcome to my Website'

@app.route('/check')
def check():
    good_exercise = True
    if good_exercise:
        return redirect(url_for('about_func'))
    else:
        return 'exercise failed'

@app.route('/other')
def other():
    return redirect('/Tal')

if __name__ == '__main__':
    app.run(debug=True)
