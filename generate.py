from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import pyperclip
import json
import string
import secrets
class CharacterValidation(Validator):
    def validate(self, document):
        try:
            val = int(document.text)
            if val >= 1 and val <= 20 :
                ok = True
            else:
                ok = False
        except ValueError:
            ok = False
        if not ok:
            raise ValidationError(
                message='Tiene que ser un numero y estar entre 5 a 20 caracteres',
                cursor_position=len(document.text))  # Move cursor to end
class NameValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message='El nombre no puede estar vacio',
                cursor_position=len(document.text)
            )
        elif document.text == 'exit':
            raise ValidationError(
                message='Este nombre esta reservado',
                cursor_position=len(document.text)
            )
        else:    
            with open('config.json', 'r') as json_config:
                config = json_config.read()
            passwords = json.loads(config)['passwords']
            for password in passwords:
                if document.text == password['nombre']:
                    raise ValidationError(
                        message='Este nombre ya existe',
                        cursor_position=len(document.text)
                    )
                    break

def createPswd(timer):
    question1 = [
        {
            'type': 'input',
            'qmark': '>',
            'name': 'pass_name',
            'message': 'Nombre de contraseña',
            'validate': NameValidator 
        },
        {
            'type': 'input',
            'qmark': '#',
            'name': 'characters_qty',
            'message': 'Numero de caracteres [5-20]:',
            'default':'5',
            'validate': CharacterValidation
        }
    ]
    answers = prompt(question1)
    question2 = [
        {
            'type': 'checkbox',
            'qmark': '$A#',
            'message': 'Armar contraseña con:',
            'name': 'characters_type',
            'choices': [ 
                {
                    'name' : 'Simbolos ($%#"!..)',
                    'value':'simbols'
                },
                {
                    'name' : 'Numeros (12345...)',
                    'value':'numbers'
                },
                {
                    'name' : 'Letras (ABCDEF...)',
                    'value':'letters'
                }
            ]
        }
    ]
    types = []
    while len(types) < 1:
        types = prompt(question2)['characters_type']
        if len(types)< 1:
            print('Debes seleccionar al menos 1 tipo de caracter')
    
    #Crea string con las elecciones del usuario
    shuffle = ''
    if 'simbols' in types:
        shuffle += string.punctuation
    if 'numbers' in types:
        shuffle += string.digits
    if 'letters' in types:
        shuffle += string.ascii_letters

    #Creacion de contraseña
    created_password = ''.join(secrets.choice(shuffle) for i in range(int(answers['characters_qty'])))
    
    #Lectura y escritura de config.json con la nueva contraseña
    with open('config.json', 'r') as json_config:
        config = json_config.read()
    config = json.loads(config)
    config['passwords'].append({
        'nombre': answers['pass_name'],
        'contra': created_password
    })
    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)
    print('Contraseña creada!')
    #Copiando al portapapeles
    pyperclip.copy(created_password)
    print('...Se ha copiado a tu portapapeles')
    timer.stop()
    quit()