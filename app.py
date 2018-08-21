import os
from bottle import route, run, template, static_file, request, redirect, response

# db_name = {'heroku'}
# host = {'us-cdbr-iron-east-01.cleardb.net'}
# username = {'b8b921e229e863'}
# passwd = {'a87b2e7e'}

var connection = mysql.createConnection({
  host     : 'us-cdbr-iron-east-01.cleardb.net',
  user     : 'b4da42a09cc349',
  password : 'dd235253',
  database : 'heroku'
});


@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/")
def top():

    return template('top')

@route("/test")
def top_db():

    con = connection.cursor()

    sql = 'select test from test where id = 1'
    test = con.execute(sql)
    db.commit()
    print(sql)
    print(test)

    result = con.fetchall()
    print(result)

    return template('test', tests=result)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
