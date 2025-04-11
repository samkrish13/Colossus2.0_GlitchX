from flask import Flask
from flask_cors import CORS
from config import Config
from db import init_db
from moviepy.editor import *
from routes.emotion_routes import emotion_routes
from routes.learning_routes import learning_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize DB
init_db(app)

# Register Blueprints
app.register_blueprint(emotion_routes, url_prefix="/api/emotion")
app.register_blueprint(learning_routes, url_prefix="/api/learn")

if __name__ == "__main__":
    from waitress import serve
    app.run(debug=True)
