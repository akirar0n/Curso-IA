nome = input("Insira o nome do aluno: ")

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Média do aluno {nome}: {media:.2f}")
if media >= 7:
    print("Parabéns! Você foi aprovado.")
elif media >= 5 and media < 7:
    print("Você está de recuperação.")
else:
    print("Você está reprovado.")