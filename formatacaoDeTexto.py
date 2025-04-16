# Formatação de Texto em Python 

# Formatação de Texto em Python Maiscula e Minúscula
print("Texto em Maiúscula".upper()) # Converte o texto para maiúscula

# .lower() - Formatação de Texto em Python
print("Texto em Minúscula".lower()) # Converte o texto para minúscula

# .capitalize() - Formatação de Texto em Python
print("Texto em Capitalize".capitalize()) # Converte a primeira letra do texto para maiúscula

# .title() - Formatação de Texto em Python
print("Texto em Title".title()) # Converte a primeira letra de cada palavra do texto para maiúscula

# .swapcase() - Formatação de Texto em Python
print("Texto em Swapcase".swapcase()) # Converte o texto para maiúscula e minúscula alternadamente

# .format() - Formatação de Texto em Python # MENOS USADA
print("Texto em {} e {}".format("Python", "Java")) # Formata o texto com as variáveis

# f'' - Formatação de Texto em Python # MAIS USADA ......
Python = "Python" # Variável Python
Java = "Java" # Variável Java

print(f"Texto em {Python} e {Java}" )# Formata o texto com as variáveis

# Split 
# .split() - Formatação de Texto em Python
print("Texto em Python".split()) # Divide o texto em uma lista de palavras

#Replace
# .replace() - Formatação de Texto em Python
print("Texto em Python".replace("Python", "Java")) # Substitui a palavra Python por Java no texto

# Strip
# .strip() - Formatação de Texto em Python
print(" Texto em Python ".strip()) # Remove os espaços em branco do início e do fim do texto

# str.center # .center() - Formatação de Texto em Python
print("Texto em Python".center(20)) # Centraliza o texto em um espaço de 20 caracteres

# len # .len() - Formatação de Texto em Python
print(len("Texto em Python")) # Retorna o tamanho do texto

# .count() - Formatação de Texto em Python
print("Texto em Python".count("Python")) # Conta o número de vezes que a palavra Python aparece no texto
