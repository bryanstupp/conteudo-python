nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

nts = nota1 + nota2
media = nts / 2
if media >= 7:
    print("Você está aprovado")
elif media <= 7:
    print("Você está reprovado")
if media == 10:
    print("Vocé é aluno destaque")