"""
Neste exercício, a coordenação do curso precisa organizar a escala de monitoria do
laboratório, e você atuará como o responsável por esta elaboração

• 3 monitores: M1, M2, M3
• 2 salas: Lab1, Lab2
• 2 horários: 14h, 16h

Regras
1. Cada monitor deve ser alocado em exatamente uma sala e um horário.
2. Não pode haver dois monitores na mesma sala no mesmo horário.
3. O monitor M1 não pode atuar às 16h.
4. O monitor M3 só pode atuar no Lab2.
"""

from collections import deque
from itertools import product

monitores = ["Monitor 1", "Monitor 2", "Monitor 3"]
laboratorios = ["Lab1", "Lab2"]
horarios = ["14h", "16h"]

def estado_inicial():
    return {}

def valido(estado):
    ocupacao = {}

    for monitor, (laboratorio, horario) in estado.items():
        if (laboratorio, horario) in ocupacao:
            return False
        ocupacao[(laboratorio, horario)] = monitor

        if monitor == "M1" and horario == "16h":
            return False

        if monitor == "M3" and laboratorio != "Lab 2":
            return False
        
    return True

def gerar_estados(estado):
    novos_estados = []

    nao_alocados = [m for m in monitores if m not in estado]

    if not nao_alocados:
        return []
    
    monitor = nao_alocados[0]

    for laboratorio, horario in product(laboratorios, horarios):
        novo_estado = estado.copy()
        novo_estado[monitor] = (laboratorio, horario)

        if valido(novo_estado):
            novos_estados.append(novo_estado)

    return novos_estados

def bfs():
    fila = deque([estado_inicial()])

    while fila:
        estado = fila.popleft()

        if len(estado) == len(monitores):
            return estado
        
        for proximo in gerar_estados(estado):
            fila.append(proximo)

    return None

solucao = bfs()

if solucao:
    print("Solução encontrada: \n")
    for mon, (laboratorio, horario) in solucao.items():
        print(f"{mon} -> {laboratorio} às {horario}")
else:
    print("Nenhuma solução encontrada")