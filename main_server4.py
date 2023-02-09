from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "123"

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # answer = dict(request.form)
        # print(answer["username"], answer["password"], answer["remember_me"] if 'remember_me' in answer else "")
        return redirect('/success')
    return render_template('login.html', title="Авторизация", form=form)

@app.route('/success')
def success():
    return render_template('index_in.html', title="Авторизация", username="пользователь. Вы успешно авторизованы")


if __name__ == '__main__':
    print("http://127.0.0.1:8080/odd_even")
    print("http://127.0.0.1:8080/news")
    print("http://127.0.0.1:8080/login")
    app.run(port=8080, host='127.0.0.1')

