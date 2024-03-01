from flask import Flask
from flask_cors import CORS


from api.endpoints import blueprint, home_bp


def create_app():
    """Create Flask App"""

    flask_app = Flask(__name__)
    CORS(flask_app)
    flask_app.register_blueprint(blueprint, url_prefix="/api")
    flask_app.register_blueprint(home_bp, url_prefix="/")

    return flask_app


app = create_app()
