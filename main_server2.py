from flask import Flask, render_template

# создаем объект приложения как экземпляр класса Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = { "username": "ученик Лицея Академии Яндекса",
              "title": 'Домашняя страница'}
    return render_template('index.html', **param)


if __name__ == '__main__':
    print("http://127.0.0.1:8080/index")
    app.run(port=8080, host='127.0.0.1')
