#exercicio2
#Estruturas Condicionais Simulando um Classificador 
#Simule um "classificador de risco de credito".O sistema de pedir:Renda mensal;score de credito;
# possui restrição(sim/não).Regras:Se score >700 e sem restrição ->aprovado;Se score entre 500 e 700 ->Analise manual;
#caso contrário ->negado

renda_mensal = float(input("Digite a renda mensal: "))
score_credito = int(input("Digite o score de crédito: "))
restricao = input("Possui restrição? (sim/não): ")

if score_credito > 700 and restricao == "não":
    print("Aprovado.")
    #== comparação, > maior que, < menor que, >= maior ou igual, <= menor ou igual, != diferente
    #and operador lógico para combinar condições, or operador lógico para ou, not operador lógico para negação
    #=== (compara valor e tipo)operador de identidade para verificar se duas variáveis são o mesmo objeto, is not operador de identidade para verificar se duas variáveis não são o mesmo objeto
elif 500 <= score_credito <= 700:
    print("Análise manual.")
else:
    print("Negado.")