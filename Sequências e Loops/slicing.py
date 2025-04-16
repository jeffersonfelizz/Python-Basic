'''
Slicing é uma técnica utilizada para acessar partes de uma sequência, como listas ou strings, em Python.
# Ela permite selecionar um intervalo de elementos de uma sequência, especificando o índice inicial e final, além de um passo opcional.
# O formato básico de um slicing é: sequencia[inicio:fim:passo].


'''
# exemplo de slicing em uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[2:5])  # Saída: [3, 4, 5] (elementos do índice 2 ao 4)
print(lista[::2])  # Saída: [1, 3, 5, 7, 9] (elementos com passo 2)
print(lista[::-1])  # Saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (lista invertida)
print(lista[5:])  # Saída: [6, 7, 8, 9, 10] (elementos do índice 5 até o final)
print(lista[:5])  # Saída: [1, 2, 3, 4, 5] (elementos do início até o índice 4)
print(lista[1:8:2])  # Saída: [2, 4, 6, 8] (elementos do índice 1 ao 7 com passo 2)
print(lista[::3])  # Saída: [1, 4, 7, 10] (elementos com passo 3)
print(lista[1:9:3])  # Saída: [2, 5, 8] (elementos do índice 1 ao 8 com passo 3)

# exemplo de slicing em uma string
string = "Python é uma linguagem de programação"
print(string[0:6])  # Saída: 'Python' (caracteres do índice 0 ao 5)
print(string[::2])  # Saída: 'Pto m igam e rgamao' (caracteres com passo 2)
print(string[::-1])  # Saída: 'amargorp ed emal gnaihtnoP' (string invertida)
