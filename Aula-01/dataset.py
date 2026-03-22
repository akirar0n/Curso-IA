pessoas = [
    {"nome": "Ana", "idade": 22, "salário": 4000},
    {"nome": "Carlos", "idade": 30, "salário": 6000},
    {"nome": "Maria", "idade": 28, "salário": 5000},
    {"nome": "João", "idade": 35, "salário": 3000},
    {"nome": "Fernanda", "idade": 40, "salário": 8000},
]

print("Salário acima de 5000: ")
for pessoa in pessoas:
    if pessoa["salario"] > 5000:
        print(pessoa["nome"])

total = 0
for pessoa in pessoas:
    total += pessoa["salario"]

media_salarial = total