n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
valores = (n1,n2, n3, n4)

print(f'Os números digitados foram: {valores}')
print(f'O número 9 foi digitado {valores.count(9)} vezes')
print(f'O número 3 aparaceu na posição {valores.index(3) + 1}')
print(f'Os valores digitados pares foram os: ',end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')