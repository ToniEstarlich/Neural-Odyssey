import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Toni2207'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Toni2207@localhost/neural_odyssey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False