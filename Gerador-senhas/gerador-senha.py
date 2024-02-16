import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

comprimento = int(input("Digite o comprimento da senha desejada: "))
senha = gerar_senha(comprimento)
print("A senha gerada é:",senha)