largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
tinta = area / 2
precotinta = tinta * 35

print("A área da parede é de {:.2f} m²".format(area))
print("Você vai precisar de {:.2f} L de tinta".format(tinta))
print("O custo da tinta será R$ {:.2f}".format(precotinta))
