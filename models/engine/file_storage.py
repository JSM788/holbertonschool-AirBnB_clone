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
        dic_to_json = {}
        for k in FileStorage.__objects.keys():
            dic_to_json.update({k: FileStorage.__objects[k].to_dict()})
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dic_to_json))


    def reload(self):
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

