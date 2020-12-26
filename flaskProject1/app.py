from flask import Flask, redirect,url_for, render_template

app = Flask(__name__)

@app.route('/')
def index_func():
    #you get the name
    username= ''
    return render_template('index2.html',name = username)

@app.route('/Tal')
def about_func():
    return 'Hello, my name is Tal Yachini'

@app.route('/home')
@app.route('/')
def home_func():
    return render_template('home.html' , user = {'firstName' : 'Ariel' , 'lastName' : 'Perchik'}, hobbies = ['dancing, teaching'], degree = ('B.Sc' , 'M.Sc'))

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


@app.route('/user')
def user_func():
    user_from_DB = {'firstName' : 'Ariel' , 'lastName' : 'Perchik' , 'gender' :'boy'}
    return render_template('user.html', user = user_from_DB, hobbies = ['dancing, teaching'])

if __name__ == '__main__':
    app.run(debug=True)
