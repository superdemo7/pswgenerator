from PyInquirer import style_from_dict, Token, prompt, Separator
#Opciones
import changePswName
import borrarPswd
import verHistorial
import deleteAll
import email
def menu(timer):
    timer.restart()
    question = [
        {
        'type': 'list',
        'qmark':'<>',
        'name': 'choices',
        'message': 'Elige una opcion',
        'choices': [
            {
                'name':'Cambiar el nombre de una contraseña',
                'value':'change'
            },
            {
                'name':'Ver historial',
                'value':'history'
            },
            {
                'name':'Enviar correo',
                'value':'email'
            },
            Separator(),
            {
                'name':'Borrar una contraseña',
                'value':'delete'
            },
            {
                'name':'Borrar todo',
                'value':'delete_all'
            },
            Separator(),
            {
                'name':'Salir',
                'value':'exit'
            }
        ]
    }
    ]
    option_selected = prompt(question)
    try:
        option_selected = option_selected['choices']
    except KeyError:
        pass
    if option_selected == 'delete':
        borrarPswd.borrarPswd(timer)
    elif option_selected == 'change':
        changePswName.changeName(timer)
    elif option_selected == 'history':
        verHistorial.verHistorial(timer)
    elif option_selected == 'delete_all':
        deleteAll.deleteAll(timer)
    elif option_selected == 'email':
        email.send(timer)
    elif option_selected == 'exit':
        timer.stop()
        timer.clear()
        print('Tu sesión se ha cerrado satisfactoriamente')
        quit()