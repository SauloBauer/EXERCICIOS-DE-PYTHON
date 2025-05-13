frase = str(input('Escreva uma frase: ')).strip().upper()# strip tira os espaços e upper deixa miusculo
palavras = frase.split()#separa por palavras
junto = ''.join(palavras)#juntar as palavras separadas
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')