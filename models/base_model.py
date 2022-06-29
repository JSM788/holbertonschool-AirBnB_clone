#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')


    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic.update({'created_at' : self.created_at.isoformat()})
        new_dic.update({'updated_at' : self.updated_at.isoformat()})
        return new_dic
