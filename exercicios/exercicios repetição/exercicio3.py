pa = 80000
pb = 200000
anos = 0

while pa < pb:
    pa =pa * 1.03
    pb =pb * 1.015
    anos = anos + 1
print(f"Foram necessarios {anos} anos para o país A passar o país B")