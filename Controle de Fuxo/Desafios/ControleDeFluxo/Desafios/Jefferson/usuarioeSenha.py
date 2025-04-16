'''
Desafio - Crie um Programa que:

- pede por um nome de usuario e uma senha
- verifica se o nome de usuario e a senha estao corretos
- se estiverem corretos, imprime "Acesso permitido"

- se estiverem incorretos, imprime "Acesso negado"
- se o nome de usuario estiver incorreto, imprime "Usuario incorreto"
- se a senha estiver incorreta, imprime "Senha incorreta"


'''


Usuario = input('Digite o nome de usuario: ')
Senha = input('Digite a senha: ')

if Usuario == 'admin' and Senha == '123456':
    print('Acesso permitido')
elif Usuario != 'admin' and Senha == '123456':
    print('Acesso negado')
    print('Usuario incorreto')
elif usuario == 'admin' and senha != '123456':
    print('Acesso negado')
    print('Senha incorreta')
elif Usuario != 'admin' and Senha != '123456':
    print('Acesso negado')
    print('Usuario incorreto')
    print('Senha incorreta')
else:
    print('Acesso negado')
    print('Usuario incorreto')
    print('Senha incorreta')
    
