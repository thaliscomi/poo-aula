a = input()
if "+" in a:
    x, y = a.split("+")
    print(int(x)+int(y))
elif "-" in a:
    x, y = a.split("-")
    print(int(x)-int(y))
elif "/" in a:
    x, y = a.split("/")
    print(int(x)/int(y))