a = int(input('num:'))
b = int(input('num:'))
c = int(input('num:'))
d = int(input('num:'))

pares = 0

impares = 0

for i in a,b,c,d:
    if i%2 == 0:
        pares += i
    else:
        impares += i

print(f'soma dos pares: {pares}')
print(f'soma dos impares: {impares}')