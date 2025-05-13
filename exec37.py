numero = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão. 
Digite ( 1 ) para binário 
Digite ( 2 ) para octal 
Digite ( 3 ) para hexadecimal''')
base = int(input('Sua Opção: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero [2:])))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero [2:])))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero [2:])))
else:
    print('OPÇÃO INVÁLIDA')