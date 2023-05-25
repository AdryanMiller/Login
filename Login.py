# Bibliotecas

from colorama import Style, Fore, Back


# Lista para E-mail e Password

email = []
password = []


cada_Email = str(input('E-mail: ')).strip()

cada_Password = str(input('Password: '))

# Condição para ver se está preenchido

if cada_Email and cada_Password:
    a_Possicao = cada_Email.find('@')
    servidor = cada_Email[a_Possicao:]

    if a_Possicao != -1 and '.' in servidor:
        print('Email Comfirmado')
        email.append(cada_Email)
    else:
        print('Email invalido')

    #Condição para o Password
    cont = len(cada_Password)
    if cont >= 8 and cont <= 16:
        print('Senha cormirmada')
        password.append(cada_Password)
    else:
        print('Senha Invalida')



else:
    print('Campos não preenchidos corretamente. Preencha novamente por favor!!!')

print(email)
print(password)


