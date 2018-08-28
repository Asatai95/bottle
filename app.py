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
def sendmail():

    gmail_usr = 'defense433@gmail.com'
    gmail_password = 'Asatai95!'

    sent_form = 'Taishi Asato'
    to = ['defense433@gmail.com' ,'https://app-py-heroku.herokuapp.com']
    subject = 'TEST'
    body = "Hey, whats up? \n\n- You"
    email_text = """\
    FROM: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_form, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email')
    except:
        print ('Something went wrong...')


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
