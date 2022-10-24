from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class PositiveContent(Base):
    __tablename__ = 'positivecontents'
    id = Column(Integer, primary_key=True)
    body = Column(Text)

    def __init__(self, body=None):
        self.body = body

    def __repr__(self):
        return '<Body %r>' % (self.body)