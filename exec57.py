sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFm':
    sexo = str(input('Sexo inválido, Tente novamente:')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))