'''
Desafio 3: Caixa de nome estilizada

Enunciado:

Peça ao usuário que digite seu nome e exiba-o centralizado em uma “caixa” com *, com 30 caracteres de largura.

Dica:

Use str.center() e len() para alinhar o nome.




'''

## Solução:

# Solicita o nome do usuário
nome = input("Digite seu nome: ")
# Calcula o tamanho do nome
tamanho_nome = len(nome)
print("*"*30) # Exibe a parte superior da caixa com 30 asteriscos
print(nome.center(30))
print("*"*30) # Exibe o nome centralizado


# Cria a caixa com * e centraliza o nome
