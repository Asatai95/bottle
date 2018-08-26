import MySQLdb
from bottle import route, run, template, static_file, request, redirect, response, view
from email.mime.text import MIMEText
import email
import smtplib
import os
import stripe
import sys

sys.setrecursionlimit(30000)

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']



@route("/static/:path#.+#", name='static')
def test(path):
    return static_file(path, root='static')

@route("/")
def top():

    return template("top")

@route("/test_sub")
def test():

    return template('top')

@route("/test")
@view("test")
def test_view():

    return dict(key=stripe_keys['publishable_key'])

@route("/test", method='POST')
@view("test")
def test_sub():

    amount = '500'

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.forms['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Bottle Charge'
    )

    return template("top", amount=amount)

@route('/email')
@view('top')
def sendmail(to_addr_list, subject, message):

    subject = "TEST"
    message = 'TESTだよ'
    recepients_list = "defense433@gmail.com"
    sendmail(recepients_list, subject, message)
    username = "defense433@gmail.com"
    from_addr="defense433@gmail.com"
    password="Asatai95!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    newmessage = '\r\n'.join([
              'To: %s' %recepient_list,
               'From: %s' % from_addr,
                'Subject: %s' %subject,
                '',
                message
                ])
    sys.setrecursionlimit(30000)

    try:
        server.sendmail(from_addr, password, message)
        print('test')
        sendNotification()
    except:
        print('error')
    server.quit()
    sendNotification()

# sendNotification()

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
