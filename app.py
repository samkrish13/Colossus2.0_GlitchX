from flask import Flask, render_template
from webcam_feed import video_bp

app = Flask(__name__)
app.register_blueprint(video_bp)

@app.route('/')
def home():
    return render_template('live.html')

if __name__ == '__main__':
    app.run(debug=True)
