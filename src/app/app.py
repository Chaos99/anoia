
from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
print("app created")

#login = LoginManager(app)


# load routes definition from file
from . import routes

if __name__ == "__main__":
    app.run()