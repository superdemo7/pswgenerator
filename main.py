#Librerias
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
import pyperclip
import os.path
#Archivos
import installation
import menu
import json

def main():
    if os.path.exists('config.json'):
        questions = [
            {
                'type': 'password',
                'name': 'pass',
                'message': 'Ingresa tu PIN',
            }
        ]
        pin = prompt(questions)
        with open('config.json') as file:
            data = json.load(file)
        for user in data['user']:
            contra = user['psw']
        if pin['pass'] == contra:
            menu.menu()
        else:
            print('El PIN ingresado es incorrecto')
    else:
        installation.install()
        
if __name__ == "__main__":
    main()
    pass