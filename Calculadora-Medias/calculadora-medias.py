def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []
while True:
    nota = input("Digite uma nota (ou 'fim' para sair): ")
    if nota.lower() == 'fim':
        break
    notas.append(float(nota))

media = calcular_media(notas)
print("A média das notas é:", media)
