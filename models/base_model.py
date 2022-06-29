#!/usr/bin/python3


class BaseModel:

    def __init__(self):
        self.id = 
        self.created_at =
        self.updated_at =

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')


    def save(self):
        pass

    def to_dict(self):
        pass
