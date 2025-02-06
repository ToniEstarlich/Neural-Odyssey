from flask import Flask
from models import db
from models.user import User
from models.course import Course
from models.progress import Progress
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)