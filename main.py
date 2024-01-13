import flask
from flask import Flask, request, jsonify

from bs4 import BeautifulSoup



app = Flask(__name__)


# Простые примеры
@app.route('/test')
def test():
    return 'Hello world!'


@app.route('/get_json')
def get_json():
    json = {'abc': 123, 'bcd': 234}
    return json


@app.route('/get_html')
def get_html():
    html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
                <html>
                 <head>
                  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                  <title>Пример веб-страницы</title>
                 </head>
                 <body>
                  <h1>Заголовок</h1>
                  <!-- Комментарий -->
                  <p>Первый абзац.</p>
                  <p>Второй абзац.</p>
                 </body>
                </html>"""
    return html


@app.route('/get_html_2')
def get_html_2():
    with open('./example_html.html', encoding='utf-8') as file:
        html_2 = file.read()
        print(html_2)
        file.close()
    return html_2


# Примеры с указанием типа запроса
@app.route('/get_sum', methods=["GET"])
def sum():
    args = request.args
    print(args)
    a = request.args.get("a")
    b = request.args.get("b")
    return str(int(a) + int(b))


@app.route('/change_html', methods=["GET"])
def change_html():
    first_text = request.args.get("first")
    second_text = request.args.get("second")

    with open('./example_html.html', 'r', encoding='utf-8') as file:
        start_html = file.read()
        file.close()

    soup = BeautifulSoup(start_html, features="html.parser")

    target_first = soup.body.find(id='first')
    target_first.string.replace_with(first_text)
    # target_first = first_text

    target_second = soup.body.find(id='second')
    #target_second = second_text
    target_second.string.replace_with(second_text)

    result_html = str(soup)
    return result_html



def main():
    app.run(port=5001)


if __name__ == '__main__':
    main()
