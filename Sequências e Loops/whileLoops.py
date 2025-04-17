# While é um loop que executa um bloco de código enquanto uma condição for verdadeira.
# O loop while é útil quando não sabemos quantas vezes o loop deve ser executado.
# O loop while continua a executar o bloco de código enquanto a condição for verdadeira.
# Quando a condição se torna falsa, o loop para de executar
# e o programa continua com o próximo bloco de código após o loop.

n = 0
while n < 5:
    print(n)
    n += 1  # Incrementa n em 1 a cada iteração do loop
    if n >= 3:
        print("O loop parou porque n é maior ou igual a 5.")
        break
    else:
        print("O loop continua porque n é menor que 5.")
        continue # O loop continua a executar enquanto n for menor que 5
    