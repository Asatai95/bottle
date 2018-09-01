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
    jp_encoding = 'iso-2022-jp'
    mail_subject = '〇〇商品について'
    body = 'text.txt'
    sender_name = u"〇〇株式会社"

    with open(body, 'r', encoding='utf-8') as file:
        body = file.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login(gmail_usr, gmail_password)


    if server is not False:

        msg = MIMEText(body.encode(jp_encoding), "plain", jp_encoding)

        from_jp = Header(sender_name, jp_encoding)
        msg['From'] = from_jp
        From = gmail_usr
        msg['Subject'] = Header(mail_subject, jp_encoding)
        msg['To'] = you
        to = msg['To']

        server.sendmail(From, to, msg.as_string())


        print('Email')
        if server is not False:
            message = '確かにメッセージを送信しました。'
            return template('message' ,message=message)

        server.close()

    else:

        # message = 'エラーが発生しました。'
        print('test')
        # if message is not False:
        #     message = 'エラーが発生しました。'
        #     print ('Something went wrong...')
        #     return template('message', message=message)


run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
