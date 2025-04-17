# O loop for é uma maneira eficiente de iterar sobre sequências em Python, como listas, tuplas e strings.
# Ele permite que você execute um bloco de código para cada item na sequência, sem precisar usar um índice ou contador manualmente.
# Isso torna o código mais legível e menos propenso a erros.
# Além disso, o loop for pode ser combinado com outras estruturas de controle, como condicionais e funções, para criar soluções mais complexas.
# O loop for é uma das estruturas de controle mais comuns em Python e é amplamente utilizado em programação.


# O loop for percorre cada elemento da lista valores e imprime o valor atual.
valores = [1, 2, 3, 4, 5]
for valor in valores:
    print(valor)
    

nome = "Lucas"
for letra in nome:
    print(letra)

lista = [[1,2,3,4,5],[6,7,8,9,10]]
for sublista in lista:
    for valor in sublista:
        print(valor)

# dicionário em Python
clientes = {
    "nome": "Lucas",
    "idade": 30,
    "cidade": "São Paulo"
} 
# for itera sobre o dicionário clientes e imprime a chave e o valor correspondente
for chave,valor in clientes.items(): # itera sobre o dicionário clientes e imprime a chave e o valor correspondente
    print(f"{chave}: {valor}")

cliente = [
    ("Lucas", 30, "São Paulo"),
    ("Maria", 25, "Rio de Janeiro"),
    ("João", 35, "Belo Horizonte"),
    ("Ana", 28, "Curitiba"),
]
for nome, idade, cidade in cliente:
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")