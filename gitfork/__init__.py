from flask import Flask

app = Flask(__name__)

from gitfork.fork_repo.routes import mod

app.register_blueprint(fork_repo.routes.mod)

