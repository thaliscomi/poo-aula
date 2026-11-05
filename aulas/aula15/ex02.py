try:
    a = int(input('informe o dividendo: '))
    b = int(input('informe o divisor: '))
    print(a/b)
except Exception as erro:
    print(type(erro))
    print(erro)