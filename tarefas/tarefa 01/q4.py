a = input().split(',')
soma = 0
for i in range(1, len(a)+1):
    soma = soma + int(a[i-1])
print(soma)
