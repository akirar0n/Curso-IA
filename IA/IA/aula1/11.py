#exercicio3
#Listas e Estatistica Basica
#Crie uma lista com 20 valores,simulando alturas de pessoas.Depois:calcule média,maior valor,menor valor,desvio simples(max-min)

#lista de alturas de pessoas
alturas = [1.70, 1.65, 1.80, 1.75, 1.60, 1.85, 1.90, 1.55, 1.68, 1.72, 1.78, 1.82, 1.66, 1.74,1.88, 1.77, 1.62, 1.83, 1.79, 1.67]

media = sum(alturas) / len(alturas)
maior = max(alturas)
menor = min(alturas)
desvio_simples = maior - menor

print(f"Média das alturas: {media:.2f}")
print(f"Maior altura: {maior}")
print(f"Menor altura: {menor}")
print(f"Desvio simples (max - min): {round(desvio_simples, 2)}")