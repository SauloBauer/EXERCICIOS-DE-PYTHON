soma = 0
for c in range(1, 7):
    n = int(input('Digite O {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é: {}'.format(soma))
