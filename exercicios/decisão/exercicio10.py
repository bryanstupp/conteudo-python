p = str(input("Digite o período que você estuda, digite M para matutino e V para vespertino e N para noturno: "))

if p == "v" :
    print("Vespertino escolhido!")
elif p == "m":
    print("matutino escolhido!")
elif p == "n":
    print("noturno escolhido!")
else:
    print("Valor inválido")

if p == "v" :
    print("Boa tarde!")
elif p == "m":
    print("Bom dia!")
elif p == "n":
    print("Boa noite")
