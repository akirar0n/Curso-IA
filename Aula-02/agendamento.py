# Agendamento (Aula 02)

# Problema
# 2 SALAS
# 2 PROFESSORES
# 2 HORÁRIOS

from collections import deque
from itertools import product

professores = ["P1", "P2"]
salas = ["Sala 1", "Sala 2"]
horarios = ["8h", "10h"]

def estado_inicial():
    return{}

def valido(estado):
    ocupacao = {}

    for professor, (sala, horario) in estado.items():
        if (sala, horario) in ocupacao:
            return False
        ocupacao[(sala, horario)] = professor

    return True  

def gerar_estados(estado):
    novos_estados = []

    nao_alocados = [p for p in professores if p not in estado]

    if not nao_alocados:
        return []

    professor = nao_alocados[0]

    for sala, horario in product(salas, horarios):
        novo_estado = estado.copy()
        novo_estado[professor] = (sala, horario)

        if valido(novo_estado):
            novos_estados.append(novo_estado)

    return novos_estados

    
def bfs():
    fila = deque([estado_inicial()])

    while fila:
        estado = fila.popleft()

        if len(estado) == len(professores):
            return estado

        for proximo in gerar_estados(estado):
            fila.append(proximo)

    return None

solucao = bfs()

if solucao:
    print("Solução encontrada:\n")
    for prof, (sala, horario) in solucao.items():
        print(f"{prof} -> {sala} às {horario}")
else:
    print("Nenhuma solução encontrada")