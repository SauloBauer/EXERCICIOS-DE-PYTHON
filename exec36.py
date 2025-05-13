vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = vcasa / (anos * 12)
minimo = salario * 30 / 100

if prestacao >= minimo:
    print('Infelizmente NÃO será possível a realização do seu empréstimo, pois a prestação excedeu 30% do seu salário.')
else:
    print('Parabéns seu empréstimo foi APROVADO')