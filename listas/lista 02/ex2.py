mes = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
a = int(input('digite o numero do mes: '))
if a < 0 or a > 12:
    raise ValueError('o numero tem que ser um inteiro entre 1 e 12')

if a <= 3:
    trimestre = "primeiro"
elif a <= 6:
    trimestre =  "segundo"
elif a <= 9:
    trimestre = 'terceiro'
else:
    trimestre = "quarto"

print(f'o mês de {mes[a-1]} está no {trimestre} trimestre')