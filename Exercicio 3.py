produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))
preco = produto1 + produto2 + produto3
desconto = preco * 10 / 100
if preco > 100:
    final = preco - desconto
    print('O valor do desconto é R$ {:.2f}'.format(desconto))
    print("O preço com desconto é R$ {:.2f}".format(final))
else:
    final = preco
print("O preço total dos produtos é R$ {:.2f}".format(preco))

