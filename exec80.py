lista = []
for c in range(0, 5):#Questão pede somente 5 numeros
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:#se o numero for o primeiro digitado OU numero digitado for maior que o ultimo, adiciona ao final
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else: #se não
        pos = 0 #posição é 0
        while pos < len(lista): #enquanto posição for menor que o ultimo numero da lista.
            if n <= lista[pos]: #Entra no IF, Se (n) for menor ou igual a lista de posição.
                lista.insert(pos, n) #adicione na lista a posição 0 e o numero digitado.
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('='*50)
print(f'Os valores digitados foram {lista}')
