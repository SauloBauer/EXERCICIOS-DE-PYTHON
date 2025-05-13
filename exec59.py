from time import sleep
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
print('-='*40)
escolha = 0
while escolha != 5:
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    sleep(1)
    escolha = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>> Qual a sua opção? '))
    print('-=' * 40)
    sleep(2)
    if escolha == 1:
        soma = a + b
        print('A soma de {} + {} é: {}'.format(a, b, soma))
    elif escolha == 2:
        soma = a * b
        print('A multiplicação entre os números {} * {} = {}'.format(a, b, soma))

    elif escolha == 3:
        maior = 0
        if a > b:
            maior = a
        else:
            maior = b
        print('O maior número entre {} e {} é: {}'.format(a, b, maior))
    elif escolha == 4:
        print('Informe os números novamente')
        a = int(input('Primeiro Valor: '))
        b = int(input('Segundo Valor: '))
    elif escolha == 5:
        print('Finaliando...')
    else:
        print('Opção inválida, tente novamente...')
    print('-='*40)
    sleep(3)
print('FIM DO PROGRAMA!')
