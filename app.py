from flask import Flask
from routes.emotion_routes import emotion_routes
from routes.learning_routes import learning_routes

app = Flask(__name__)

app.register_blueprint(emotion_routes, url_prefix="/api/emotion")
app.register_blueprint(learning_routes, url_prefix="/api/learn")

if __name__ == "__main__":
    app.run(debug=True)
