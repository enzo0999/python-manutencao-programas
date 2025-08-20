numeros = []

for i in range(5):
    valor = int(input("Digite um número: "))
    numeros.append(valor)

busca = int(input("Digite o número que deseja buscar: "))

encontrado = False
for n in numeros:
    if n == busca:
        encontrado = True
        print("Número encontrado!")

if not encontrado:
    print("Número não encontrado")
