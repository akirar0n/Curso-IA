from collections import deque

def executar_entregador(grafo, inicio):
    fila = deque([inicio])
    visitados = set([inicio])
    
    print("\n --- INICIANDO BFS (VARREDURA POR NÍVEL) ---")
    
    while fila:
        local_atual = fila.popleft()
        print(f"Entregando em: {local_atual}")
        
        for vizinho in grafo[local_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    print("\n" + "-"*50)
    
def executar_dfs_software(grafo, etapa, rastro=None):
    if rastro is None:
        rastro = []
        rastro.append(etapa)
        print(f"Analizando trilha: {'->'.join(rastro)}")
        
    if not grafo[etapa]:
        print(f"SUCESSO! Objetivo encontrado no fim da linha: {etapa}")
            
        return True
        
    for proxima in grafo[etapa]:
        if executar_dfs_software(grafo, proxima, list(rastro)):
            return True
        return False
        
mapa_entregas = {
    'CD Logístico': ['Rua A', 'Rua B', 'Rua C'],
    'Rua A': ['Casa 1'],
    'Rua B': [],
    'Rua C': [],
    'Casa 1': []
}

mapa_software = {
    'Nova Ideia': ['n8n', 'Código'],
    'n8n': ['Crias os nós'],
    'Código': ['Configurar NextJS'],
    'Criar os nós': [],
    'Configurar NextJS': []
}

if __name__ == "__main__":
    executar_entregador(mapa_entregas, 'CD Logístico')
    print("\n" + "-"*50)
    print("\n --- INICIANDO DFS (MERGULHO PROFUNDO) ---")
    executar_dfs_software(mapa_software, 'Nova Ideia')