largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
litros = area / 2
print("Sua parede tem a area de {:.2f}m2. Para pintar sua parede e necessario {:.2f}L de tinta. ".format(area, litros))