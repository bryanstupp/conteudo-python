valor1 = int(input("Digite um número inteiro:"))
valor2 = int(input("Digite outro número inteiro:"))

soma = 0

for numero in range(valor1+1,valor2):
    print(numero,end=",")
    soma = soma + numero

print(f"A soma é {soma}")