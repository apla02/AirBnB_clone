#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import json


class FileStorage():
    '''
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Method to return the dictionay __object
        '''
        return self.__objects

    def new(self, obj):
        '''
        '''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Method to serializes __objects to the JSON file
        '''
        print(self.__dict__)
        dic_objects = {}
        for key, value in FileStorage.__objects.items():
            dic_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            json.dump(dic_objects, fd)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        file = FileStorage.__file_path
        try:
            with open(file, "r", encoding='utf-8') as fd: #'{key (class.id): value ({key(id):value(14565r34), key(create):ijkk})}'
                js_rep = json.load(fd)
                for key, value in js_rep.items():
                    myobject = eval(value['class'] + '(**value)')
                    type(self).__objects[key] = myobject

        except:
            pass
