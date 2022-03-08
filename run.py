import os

from app import app
from db import db

uri = os.getenv('DATABASE_URL')
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()