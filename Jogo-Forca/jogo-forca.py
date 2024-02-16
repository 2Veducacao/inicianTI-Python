import random

palavras = ['python', 'programacao', 'computador', 'codigo', 'desenvolvimento']
palavra = random.choice(palavras)
letras_certas = []
tentativas = 6

print("Bem-vindo ao jogo da forca!")
print("_ " * len(palavra))

while tentativas > 0:
    letra = input("Digite uma letra: ").lower()
    if letra in palavra:
        letras_certas.append(letra)
        print("Letra correta!")
    else:
        tentativas -= 1
        print(f"Letra errada! Você tem {tentativas} tentativas restantes.")

    # Mostrar letras corretas e traços para letras ainda não descobertas
    for letra_palavra in palavra:
        if letra_palavra in letras_certas:
            print(letra_palavra, end=' ')
        else:
            print('_', end=' ')

    # Verificar se o jogador venceu
    if set(palavra) == set(letras_certas):
        print("\nParabéns! Você ganhou!")
        break
else:
    print("\nVocê perdeu! A palavra correta era:",palavra)