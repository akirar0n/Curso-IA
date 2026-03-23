# DEFINICAO DE MERCADO
# LISTAR 20 CARACTERISTICAS DE POSTS VIRAIS
# *CTA = Call To Action

import random

NOMES_CARACTERISTICAS = [
    "QUALIDADE 4K", "VIDEO CURTO", "LEGENDA CURTA", "USO DE HASHTAG TREND",
    "AUDIO VIRAL", "CORES VIBRANTES", "PRESENÇA DE ROSTO HUMANO", "*CTA", 
    "LEGENDA EMBUTIDA", "POSTADO EM HORARIO DE PICO", "COLLAB COM OUTRO PERFIL",
    "RESPONDE AOS COMENTARIOS", "USO DE ENQUETE", "THUMB ATRAENTE", 
    "TEMA QUE DESPERTA CURIOSIDADE", "HUMOR OU ENTRETENIMENTO",
    "TUTORIAL/EDUCATIVO", "CENARIO ESTETICO", "CORTE RAPIDO EDICAO",
    "TRILHA SONORA SINCRONIZADA"
]

ALVO_VIRAL = [1] * len(NOMES_CARACTERISTICAS)

TAMANHO_POPULACAO = 20
MAX_GERACOES = 100
TAXA_MUTACAO = 0.1

def criar_post_aleatorio():
    return[random.randint(0,1) for _ in range(20)]    

post_teste = criar_post_aleatorio()

print(f"Post Teste: {post_teste}")

# FITNESS - QUÃO PARECIDO É COM O INDIVÍDUO IDEAL
def calcular_engajamento(post):
    return sum(1 for p, a in zip(post, ALVO_VIRAL) if p == a)

print(f"Engajamento teste: {calcular_engajamento(post_teste)}")

# CROSSOVER
def fusao_de_post(pai1, pai2):
    ponto = random.randint(1,10)
    return pai1[:ponto] + pai2[ponto:]

post_teste2 = criar_post_aleatorio()
# print(f"Post Teste: {post_teste2}")
# print(f"Engajamento teste 2: {calcular_engajamento(post_teste2)}")

# print(f"Fusão Teste: {fusao_de_post(post_teste, post_teste2)}")

# MUTACAO
def teste_de_novidade(post):
    novo_post = list(post)
    idx = random.randint(0, 19)
    novo_post[idx] = 1 - novo_post[idx]
    return novo_post

# print(f"Mutação teste: {teste_de_novidade(post_teste)}")

populacao = [criar_post_aleatorio() for _ in range(TAMANHO_POPULACAO)]

for geracao in range (MAX_GERACOES):
    populacao.sort(key=calcular_engajamento, reverse=True)
    melhor_post = populacao[0]
    nota_atual = calcular_engajamento(melhor_post)
    
    print(f"Ciclo {geracao:02d} | Melhor post atual: {nota_atual}/20 pontos")

    if nota_atual == 20:
        print(f"SUCESSO!! A formula perfeita está no ciclo {geracao}")
        break
    
    proxima_geracao = populacao[:4]
    
    while len(proxima_geracao) < TAMANHO_POPULACAO:
        p1, p2 = random.sample(populacao[:10], 2)
        filho = fusao_de_post(p1, p2)
        
    if random.random() < TAXA_MUTACAO:
        filho = teste_de_novidade(filho)
    
    proxima_geracao.append(filho)
    
populacao = proxima_geracao

for i, status in enumerate(populacao[0]):
    legenda = "[ATIVADO]" if status == 1 else "[DESCARTADO]"
    print(f"{legenda:<15} | {NOMES_CARACTERISTICAS[i]}")
    
print("="*50)

print(f"Resultado: {calcular_engajamento(populacao[0])/(len(NOMES_CARACTERISTICAS))}")