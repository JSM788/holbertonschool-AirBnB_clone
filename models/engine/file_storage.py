#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_name = obj.__class__.__name__
        FileStorage.__objects.update({f"{obj_name}.{obj.id}": obj})

    def save(self):
        pass

    def reload(self):
        pass
