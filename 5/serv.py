from http.server import HTTPServer, CGIHTTPRequestHandler
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template,url_for,redirect

class LoginForm(FlaskForm):
    username = StringField('Id твой', validators=[DataRequired()])
    password = PasswordField('Пароль твой какой', validators=[DataRequired()])
    cap = StringField('Id кэпа твоего', validators=[DataRequired()])
    password_cap = PasswordField('Пароль его', validators=[DataRequired()])
    submit = SubmitField('Попробовать получить доступ')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('base.html', title='Авторизация', form=form,url=url_for('static',filename='m.jpg'))
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




