
from flask import Flask,redirect,url_for, render_template,request, session,Blueprint
import mysql
from mysql import connector
from flask import jsonify

import pkgutil
import sys



app = Flask(__name__)
app.secret_key = '123'
user_list = [{'First Name': 'Tal', 'Last Name': 'Yachini', 'Email': 'yachini@post.bgu.ac.il'}
    , {'First Name': 'Or', 'Last Name': 'Hadar', 'Email': 'orhadar24@gmail.com'}
    , {'First Name': 'Boaz', 'Last Name': 'Kishoni', 'Email': 'boazki@post.bgu.ac.il'}]

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

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


def interact_db(query,query_type:str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user = 'root',
                                         passwd = 'root',
                                         database = 'myflaskappdb')

    cursor = connection.cursor (named_tuple = True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# -----------------------------------------------------

@app.route('/users')
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users = query_result)

# -----------------------------------------------------
@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        first_name = request.form['First Name']
        last_name = request.form['Last Name']
        email = request.form['Email']
        password = request.form['Password']
        query = "INSERT INTO users(first_name,last_name,email,password) VALUES ('%s','%s','%s','%s')" % (first_name, last_name, email, password)
        interact_db(query = query, query_type='commit')
        return redirect('/users')
    return render_template('insert_user.html', req_method = request.method)

# ----------------------------------------------------
@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args.get('id')
        query = "DELETE FROM users WHERE id ='%s';" % user_id
        interact_db( query=query, query_type='commit')
        return redirect('/users')

    return 'deleted user'

@app.route('/assignment11/users')
def get_users():
    if request.method == "GET":
        query = "SELECT id,first_name,last_name,email FROM users"
        query_result = interact_db(query=query, query_type='fetch')
    if (len(query_result) == 0):
        return jsonify({
            'success': 'False',
            'Error': 'There is no users data'
        })
    else:
        return jsonify({
            'success': 'True',
            'data': query_result
        })

@app.route('/assignment11/users/selected/', defaults={'SOME_USER_ID': 00})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def get_user_by_id(SOME_USER_ID):
    if request.method == "GET":
        query = "SELECT id,first_name,last_name,email FROM users WHERE id ='%s'" % SOME_USER_ID
        query_result = interact_db(query=query, query_type= 'fetch')
        if (len(query_result)== 0):
            return jsonify({
                'success': 'False',
                'Error': 'User does not exist',
                'Default User ID': SOME_USER_ID
            })
        else:
            return jsonify({
                'success': 'True',
                'data': query_result[0],

            })

if __name__ == '__main__':
    app.run(debug=True)
