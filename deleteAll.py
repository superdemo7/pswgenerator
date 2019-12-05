from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
import os
import menu
def deleteAll(timer):
    confirmation = [
        {
            'type': 'confirm',
            'qmark':'!',
            'message': 'Esta accion borrara toda la información de aplicación...continuar?',
            'name': 'delete',
            'default': False
        },
        {
            'type': 'confirm',
            'qmark':'!!!',
            'message': 'Confirmar?',
            'name': 'delete_confirm',
            'default': False,
            'when':lambda answers: answers['delete']
        }
    ]
    answers = prompt(confirmation)
    if not answers['delete'] or not answers['delete_confirm']:
        menu.menu(timer)
    else:
        os.remove("config.json")
        timer.stop()
        timer.clear()
        print('Para reinstalar vuelva a abrir el programa')
        quit()