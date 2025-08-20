palavra = input("Digite uma palavra: ")

vogais = 0
for letra in palavra:
    if letra in ["a", "e", "i", "o", "u"]:
        vogais += 1

print("Quantidade de vogais:", vogais)
