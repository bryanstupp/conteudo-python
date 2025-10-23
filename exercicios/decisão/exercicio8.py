p1 = input("Digite o preço do primeiro produto: ")
p2 = input("Digite o preço do segundo produto: ")
p3 = input("Digite o preço do terceiro produto: ")

if p1 < p2 and p1 < p3:
    print("Você deve comprar o primeiro produto pois ele é mais barato")
elif p2 < p1 and p2 < p3:
    print("Você deve comprar o segundo produto pois ele é mais barato")
else:
    print("Você deve comprar o terceiro produto pois ele é mais barato")