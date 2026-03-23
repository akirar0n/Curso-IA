alturas = [1.52, 1.68, 1.75, 1.83, 1.60, 1.71, 1.90, 1.55, 1.78, 1.65,
            1.88, 1.57, 1.73, 1.82, 1.63, 1.95, 1.70, 1.58, 1.85, 1.66]

media = sum(alturas) / len(alturas)
maior = max(alturas)   
menor = min(alturas)
desvio_simples = maior - menor

print('Média de altura: ', round(media, 2))
print('Altura máxima: ', maior)
print('Altura mínima: ', menor)
print('Amplitude: ', round(desvio_simples, 2))