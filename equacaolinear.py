#função que resolve uma equação linear ax+b=c

def separa_fatores(equacao):
  ab=equacao.rpartition("=")[0]
  a=int(ab.rpartition("x")[0])
  b=int(ab.rpartition("x")[-1])
  c=int(equacao.rpartition("=")[-1])
  x=(c-b)/a
  print("valor de x=",x)


separa_fatores(input("digite a equação\n").lower().replace(" ",""))
