'''

Desafio 5: Extrator de nome

Enunciado:

Peça o nome completo do usuário e exiba apenas o primeiro e o último nome separadamente.

Dica:
Use split() para separar as partes do nome.


'''
nomeCompleto = input('Digite seu nome completo: ')
nomeCompleto = nomeCompleto.strip()  # Remove espaços em branco no início e no final
print(f'O primeiro nome é: {nomeCompleto.split()[0]} \nO último nome é: {nomeCompleto.split()[-1]}')