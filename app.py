import MySQLdb
import os
from bottle import route, run, template, static_file, request, redirect, response, view
import stripe

stripe_keys = {
  'secret_key': os.environ['sk_live_jSdNiWzNTAjyK8jMz7JZ1vvp'],
  'publishable_key': os.environ['pk_live_BeJqMkXLopr3HjiKYmyNMeh0']
}

stripe.api_key = stripe_keys['secret_key']

# test
# db_name = {'heroku'}
# host = {'us-cdbr-iron-east-01.cleardb.net'}
# username = {'b8b921e229e863'}
# passwd = {'a87b2e7e'}

# connection = mysql.createConnection({
#   host     : 'us-cdbr-iron-east-01.cleardb.net',
#   user     : 'b4da42a09cc349',
#   password : 'dd235253',
#   database : 'heroku'
# });


@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/")
@view("top")
def top():

    return dict(key=stripe_keys['publishable_key'])

@route("/test_sub")
def test_sub_view():

    return template('test')

@route("/test_sub", method='POST')
@view("test")
def test_sub():

    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return dict(amount=amount)

# @route("/test")
# @view("test")
# def top_db():
#
#     db = MySQLdb.connect(db='heroku_d9c662866ce227f', host='us-cdbr-iron-east-01.cleardb.net', port=3306, user='b4da42a09cc349', passwd='dd235253')
#     con = db.cursor()
#
#     sql = 'select id, test from test where id = 1'
#     test = con.execute(sql)
#     db.commit()
#     print(sql)
#     print(test)
#
#     result = con.fetchall()
#     _int = result[0][0]
#     sub = result[0][1]
#     print(result)
#     print(_int)
#     print(sub)
#
#     return dict(sub = sub, _int = _int)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
