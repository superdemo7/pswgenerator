from PyInquirer import style_from_dict, Token, prompt, Separator
def menu():
    question = [
        {
        'type': 'list',
        'name': 'choices',
        'message': 'Elige una opcion',
        'choices': [
            'Cambiar el nombre de una contraseña',
            'Ver historial',
            Separator(),
            'Borrar una contraseña',
            'Borrar todo'
        ]
    }
    ]
    option_selected = prompt(question)
    print(option_selected)