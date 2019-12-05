from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError

def Nombres(answers):
    #buscar todos los nombres del archivo json y meterlos a un arreglo
    nombres = ['PSW', 'mi favorita', 'la nueva', 'Imposible']
    arregloNombres = nombres
    return nombres

def borrarPswd():
    questions = [
        {
            'type': 'list',
            'name': 'choices',
            'message': 'Elige la contraseña a borrar (se borrara el nombre junto con su contraseña)',
            'choices': Nombres
        },
    ]
    answers = prompt(questions)
    #volver a agarrar los nombres del archivo json pero esta vez con su contraseña y meterlos a un arreglo
    nombres = ['PSW', 'mi favorita', 'la nueva', 'Imposible']
    for x in range(0,len(nombres)):
        if(nombres[x] == answers['choices']):
            nombres.pop(x)
            break
    print(answers['choices']+ ' borrado satisfactoriamente junto con su contraseña')
    print(nombres)

borrarPswd()