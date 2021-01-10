from flask import Flask,Blueprint,render_template,redirect,url_for,request
import mysql.connector
import pkgutil
import sys

# from utilities.db.db_manager import dbManger
assignment10 = Flask(__name__)
assignment10.secret_key = '321'

assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                         static_url_path='/assignment10.html',
                         template_folder='templates')


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


@assignment10.route('/assignment10',methods=['GET', 'POST'])
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)

@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args.get('id')
        query = "DELETE FROM users WHERE id ='%s';" % user_id
        interact_db( query=query, query_type='commit')
        return redirect('/assignment10')

@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        first_name = request.form['First Name']
        last_name = request.form['Last Name']
        email = request.form['Email']
        password = request.form['Password']
        query = "INSERT INTO users(first_name,last_name,email,password) VALUES ('%s','%s','%s','%s')" % (first_name, last_name, email, password)
        interact_db(query = query, query_type='commit')
        return redirect('/assignment10')

@assignment10.route('/update_row', methods=['GET', 'POST'])
def update_row():
    if request.method == 'POST':
        id_to_update = request.form['ID To Update']
        first_name = request.form['First Name']
        last_name = request.form['Last Name']
        email = request.form['Email']
        password = request.form['Password']
        query = "UPDATE users SET first_name= '%s' , last_name= '%s', email= '%s', password = '%s' WHERE id = %s;" % (first_name,last_name,email,password,id_to_update)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'update user details'