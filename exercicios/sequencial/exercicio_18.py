tam = float(input("digite o tamanho do arquivo para download em megas:"))
vel = float(input("digite a velocidade da internet em mbps: "))
r = tam * vel
r1 = r / 60
print("O tempo de espera é:",r1,"minutos")
