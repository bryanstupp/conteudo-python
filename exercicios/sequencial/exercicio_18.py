tam = float(input("digite o tamanho do arquivo para download em megas:"))
vel = float(input("digite a velocidade da internet em mbps: "))
r = tam * vel
r1 = r / 60
r2 = r1 / 60
print("O tempo de espera é:",r2,"minutos")
