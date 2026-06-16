a = [int(input()),int(input()),int(input()),int(input())]
b = a.copy()

for z in b:
    b.remove(z)
    if z in b:
        raise ValueError('os valores precisam ser diferentes')
    b = a.copy()

print(max(a))
print(min(a))
a.remove(max(a))
a.remove(min(a))

print(min(a)+max(a))