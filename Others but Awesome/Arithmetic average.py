ArrX = []
y = 0
z = 0

def decimal(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


while True:
    x = input("Ingresa un numero \n")
    if x == "N":
        print("\n")
        break
    ArrX.append(int(x))

nM = len(ArrX)
i = tuple(ArrX)

for n in ArrX:
    y = n + y

MA = decimal(y / nM)

print(f"La M.A es: {MA}")

for n in i:
    z = abs(n - MA) + z

MD = decimal(z / nM)

print(f"La M.D es: {MD}")
