# calculadora.py
# Projeto simples de calculadora em Python

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("=== Calculadora Simples ===")
print("Operações disponíveis: +  -  *  /")

while True:
    n1 = input("\nDigite o primeiro número (ou 'sair' para encerrar): ")
    if n1.lower() == "sair":
        print("Encerrando a calculadora...")
        break

    n2 = input("Digite o segundo número: ")
    operacao = input("Escolha a operação (+, -, *, /): ")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Por favor, digite apenas números!")
        continue

    if operacao == "+":
        resultado = somar(n1, n2)
    elif operacao == "-":
        resultado = subtrair(n1, n2)
    elif operacao == "*":
        resultado = multiplicar(n1, n2)
    elif operacao == "/":
        resultado = dividir(n1, n2)
    else:
        print("Operação inválida!")
        continue

    print("Resultado:", resultado)
