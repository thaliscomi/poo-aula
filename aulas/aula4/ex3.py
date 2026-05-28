# questão 3
a = input()

soma = 0
for c in a:
    if c.isdigit():
        soma += int(c)
print(soma)