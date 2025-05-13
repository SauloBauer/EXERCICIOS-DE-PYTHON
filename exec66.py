n = cont = s = 0
while True:
    n = int(input('Digite um valor [999 para encerrar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números e soma entre eles é {s}')


