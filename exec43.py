peso = float(input('Digite o seu Peso (Kg): '))
altura = float(input('Digite sua Altura (m): '))
imc = peso / (altura**2)
print('O IMC desta pessoa é {:.1f}: '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MORBIDA!')