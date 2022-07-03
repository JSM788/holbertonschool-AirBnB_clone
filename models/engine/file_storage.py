#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serialize/Deserialize python data
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new object
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects.update({f"{obj_name}.{obj.id}": obj})

    def save(self):
        """
        Serialize __objects to the JSON file __file_path
        """
        dic_to_json = {}
        for k in FileStorage.__objects.keys():
            dic_to_json.update({k: FileStorage.__objects[k].to_dict()})
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dic_to_json))

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects
        """
        json_file = FileStorage.__file_path
        json_to_dic = {}
        dic = {}
        try:
            with open(json_file, mode='r', encoding='utf-8') as f:
                json_to_dic = json.load(f)
            for k, v in json_to_dic.items():
                clase = v['__class__']
                del v['__class__']
                dic.update({k: eval(clase)(**v)})
            FileStorage.__objects = dic
        except FileNotFoundError:
            return
