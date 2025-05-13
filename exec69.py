contmaior = contmulher = conthomem = 0

while True:
    print('='*30)
    print('   CADASTRE UMA PESSOA')
    print('='*30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        contmaior += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and sexo < 20:
        contmulher += 1

    print('-'*30)
    continuar = ' '
    while continuar not in 'SM':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break

print(f'Total de pessoas com mais de 18 anos: {contmaior}')
print(f'Total de homens cadastrados: {conthomem}')
print(f'Total de mulheres com menos de 20 anos: {contmulher}')