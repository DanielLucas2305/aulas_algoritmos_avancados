notas = []

print("-------------Calculadora de médias-------------------")
print()

quantidade = int(input("Insira a quantidade de notas desejada para calculo da média: "))

for i in range(quantidade):
    nota = float(input(f"Insira a {i+1}ª nota: "))
    notas.append(nota)

print("As notas inseridas foram:",notas)

flag_notas = 0

for i in notas:
    flag_notas += i

media = flag_notas / len(notas)

print("A média final é igual: ", f"{media:.2f}")