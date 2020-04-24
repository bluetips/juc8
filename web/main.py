from flask import Flask

from web.wechat import wechat

app = Flask(__name__)
app.debug = True
app.register_blueprint(wechat, url_prefix='/wechat')


@app.route('/')
def welcome():
    return "Welcom To Home Page"


if __name__ == '__main__':
    app.run()
