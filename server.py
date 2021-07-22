from flask import Flask, render_template, request, redirect
import pymysql
from random import *

db = pymysql.connect(host="localhost", user="root", passwd="sosnm0907#", db="free_board", charset="utf8")
cur = db.cursor()

app = Flask(__name__)
global int1
int1 = 0
@app.route('/')
def index():
    sql = "SELECT * from userdata"
    cur.execute(sql)

    data_list = cur.fetchall()

    


    return render_template('main.html', value=data_list)
@app.route('/write')
def write():
    return render_template('write.html')
@app.route('/loding',methods=['GET', 'POST'])
def roding():
    global int1
    name = request.args.get('name')
    title = request.args.get('title')
    result = request.args.get('result')
    print(result)
    sql = "SELECT * from userdata"
    cur.execute(sql)


    mycursor = db.cursor()
    c = randrange(999999)

    sql = "INSERT INTO userdata (`num`, `title`, `writer`, `views`, `context`) VALUES (%s, %s,%s,%s,%s)"
    val = (str(c), str(title), str(name), '1', str(result))

    mycursor.execute(sql, val)

    db.commit()

    return redirect('/')
@app.route('/look/<int:articleID>/')
def board_content(articleID):
    UserId = articleID

    sql = "SELECT * FROM userdata WHERE num = '{}'".format(UserId)

    cur.execute(sql)

    result = cur.fetchall()




    return render_template("look.html", result=result)
    

if __name__ == '__main__':
    app.run()