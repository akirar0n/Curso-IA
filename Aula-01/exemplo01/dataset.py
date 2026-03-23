pessoas = [
    {"nome": "Ana", "idade": 22, "salario": 4000},
    {"nome": "Carlos", "idade": 30, "salario": 6000},
    {"nome": "Maria", "idade": 28, "salario": 5000},
    {"nome": "João", "idade": 35, "salario": 3000},
    {"nome": "Fernanda", "idade": 40, "salario": 8000}
]

print("Salário acima de 5000: ")
for pessoa in pessoas:
    if pessoa["salario"] > 5000:
        print(pessoa["nome"])

total = 0
for pessoa in pessoas:
    total += pessoa["salario"]

media_salarial = total / len(pessoas)
print("Média salarial: ", media_salarial)