from flask import Flask

app = Flask(__name__)

from app import routes

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
