from flask import Flask
from urls import esther

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(esther)

if __name__ == '__main__':
    app.run(port=80, debug=True)
