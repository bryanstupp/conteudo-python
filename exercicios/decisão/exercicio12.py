horas = int(input("Digite a quantidade de horas trabalhadas: "))
valor = int(input("Digite o valor por horas: "))
slbruto = horas * valor
if slbruto <= 900:
    print("Salário bruto :",slbruto)
    print("Imposto de renda(0%)")
    