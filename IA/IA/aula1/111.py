#Simulando um Dataset
#Crie uma lista de dicionários (dados estruturados) com 5 pessoas contendo: Nome, idade e salário.
#Depois:Mostre apenas quem tem salário acima de 5000,Calcule a média salarial

pessoas = [
    {"nome": "Alice", "idade": 30, "salario": 6000},
    {"nome": "Bob", "idade": 25, "salario": 450 },
    {"nome": "Charlie", "idade": 35, "salario": 700 },
    {"nome": "David", "idade": 28, "salario": 4800},
    {"nome": "Eve", "idade": 32, "salario": 5200}
]                   
salarios_acima_5000 = [pessoa for pessoa in pessoas if pessoa["salario"] > 5000]
media_salarial = sum(pessoa["salario"] for pessoa in pessoas) / len(pessoas)
print("Pessoas com salário acima de 5000:")
for pessoa in salarios_acima_5000:
    print(f"{pessoa['nome']} - Salário: {pessoa['salario']}")
print(f"Média salarial: {media_salarial:.2f}")

