numero = int(input('Digite o seu número de celular sem o DDD: '))

if numero >= 10:
    print(' ')
else:
    print('Quantidade de números correta')

if numero[0] == 9:
    print('Correto')
else:
    print('O número não começa com o dígito 9')
