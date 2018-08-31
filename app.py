#!/usr/bin/venv python
# -*- coding: utf_8 -*-
import MySQLdb
from bottle import route, run, template, static_file, request, redirect, response, view
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import message
from email import charset
import email
import base64
import smtplib
import os
import stripe
import sys

charset.add_charset('utf-8', charset.SHORTEST, None, 'utf-8')
cset = 'utf-8'
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
def sendmail():

    gmail_usr = 'defense433@gmail.com'
    gmail_password = 'Asatai95!'
    you = 'asatai918@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = you
    From = msg['From']

    msg['To'] = gmail_usr
    to = msg['To']

    msg['Subject'] = "TEST"
    subject = msg['Subject']

    text = "テスト"
    text_sub = text.encode("ascii", errors="ignore")
    email_text = """\
        FROM: %s
        To: %s
        Subject: %s

        %s
        """ % (From, to, subject, text_sub )

    msg_sub = MIMEText(text, "plain", cset)


    if msg_sub is not False:

        # msg = msg.encode('ascii')

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()

        server.starttls()

        server.ehlo()

        server.login(gmail_usr, gmail_password)


        msg.attach(msg_sub)


        server.sendmail(you, gmail_usr, email_text)



        server.quit()
        print('Email')
        if server is not False:
            message = '確かにメッセージを送信しました。'
            return template('message' ,message=message)

    else:

        # message = 'エラーが発生しました。'
        print('test')
        # if message is not False:
        #     message = 'エラーが発生しました。'
        #     print ('Something went wrong...')
        #     return template('message', message=message)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
