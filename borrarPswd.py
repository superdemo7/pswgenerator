from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import json
import menu
def Nombres(answers):
    #buscar todos los nombres del archivo json y meterlos a un arreglo
    with open('config.json') as file:
        data = json.load(file)
        nombres = []
        for user in data['passwords']:
            nombres.append(decrypt(data['secret'],bytes(user['nombre'],'latin-1')).decode('latin-1'))
        nombres.append({
            'name':'<--Volver',
            'value':'exit'
        })
    return nombres

def borrarPswd(timer):
    with open('config.json') as file:
        data = json.load(file)
    if(data['passwords']):
        questions = [
            {
                'type': 'list',
                'name': 'choices',
                'message': 'Elige el nombre a borrar (se borrara el nombre junto con su contraseña)',
                'choices': Nombres
            },
        ]
        answers = prompt(questions)
        try:
            if answers['choices'] == 'exit':
                menu.menu(timer)
            else:
                with open('config.json') as file:
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
                with open ('config.json', 'w') as file:
                    json.dump(data, file, indent=2)
                print(answers['choices']+ ' borrado satisfactoriamente junto con su contraseña')
                print(nombres)
                menu.menu(timer)
        except KeyError:
            pass
    else:
        print('No tienes ninguna contraseña archivada, agregala usando la opcion "generate"')
        menu.menu(timer)