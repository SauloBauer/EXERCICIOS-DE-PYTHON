from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('''O atleta tem {} anos.
Classificação: MIRIM'''.format(idade))
elif idade <= 14:
    print('''O atleta tem {} anos.
Classificação: INFANTIL'''.format(idade))
elif idade <= 19:
    print('''O atleta tem {} anos.
Classificação: JÚNIOR'''.format(idade))
elif idade <= 25:
    print('''O atleta tem {} anos.
Classificação: SÊNIOR'''.format(idade))
else:
    print('''O atleta tem {} anos.
Classificação: MASTER'''.format(idade))