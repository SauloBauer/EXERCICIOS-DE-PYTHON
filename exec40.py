nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota1 + nota2) / 2
print('Com {:.2f} e {:.2f}, a média é {}'.format(nota1, nota2, m))
if m >= 7:
    print('PARABÉNS! O ALUNO FOI APROVADO!')
elif m >= 5:
    print('0 ALUNO ESTÁ DE RECUPERAÇÃO!')
else:
    print('O ALUNO ESTÁ REPROVADO!')