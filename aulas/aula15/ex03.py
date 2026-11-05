try:
    a = int(input('informe o dividendo: '))
    b = int(input('informe o divisor: '))
    print(a/b)
except ValueError as erro:
    print(erro)
finally:
    print('Ok')
print('Fim')