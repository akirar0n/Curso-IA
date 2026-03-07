#Exercicio02(agendamento) [CSB]
#Problema:2 salas;2 professores ;2horarios.
#Modelar:representação do estado,função que verifica conflitos

from collections import deque
from itertools import product  
#biblioteca para criar filas e para criar combinações de elementos

# -----------------------------
# Domínio do problema
# -----------------------------

professores = ["P1", "P2"]
salas = ["Sala1", "Sala2"]
horarios = ["8h", "10h"]

# -----------------------------
# Representação de Estado
# -----------------------------
# Um estado é um dicionário:
# {
#   "P1": ("Sala1", "8h"),
#   "P2": ("Sala2", "10h")
# }

def estado_inicial():
    return {}

# -----------------------------
# Função de Validação
# -----------------------------

def valido(estado):
    ocupacao = {}

    for professor, (sala, horario) in estado.items():
        if (sala, horario) in ocupacao:
            return False
        ocupacao[(sala, horario)] = professor

    return True

# -----------------------------
# Geração de Novos Estados
# -----------------------------

def gerar_estados(estado):
    novos_estados = []

    # Próximo professor a ser alocado
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

# -----------------------------
# Busca BFS
# -----------------------------

def bfs():
    fila = deque([estado_inicial()])

    while fila:
        estado = fila.popleft()

        # Se todos professores foram alocados
        if len(estado) == len(professores):
            return estado

        for proximo in gerar_estados(estado):
            fila.append(proximo)

    return None

# -----------------------------
# Execução
# -----------------------------

solucao = bfs()

if solucao:
    print("Solução encontrada:\n")
    for prof, (sala, horario) in solucao.items():
        print(f"{prof} -> {sala} às {horario}")
else:
    print("Nenhuma solução encontrada.")