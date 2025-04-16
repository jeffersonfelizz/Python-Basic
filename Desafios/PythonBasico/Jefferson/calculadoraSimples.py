'''

Desafio 2: Calculadora simples

Enunciado:

Peça dois números ao usuário e mostre a soma, subtração, multiplicação e divisão formatadas em uma única saída.

Dica:
Converta os valores com float() e use f-string ou .format() para a formatação.


'''

# Solicita ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
multiplicacao = num1 * num2
subtracao = num1 - num2
divisao = num1 / num2

print(f"A soma é: {soma} \nA Subtração é: {multiplicacao}\n A Multiplicação é: {subtracao}\n A divisão é: {divisao}\n")
