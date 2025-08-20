import random
numero = 10
palpite = int(input("Tente adivinhar o número: "))
if palpite > numero:
    print("Menor")
elif palpite < numero:
    print("Maior")
else:
    print("Acertou!")
