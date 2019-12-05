from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import json

def Nombres(answers):
    with open('historial.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['historial']:
            nombres.append(user['name'])
    return nombres

def verHistorial():
    questions = [
        {
            'type': 'list',
            'name': 'choices',
            'message': 'selecciona el historial de alguno de los nombres',
            'choices': Nombres
        },
    ]
    answers = prompt(questions)
    with open('historial.json') as file:
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