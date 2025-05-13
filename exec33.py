a = int(input('Informe o Primeiro valor: '))
b = int(input('Informe o Segundo valor: '))
c = int(input('Informe o Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é o {}'.format(menor))
print('O maior valor é o {}'.format(maior))