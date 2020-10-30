#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''
        HBNB Command interpreter
    '''
    prompt = "(hbnb)"
    file = None

    def do_EOF(self, args):
        'EOF command to exit the program'
        return True

    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'do anything'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
