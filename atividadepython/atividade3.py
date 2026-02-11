contador = 1
while contador <=4:
    nota = float(input(f"insira a nota do {contador} aluno"))
    soma_notas  += nota
contador +=1 
media = soma_notas/4
print("a media das 4 noats e:,media")