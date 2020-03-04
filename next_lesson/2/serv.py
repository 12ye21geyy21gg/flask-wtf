from http.server import HTTPServer, CGIHTTPRequestHandler
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template,url_for,redirect
from flask_login import LoginManager,login_user,logout_user,login_required
import json,random
from data import db_session
from data import users
from flask import Flask

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')




app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def root():
    return render_template('base.html')
@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)
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




