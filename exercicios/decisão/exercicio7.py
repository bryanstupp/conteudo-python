n1 = float(input("digite o primeiro número: "))
n2 = float(input("digite o segundo número: "))
n3 = float(input("digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("número 1 é o maior",n1)
elif n2 > n1 and n2 > n3:
    print("o número maior é", n2)
else:
    print("o número maior é", n3)

n1 = float(input("digite o primeiro número: "))
n2 = float(input("digite o segundo número: "))
n3 = float(input("digite o terceiro número: "))

if n1 < n2 and n1 < n3:
    print("o menor número é",n1)
elif n2 < n1 and n2 < n3:
    print("o número menor é", n2)
else:
    print("o número menor é", n3)