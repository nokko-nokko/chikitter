# from sqlalchemy import Column, Integer, String, Text, DateTime
# from models.database import Base
# from datetime import datetime

# 以下を追加

from flask_sqlalchemy import SQLAlchemy
from app.app import app
from datetime import datetime
import os

db_uri = os.environ.get('DATABASE_URL') or 'postgresql://localhost/positive'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PositiveContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)

    def __init__(self, body=None):
        self.body = body

    def __repr__(self):
        return '<Body %r>' % (self.body)

# class PositiveContent(Base):
#     __tablename__ = 'positivecontents'
#     id = Column(Integer, primary_key=True)
#     body = Column(Text)

#     def __init__(self, body=None):
#         self.body = body

#     def __repr__(self):
#         return '<Body %r>' % (self.body)