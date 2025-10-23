comb = str(input("Digite o tipo de combustível em: A para alcool e G para gasolina:"))
litroal = 6.29 * comb
if comb == "A":
    print("Você escolheu alcool!")


elif "A" <= 20:
    pct = 0.03 * 6.29
    d1 = litroal - pct
    print("Você vai pagar R$",d1)
elif "A" >= 20:
    pct1 = 0.03 * 6.29
    d2 = litroal - pct1
    print("Você vai pagar R$",d2)

