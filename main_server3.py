from flask import Flask, render_template
import json

# создаем объект приложения как экземпляр класса Flask
app = Flask(__name__)


@app.route('/')
@app.route('/odd_even')
def index():
    return render_template('odd_even.html', number=6)

@app.route('/news')
def news():
    with open("db/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html',
                           news=news_list,
                           title="Новости")

if __name__ == '__main__':
    print("http://127.0.0.1:8080/odd_even")
    print("http://127.0.0.1:8080/news")
    app.run(port=8080, host='127.0.0.1')
