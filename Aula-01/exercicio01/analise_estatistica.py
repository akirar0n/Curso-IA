import numpy as np 

np.random.seed(42)

fator_E = np.random.randint(0, 21, 10)
fator_F = np.random.randint(0, 15, 10)

media_E = np.mean(fator_E)
desvio_E = np.std(fator_E)

print("Fator E (Tempo de Estudo):", fator_E)
print("Fator F (Faltas):", fator_F)
print("Média do tempo de estudo:", media_E)
print("Desvio padrão do tempo de estudo:", round(desvio_E, 2))

IAp = (fator_E * 0.6) - (fator_F * 0.4)

print("Índice de Aproveitamento (IAp):", IAp)

for i in range(10):
    if IAp[i] >= 7:
        diagnostico = "Alta chance de aprovação"
    elif IAp[i] >= 5:
        diagnostico = "Risco moderado de reprovação"
    else: 
        diagnostico = "Intervenção Imediata"
    
    print(f"Aluno {i+1} / Tempo de estudo: {fator_F[i]} / Faltas: {fator_E[i]} / IAp: {IAp[i]:.2f} / Diagnóstico: {diagnostico}")