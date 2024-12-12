from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def main():
    theme = request.cookies.get('theme', 'light')
    lang = request.cookies.get('lang', 'ru')
    if (lang == "ru"):
        return render_template('index.html', theme=theme, lang=lang)
    else:
        return render_template('index_en.html', theme=theme, lang=lang)


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"

@app.route('/set_theme')
def set_theme():
    theme = request.args.get('theme')
    if theme in ['light', 'dark']:
        resp = make_response("Тема установлена")  # Можно вернуть пустой ответ
        resp.set_cookie('theme', theme)
        return resp
    return "Неверная тема", 400

@app.route('/set_lang')
def set_lang():
    lang = request.args.get('lang')
    if lang in ['ru', 'en']:
        resp = make_response("Язык установлен")  # Можно вернуть пустой ответ
        resp.set_cookie('lang', lang)
        return resp
    return "Неверная тема", 400



if __name__ == '__main__':
    app.run(port=5002, debug=True)
