from flask import Flask
from password.routes import password_bp


app = Flask(__name__)
app.register_blueprint(password_bp)


