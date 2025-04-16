'''
Desafio 4: Transformador de texto
Enunciado:
Peça ao usuário uma frase e exiba:

A frase toda em maiúsculas

A frase toda em minúsculas

A frase com todas as ocorrências da letra "a" substituídas por "@".

Dica:
Use os métodos upper(), lower() e replace().
'''

# Solicita ao usuário uma frase
frase = input("Digite uma frase: ")

print(frase.upper())  # Exibe a frase toda em maiúsculas

print(frase.lower())  # Exibe a frase toda em minúsculas

print(frase.replace("a", "@")) # Exibe a frase com todas as ocorrências da letra "a" substituídas por "@"
