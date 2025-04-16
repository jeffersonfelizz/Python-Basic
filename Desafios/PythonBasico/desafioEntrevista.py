# Desafio Entrevista 
# Crie um programa que 
# - pede pelo seu nome e idade, 
nome = str(input("Qual é o seu nome? "))
idade =int(input("Qual é a sua idade? "))
# - da oi para você, 
print(f"Olá {nome}, Tudo bem?")
# - conta quantas letras seu nome possui
print(f'Seu Nome possui : {len(nome)} letras')
# Fala quantos anos você tera daqui a 5 anos 
print(f'Você terá {idade + 5} anos daqui a 5 anos')
# - quantos anos você tinha há 10 anos atrás.
print(f'Você tinha {idade - 10} anos há 10 anos atrás')