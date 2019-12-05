from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError

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
    #buscar todos los nombres del archivo json y meterlos a un arreglo
    nombres = ['PSW', 'mi favorita', 'la nueva', 'Imposible']
    arregloNombres = nombres
    return nombres

def changeName():
    questions = [
        {
            'type': 'list',
            'name': 'choices',
            'message': 'Elige el nombre a cambiar',
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
    #volver a agarrar los nombres del archivo json pero esta vez con su contraseña y cambiar el valor de su contra
    nombres = ['PSW', 'mi favorita', 'la nueva', 'Imposible']
    for x in range(0,len(nombres)):
        if(nombres[x] == answers['choices']):
            nombres[x] = answers['newName']
            break
    print(nombres)
    #remplazarlo en el json
changeName()