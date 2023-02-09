from flask import Flask, render_template

# создаем объект приложения как экземпляр класса Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = ""
    return render_template('index.html',
                           title='',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
