peso = 50
multa_kg = 4

peso_peixe = float(input("Informe o peso total: "))

excedente = peso_peixe - peso
multa = excedente * multa_kg

print("Houveram",excedente,"Kg de peixe a mais permitido")

print("O valor da multa é R$",multa)
