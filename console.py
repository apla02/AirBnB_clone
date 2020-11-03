#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
all_objects = models.storage.all()


class HBNBCommand(cmd.Cmd):
    '''
        HBNB Command interpreter
    '''
    prompt = "(hbnb) "

    def do_create(self, line):
        'Create  command to create a new instance of a class\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            '''
            eval(args): execute the python expression
            eval(args)(self):return the object equivalent
            to the python expression'''
            new_object = eval(args[0])(self)
            new_object.save()
            print(new_object.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        'Show command to prints the string representation of an instanced'
        args = shlex.split(line)
        '''args = self.argparser.parse_args(line.split(line))'''
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in all_objects.keys():
                print("** no instance found **")
        else:
            print(all_objects[args[0] + "." + args[1]])

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects[args[0] + "." + args[1]]
            '''{key :obj} = clase.id'''
            models.storage.save()

    def do_all(self, args):
        'Prints all string representation of all instancesq\n'
        if args not in classes:
            print("** class doesn't exist **")
        else:
            list1 = []
            for key, value in all_objects.items():
                list1.append(value.__str__())
            print(list1)

    def do_update(self, line):
        'Updates an instance- attribute based on the class name and id\n'
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in all_objects.keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            dic2 = all_objects[key]  # all_objects = storage.all()
            args[2]  # name attribute
            args[3] = args[3].replace("\"", "")  # args[3] = value attribute
            setattr(dic2, args[2], args[3])
            dic2.save()

    def do_EOF(self, line):
        'EOF command to exit the program\n'
        return True

    def do_quit(self, args):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        'do anything\n'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
