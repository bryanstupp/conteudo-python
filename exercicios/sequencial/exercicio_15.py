salario = int(input("Digite quanto ganha por hora: "))
horas = int(input("digite quantas horas trabalhou no mês:"))
r1 = salario * horas
print("A- seu salário bruto é:",r1)
inss1 = 8 / 100
inss2 = inss1 * r1
print("B- pagou:",inss2,"reais no inss")
sind1 = 5 / 100
sind2 = sind1 * r1
print("C- pagou:",sind2,"reais no sindicato")
liq1 = 24 / 100
liq2 = liq1 * r1
liq3 = r1 - liq2
print("D- ficou com:",liq3,"reais de salario liquido")