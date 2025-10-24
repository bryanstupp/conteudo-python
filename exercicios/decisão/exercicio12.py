horas = int(input("Digite a quantidade de horas trabalhadas: "))
valor = int(input("Digite o valor por horas: "))
slbruto = horas * valor
ir = 0.05 * slbruto
inss = 0.1 * slbruto
fgts = 0.11 * slbruto

if slbruto <= 900:
    print("Salário bruto :",slbruto)
    print("Imposto de renda(0%)")
elif slbruto >= 901 and slbruto <= 1500  :
    print("Salário bruto :", slbruto)
    print("Imposto de renda(5%)")
elif slbruto >= 1501 and slbruto <= 2500  :
    print("Salário bruto :", slbruto)
    print("Imposto de renda(10%)")
elif slbruto >= 2501:
    print("Salário bruto :", slbruto)
    print("Imposto de renda(20%)")

