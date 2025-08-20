valor = int(input("Digite o valor: "))

notas1 = valor // 1
valor = valor % 1

notas2 = valor // 2
valor = valor % 2

notas5 = valor // 5
valor = valor % 5

notas10 = valor // 10
valor = valor % 10

notas20 = valor // 20
valor = valor % 20

notas50 = valor // 50
valor = valor % 50

notas100 = valor // 100
valor = valor % 100

print("100:", notas100)
print("50 :", notas50)
print("20 :", notas20)
print("10 :", notas10)
print("5  :", notas5)
print("2  :", notas2)
print("1  :", notas1)
