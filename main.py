#Librerias
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
import pyperclip
import os.path
import json
import click

#Archivos
import installation
import menu
import generate
import timer

@click.command()
@click.argument('action',default="nothing")
def main(action):
    if os.path.exists('config.json'):
        if action == "list":
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
        elif action == "generate":
            generate.createPswd()
        elif action == "nothing":
            print('Opciones disponibles: "list" para menu y "generate" para crear contraseña')
            timer.stop()
        else:
            print('La opcion elegida no es valida')
            timer.stop()
    else:
        installation.install(timer)
        
if __name__ == "__main__":
    main()
    pass