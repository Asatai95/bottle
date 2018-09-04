#!/usr/bin/venv python
# -*- coding: utf_8 -*-
import MySQLdb
from bottle import get, route, run, template, static_file, request, redirect, response, view
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

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

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
def test_sub():

    amount = '500'

    stripe_token = request.forms.get('stripeToken')
    mail_address = request.forms.get('stripeEmail')

    stripe.api_key = stripe_keys['secret_key']

    stripe.Charge.create(
        amount=amount,
        currency="jpy",
        description="Charge for {mail}".format(mail=mail_address),
        source=stripe_token
    )

    gmail_usr = 'defense433@gmail.com'
    gmail_password = 'Asatai95!'
    you = mail_address
    jp_encoding = 'iso-2022-jp'
    mail_subject = '〇〇商品について'
    body = 'text.txt'
    sender_name = u"OkiDoki株式会社"

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
            message = '確かに支払いは完了しました。'
            return template('message' ,message=message)

        server.close()

    else:

        print('test')

        return template("top", amount=amount)

@route('/text')
def text():

    message = 'データベースの中身を公開するよー！！'


    db = MySQLdb.connect(user='b4da42a09cc349', passwd='dd235253', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_d9c662866ce227f', charset='utf8')
    con = db.cursor()

    sql = 'select test from test where id = 1'
    test = con.execute(sql)
    db.commit()


    result = con.fetchall()
    result = result[0][0]

    return template('message', message=message, main=result)

@route('/text', method='POST')
def text_db():

    form = request.forms.get('form')
    print(form)

    db = MySQLdb.connect(user='b4da42a09cc349', passwd='dd235253', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_d9c662866ce227f', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'insert into test(test) values(%s)'
    text = con.execute(sql, ('form'))
    db.commit()
    print(text)

    result = con.fetchall()
    print(result)

    return result

@route('/text_sub', method='POST')
@view('message')
def text_db():

    form = request.forms.get('form')
    print(form)

    db = MySQLdb.connect(user='b4da42a09cc349', passwd='dd235253', host='us-cdbr-iron-east-01.cleardb.net', db='heroku_d9c662866ce227f', charset='utf8')
    con = db.cursor()
    print('???')

    sql = 'insert into test(test) values(%s)'
    text = con.execute(sql, ('form'))
    db.commit()
    print(text)

    result = con.fetchall()
    print(result)

    return result

# @route('/email')
# def sendmail():
#
#     gmail_usr = 'defense433@gmail.com'
#     gmail_password = 'Asatai95!'
#     you = 'asatai918@gmail.com'
#     jp_encoding = 'iso-2022-jp'
#     mail_subject = '〇〇商品について'
#     body = 'text.txt'
#     sender_name = u"OkiDoki株式会社"
#
#     with open(body, 'r', encoding='utf-8') as file:
#         body = file.read()
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#
#     server.ehlo()
#
#     server.starttls()
#
#     server.ehlo()
#
#     server.login(gmail_usr, gmail_password)
#
#
#     if server is not False:
#
#         msg = MIMEText(body.encode(jp_encoding), "plain", jp_encoding)
#
#         from_jp = Header(sender_name, jp_encoding)
#         msg['From'] = from_jp
#         From = gmail_usr
#         msg['Subject'] = Header(mail_subject, jp_encoding)
#         msg['To'] = you
#         to = msg['To']
#
#         server.sendmail(From, to, msg.as_string())
#
#
#         print('Email')
#         if server is not False:
#             message = '確かにメッセージを送信しました。'
#             return template('message' ,message=message)
#
#         server.close()
#
#     else:
#
#         print('test')



run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
