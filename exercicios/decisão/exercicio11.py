s = int(input("Digite seu salário atual: "))
pct1 = 0.2 * s
pct2 = 0.15 * s
pct3 = 0.1 * s
pct4 = 0.05 * s

ns1 = s + pct1
ns2 = s + pct2
ns3 = s + pct3
ns4 = s + pct4
if s <= 1450:
    print("Seu salário atual é:",s)
    print("Você ganhou uma promação de 20%")
    print("O valor do aumento foi:",pct1)
    print("O seu novo salário é: ",ns1)

elif s >= 1451 and s <= 2800:
    print("Seu salário atual é:", s)
    print("Você ganhou uma promação de 15%")
    print("O valor do aumento foi:", pct2)
    print("O seu novo salário é: ", ns2)



elif s >= 2801 and s <= 3500:
    print("Seu salário atual é:", s)
    print("Você ganhou uma promação de 10%")
    print("O valor do aumento foi:", pct3)
    print("O seu novo salário é: ", ns3)



elif s >= 3501:

    print("Seu salário atual é:",s)
    print("Você ganhou uma promação de 5%")
    print("O valor do aumento foi:", pct4)
    print("O seu novo salário é: ", ns4)

