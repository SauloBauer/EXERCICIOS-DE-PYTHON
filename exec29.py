velocidade = float(input('Qual a velocidade atual carro? '))
multa = (velocidade-80)*7
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h, Você deve pagar uma multa de R${:.2f}' .format(multa))
print('Continue assim, tenha um ótimo dia!')