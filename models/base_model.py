#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        pass

    def save(self):
        pass

    def to_dict(self):
        pass
