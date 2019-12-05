from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import json
import menu

def Nombres(answers):
    with open('config.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['historial']:
            nombres.append(user['name'])
        nombres.append({
            'name':'<--Volver',
            'value':'exit'
        })
    return nombres

def verHistorial(timer):
    with open('config.json') as file:
        data = json.load(file)
    if(not data['historial'] == []):
        questions = [
            {
                'type': 'list',
                'name': 'choices',
                'message': 'selecciona el historial de alguno de los nombres',
                'choices': Nombres
            },
        ]
        answers = prompt(questions)
        if answers['choices'] == 'exit':
            menu.menu(timer)
        else:
            with open('config.json') as file:
                data = json.load(file)
                names = []
                for nombre in data['historial']:
                    names.append({
                        "name": nombre['name'],
                        "historial": nombre['historial']
                    })
                mostrar = []
                for x in range(0,len(names)):
                    if(names[x]['name'] == answers['choices']):
                        num = 1
                        for contra in names[x]['historial']:
                            print(str(num)+". "+contra['psw'])
                            num=num+1
            menu.menu(timer)
    else:
        print('No tienes ninguna contraseña archivada, agregala usando la opcion "generate"')
        menu.menu(timer)