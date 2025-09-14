distancia = float(input("Digite a distância em quilometros: "))
tempo = float(input("Digite o tempo em horas: "))
velocidade = distancia / tempo
dismilhas = distancia * 0.621371
print('A velocidade média é de {:.2f} km/h'.format(velocidade))
print('A velocidade média é de {:.2f} milhas/h'.format(dismilhas))
