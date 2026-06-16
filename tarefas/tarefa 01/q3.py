a = input()
soma = 0
for i in a:
    if i.isdigit():
        soma = soma + int(i)

print(soma)