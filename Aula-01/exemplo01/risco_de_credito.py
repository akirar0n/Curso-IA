renda_mensal = float(input("Informe sua renda mensal: "))
score_credito = int(input("Informe seu score: "))
restricao = input("Possui restrição? (sim/não) ").lower

if score_credito > 700 and restricao == 'não':
    print('Parabéns! Seu crédito foi aprovado.')

elif 500 <= score_credito <= 700:
    print('Seu crédito precisa passar por uma revisão.')

else:
    print('Seu crédito foi negado.')