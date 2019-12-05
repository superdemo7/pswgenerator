from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import regex
import json
import secrets
import string
import main
class emailValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[^@]+@[^@]+\.[a-zA-Z]{2,}$', document.text)
        if not ok:
            raise ValidationError(
                message='Porfavor introduce un correo valido',
                cursor_position=len(document.text))

class passValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([0-9])*$', document.text)
        if not len(document.text) == 4:
            raise ValidationError(
                message='Porfavor introduce una contraseña de 4 digitos',
                cursor_position=len(document.text))
        if not ok:
            raise ValidationError(
                message='Porfavor introduce una contraseña de puros caracteres numericos',
                cursor_position=len(document.text))

def install(timer):
    timer.pause()
    questions = [
        {
            'type': 'input',
            'name': 'correo',
            'message': 'Ingresa tu correo',
            'validate': emailValidator
        },
        {
            'type': 'password',
            'message': 'Ingresa tu contraseña para siempre iniciar sesion',
            'name': 'passw',
            'validate': passValidator
        }
    ]
    answers = prompt(questions)
    data = {
        'user':[
            {
                'correo': answers['correo'],
                'psw': answers['passw']
            }
        ],
        'passwords':[],
        'historial':[]
    }
    with open ('config.json', 'w') as file:
        json.dump(data, file, indent=2)
    timer.restart()
    main.main()