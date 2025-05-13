print('=-=-=-=-=-=-LOJAS GUANABARA=-=-=-=-=-=-=-')
preco = float(input('Preço das Compras: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] Á VISTA Dinheiro/Cheque
[ 2 ] Á VISTA Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if pagamento == 1:
   total = preco - (preco * 10) / 100
elif pagamento == 2:
    total = preco - (preco * 5) / 100
elif pagamento == 3:
    total = preco
elif pagamento == 4:
    total = preco + (preco * 20) / 100
else:
    total = 0
    print('\033[1;31;40m OPÇÃO INVÁLIDA \033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))