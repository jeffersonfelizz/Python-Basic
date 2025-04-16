from random import randint, Random

'''
Desafio - Crie um Programa que:

- Escolhe um numero secreto.
- pede por um chute do usuario
- verifica se o chute esta correto.

- se não acertou, da uma dica de se o chute foi maior ou menor que o numero secreto.

- repete isso até 3 vezes

'''


numero = Random(randint(1, 10))
chute = input('Digite um numero entre 1 e 10: ')

tentativas = 0

while tentativas < 3:
    if chute == numero:
        print('Parabens! Voce acertou o numero secreto!')
        break
    elif chute < numero:
        print('O numero secreto e maior que', chute)
    else:
        print('O numero secreto e menor que', chute)
    
    tentativas += 1
    
    if tentativas < 3:
        chute = int(input('Tente novamente: '))
    else: 
        print('Voce nao acertou o numero secreto. O numero era', numero)
        break
