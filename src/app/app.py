from flask import Flask
from .config import Config
from flask_login import LoginManager
from os import path, walk


app = Flask(__name__)
app.config.from_object(Config)
print("app created")

# login = LoginManager(app)


# load routes definition from file
from . import routes


if __name__ == "__main__":
    extra_dirs = ['./templates', ]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    app.run(extra_files=extra_files)

