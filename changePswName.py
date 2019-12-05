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
            nombres.append(user['nombre'])
    return nombres

def uploadPswd(anterior, nombrePsw):
    with open('historial.json') as file:
        hist = json.load(file)
        names = []
        if(not hist == []):
            for nombre in hist['historial']:
                names.append({
                    "name": nombre['name'],
                    "historial": nombre['historial']
                })
            cambiado = False
            #si habia cambiado anteriormente la contra
            for x in range(0,len(names)):
                if(names[x]['name'] == nombrePsw):
                    names[x]['historial'].append({ "psw": anterior })
                    cambiado = True
                    break
            #Si nunca habia cambiado la contra
            if(not cambiado):
                names.append({
                    "name": nombrePsw,
                    "historial": [
                        {
                            "psw": anterior
                        }
                    ]
                })
        else:
            names.append({
                "name": nombrePsw,
                "historial": [
                    {
                        "psw": anterior
                    }
                ]
            })

    hist['historial'] = names
    with open ('historial.json', 'w') as file:
        json.dump(hist, file, indent=2)

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
                    "nombre": user['nombre'], 
                    "contra": user['contra']
                })

    for x in range(0,len(nombres)):
        nombre = nombres[x].get('nombre')
        if(nombre == answers['choices']):
            anteriorPswd = nombres[x]['contra']
            nombres[x]['contra'] = answers['newName']
            break

    data['passwords'] = nombres
    #cambiar por el nombre del json
    with open ('passwords.json', 'w') as file:
        json.dump(data, file, indent=2)

    uploadPswd(anteriorPswd, answers['choices'])