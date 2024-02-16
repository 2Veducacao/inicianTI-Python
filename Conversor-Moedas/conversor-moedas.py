def converter_moeda(valor, taxa):
    return valor * taxa

valor = float(input("Digite o valor em sua moeda: "))
taxa = float(input("Digite a taxa de conversão: "))
resultado = converter_moeda(valor, taxa)
print("O valor convertido é:",resultado)