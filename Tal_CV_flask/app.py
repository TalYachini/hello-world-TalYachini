from flask import Flask,redirect,url_for, render_template,request, session

app = Flask(__name__)
app.secret_key = '123'
user_list = [{'First Name': 'Tal', 'Last Name': 'Yachini', 'Email': 'yachini@post.bgu.ac.il'}
    , {'First Name': 'Or', 'Last Name': 'Hadar', 'Email': 'orhadar24@gmail.com'}
    , {'First Name': 'Boaz', 'Last Name': 'Kishoni', 'Email': 'boazki@post.bgu.ac.il'}]

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

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func1():
    user_reg = ''
    user_search= None
    user_exist = False
    userFound = ''
    empty_search = False

    if request.method == 'POST':
        user_reg = request.form['user_reg']
        session['user_reg'] = user_reg

    if request.method == 'GET':
            user_search = request.args.get('user_search')
            # check if user in list
            user_exist, userFound = UserExist_func(user_search, user_list)
            if user_search == '':
                empty_search = True


    return render_template('/assignment9.html', user_search = user_search, user_exist=user_exist,
                           userFound=userFound, empty_search=empty_search, user_list = user_list,
                           user_reg = user_reg)



def UserExist_func(user_detail,user_list):
    userExist = False
    userFound = ''
    for user in (user_list):
        for value in user.values():
            if user_detail == value:
                userExist = True
                userFound = user
    return userExist,userFound

@app.route('/logout' ,methods=['GET', 'POST'])
def sign_out():
    session.pop('user_reg',None)

    return redirect(url_for("assignment9_func1"))

if __name__ == '__main__':
    app.run(debug=True)
