alcool = 4.17
gaso= 6.29

litros = int(input("Escreva a quantidade de litros:"))
combustivel = input("Digite o combustível desejado, A para alcool e G para gasolina: ")

if combustivel == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco1 = litros * gaso
    precototal = preco1 - (desconto * preco1)
elif combustivel == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco1 = gaso * litros
    precototal = preco1 - (preco1 * desconto)

if precototal >0:
    print("Valor a pagar é:",precototal)
