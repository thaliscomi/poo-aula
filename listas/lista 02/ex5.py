a = int(input(':'))
b = int(input(':'))
c = int(input(':'))

x = 0
y = 0
z = 0

lista = [a,b,c]
for i in lista:
    if min(lista) == i:
        x += i
    elif max(lista) == i:
        z += i
    else:
        y += i

print(f'{x}, {y}, {z}')