from flask import Flask
from flask_cors import CORS
from config import Config
from db import db, init_db
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
    app.run(debug=True)
