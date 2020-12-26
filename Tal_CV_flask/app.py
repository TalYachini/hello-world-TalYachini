from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)


@app.route('/')
def Tal_CV():
    return render_template('CV_Tal_Yachini.html')

@app.route('/assignment8')
def My_Hobbies():
    myHobbies = ['Dancing', 'Swimming', 'Traveling']
    return render_template('assignment8.html', hobbies = myHobbies)

@app.route('/users_list')
def My_Users_List():
    return render_template('LIST_USERS.html')

@app.route('/header')
def myHeader():
    return render_template('header.html')

@app.route('/MyMusic')
def MyMusic():
    myFaveSongs = {'Kansas' : 'Dust in the Wind' , 'Shalom Hanoch' : 'Layla' , 'Coldplay' : 'The Scientist ' , 'Amy Winehouse' : 'Back to Black'}
    return render_template('MyMusic.html' , FaveMusic = myFaveSongs)


if __name__ == '__main__':
    app.run(debug=True)
