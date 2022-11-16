#14
from flask import Flask, render_template
#30
from config import Config
#44
from .api.routes import api
#24
from .site.routes import site
#40
from .authentication.routes import auth

#41
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
#44
from flask_cors import CORS
from helpers import JSONEncoder

#14
app = Flask(__name__)
#44
CORS(app) # security 

#25
app.register_blueprint(site)
#40
app.register_blueprint(auth)
#44
app.register_blueprint(api)

app.json_encoder = JSONEncoder
#30
app.config.from_object(Config)
root_db.init_app(app)
#41 
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)