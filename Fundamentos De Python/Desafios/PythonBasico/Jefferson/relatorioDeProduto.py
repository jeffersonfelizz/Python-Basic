'''
Desafio 6: Relatório de produto

Enunciado:

Crie um programa que solicite o nome de um produto, sua quantidade e o preço unitário.
Em seguida, exiba um relatório formatado, como:


Produto.....: Caneta
Quantidade..: 10
Total.......: R$ 25.00


Dica:
Use .format() ou f-strings com alinhamento e formatação numérica.




'''
produto = str(input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade: "))
precoUnitario = float(input("Digite o preço unitário: "))
precoTotal = quantidade * precoUnitario

print(f'----------\nRelatório de Produto\n----------\nProduto: {produto}\nQuantidade: {quantidade}\nPreço Unitario: R${precoTotal:.2f}')