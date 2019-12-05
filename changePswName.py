from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import json

class validateNew(Validator):
    def validate(self, document):
        newName = len(document.text)
        if not newName > 0:
            raise ValidationError(
                message='la nueva contraseña no puede estar vacia',
                cursor_position=len(document.text))
        if newName > 21:
            raise ValidationError(
                message='la nueva contraseña esta muy larga',
                cursor_position=len(document.text))

def Nombres(answers):
    #cambiar por el nombre del json
    with open('passwords.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['passwords']:
            nombres.append(user['name'])
    return nombres

def changeName():
    questions = [
        {
            'type': 'list',
            'name': 'choices',
            'message': 'Elige el nombre para cambiar su contraseña',
            'choices': Nombres
        },
        {
            'type': 'password',
            'name': 'newName',
            'message': 'Introduce la nueva contraseña',
            'validate': validateNew
        }
    ]
    answers = prompt(questions)
    #cambiar por el nombre del json
    with open('passwords.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['passwords']:
            nombres.append(
                {
                    "nombre": user['name'], 
                    "contra": user['psw']
                })

    for x in range(0,len(nombres)):
        nombre = nombres[x].get('nombre')
        if(nombre == answers['choices']):
            nombres[x]['contra'] = answers['newName']
            break
    data['passwords'] = nombres
    #cambiar por el nombre del json
    with open ('passwords.json', 'w') as file:
        json.dump(data, file, indent=2)