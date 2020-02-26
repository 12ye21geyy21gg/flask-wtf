from http.server import HTTPServer, CGIHTTPRequestHandler
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template,url_for,redirect
import json,random


app = Flask(__name__)

@app.route('/member')
def training():
    t = random.choice(json.load(open('templates/members.json',mode='r',encoding='utf8'))['members'])
    param = {}
    param['name'] = t['name']
    param['prof'] = t['prof']
    if t['icon'] % 2:
        param['url'] = url_for('static',filename='j.jpg')
    else:
        param['url'] = url_for('static',filename='m.jpg')
    return render_template('base.html', **param)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




