salario = float(input('Qual o salário do empregado? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com o novo reajuste de 15%, agora ele ganhará R${:.2f}'.format(salario, novo))