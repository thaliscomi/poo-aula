# questão 1
a = int(input())
b = int(input())

if a >= b:
    if a == b:
        print('números iguais')
    else:
        print(f'maior = {a}')
else:
    print(f'maior = {b}')