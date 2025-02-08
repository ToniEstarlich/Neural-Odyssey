from flask import Flask
from models import db
from models.user import User
from models.course import Course
from models.progress import Progress
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# Add a route to verify the app is working
@app.route('/')
def home():
    return "Hello, Neural Odyssey"

if __name__ == '__main__':
    app.run(debug=True)