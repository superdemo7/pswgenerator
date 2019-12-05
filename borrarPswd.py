from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import json

def Nombres(answers):
    #buscar todos los nombres del archivo json y meterlos a un arreglo
    with open('passwords.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['passwords']:
            nombres.append(user['nombre'])
    return nombres

def borrarPswd():
    with open('passwords.json') as file:
        data = json.load(file)
    if(not data['passwords'] == []):
        questions = [
            {
                'type': 'list',
                'name': 'choices',
                'message': 'Elige el nombre a borrar (se borrara el nombre junto con su contraseña)',
                'choices': Nombres
            },
        ]
        answers = prompt(questions)
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
                nombres.pop(x)
                break

        data['passwords'] = nombres
        #cambiar por el nombre del json
        with open ('passwords.json', 'w') as file:
            json.dump(data, file, indent=2)
        print(answers['choices']+ ' borrado satisfactoriamente junto con su contraseña')
        print(nombres)

borrarPswd()