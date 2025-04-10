numero = int(input('Digite o número da tabuada:'))

for m in range(1,11):
    print(f'{numero} x {m} = {numero * m}')

print('---- Solução com WHILE ----')
ciclos = 1

while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    # Incremento
    ciclos += 1