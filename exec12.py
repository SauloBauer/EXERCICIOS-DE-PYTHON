preco = float(input('Qual o preço do produto? R$'))
porcentagem = preco*5/100
resultado = preco - porcentagem
print('O produto sofreu 5% de desconto, por tanto agora ele é: R${:.2F}'.format(resultado))

