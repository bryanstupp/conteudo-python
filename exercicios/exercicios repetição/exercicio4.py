pa = int(input("digite a quantidade de habitantes do país A:"))
pb = int(input("digite a quantidade de habitantes do país B:"))
taxaa = float(input("Digite a porcentagem do crescimento dp país A:"))
taxab = float(input("Digite a porcentagem do crescimento dp país B:"))
anos = 0
taxaa = taxaa/100 +1
taxab = taxab/100 +1
while taxaa < taxab:
    print("valor inválido,A do país A deve ser maior.")
    taxaa = float(input("Digite a porcentagem do crescimento dp país A:"))
    taxab = float(input("Digite a porcentagem do crescimento dp país B:"))
while pa < pb:
    pa =pa * taxaa
    pb =pb * taxab
    anos = anos + 1
print(f"Foram necessarios {anos} anos para o país A passar o país B")
