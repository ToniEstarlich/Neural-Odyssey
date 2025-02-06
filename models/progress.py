from . import db

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    progress_percentage = db.Column(db.Float, default=0.0)

    user = db.relationship('User', backref=db.backref('progress', lazy=True))
    course = db.relationship('Course', backref=db.backref('progress', lazy=True))