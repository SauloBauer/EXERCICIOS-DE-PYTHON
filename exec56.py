somaidade = 0
media = 0
velhohomem = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    Nome = str(input('Nome: ')).strip() # tirar os espaços.
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += Idade # (+=) significa: (somaidade = somaidade + idade).
    if p == 1 and Sexo in 'Mn':
        velhohomem = Idade
        nomevelho = Nome
    if Idade > velhohomem and Sexo in 'Mn':
        velhohomem = Idade
        nomevelho = Nome
    if Idade < 20 and Sexo in 'Ff':
        mulher += 1

media = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(velhohomem, nomevelho))
print('No grupo tem {} mulheres abaixo de 20 anos'.format(mulher))