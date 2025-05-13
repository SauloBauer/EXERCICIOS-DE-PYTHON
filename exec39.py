from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já passou da hora de se alistar! já tem {} anos que deveria ter feito isso!'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda vai se alistar! Faltam {} anos'.format(saldo))
    print('Será em {} seu alistamento!'.format(ano))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')