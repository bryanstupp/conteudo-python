valor = 10
while valor > 0:
    print(valor)
    valor = valor - 1

saque = -1
while saque < 0 or saque > 600:
    print("Digite um valor entre 0 e 600")
    saque = int(input("Digite o valor a ser sacado: "))

alunos = ["Anna Westphal,","Kauany","Chaiane","Nicolas","Arthur"]

for aluno in alunos:
    print(f"Olá {aluno}")

    #for aluno in alunos:
    #    print(f"Olá {aluno}")

    for indice in range(0,5):
        print(f"DIzendo olá para o aluno no índice {indice}")
        print(f"Olá {alunos[indice]}")

    for letra in "NILSON":
        print(letra)