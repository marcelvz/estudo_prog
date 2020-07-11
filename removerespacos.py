#Remover espaço em branco de string (sem usar comandos prontos)
frase = input("Digite a frase\n")
fraselimpa = ""
for letra in frase:
  if letra != " ":
    fraselimpa = fraselimpa + letra
print(fraselimpa)
