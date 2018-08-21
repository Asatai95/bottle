import SQLite3
import os
from bottle import route, run, template, static_file, request, redirect, response

# db_name = {'heroku'}
# host = {'us-cdbr-iron-east-01.cleardb.net'}
# username = {'b8b921e229e863'}
# passwd = {'a87b2e7e'}

@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/")
def top():

    return template('top')

@route("/test")
def top_db():

    db = SQLite3.connect(db='heroku', host='us-cdbr-iron-east-01.cleardb.net', port=3306, user=u'b8b921e229e863', passwd='a87b2e7e')
    con = db.cursor()

    sql = 'select test from test where id = 1'
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    result = con.fetchall()
    print(result)

    return template('test', tests=result)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
