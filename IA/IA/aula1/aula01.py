#Crie uma variavel e entrada de dados , 
# pergunte o nome do aluno;pergunte tres notas ,calcule a media .
# Depois mostre se ele estrá aprovado (>ou igual 7),recuperação(.ou igual 5 e <7),recprovado(<5)

aluno = input("Digite o nome do aluno: ")
#input entrada de dados, float para converter a string em numero decimal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
#.2f para mostrar apenas duas casas decimais
print(f"A média do aluno {aluno} é {media:.2f}")
if media >= 7:
    print("O aluno está aprovado.")
elif media >= 5:
    print("O aluno está em recuperação.")
else:
    print("O aluno está reprovado.")