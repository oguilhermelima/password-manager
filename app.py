from flask import Flask
from src.application.password.password_controller import password_bp


app = Flask(__name__)
app.register_blueprint(password_bp)


