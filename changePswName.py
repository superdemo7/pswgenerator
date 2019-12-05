from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError

class validateNew(Validator):
    def validate(self, document):
        newName = len(document.text)
        if not newName > 2:
            raise ValidationError(
                message='El nuevo nombre es muy corto',
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
            'type': 'input',
            'name': 'newName',
            'message': 'Introduce el nuevo nombre',
            'validate': validateNew
        }
    ]
    answers = prompt(questions)
    #volver a agarrar los nombres del archivo json y meterlos a un arreglo
    nombres = ['PSW', 'mi favorita', 'la nueva', 'Imposible']
    for x in range(0,len(nombres)):
        if(nombres[x] == answers['choices']):
            nombres[x] = answers['newName']
            break
    print(nombres)
    #remplazarlo en el json
changeName()