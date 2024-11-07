h = 0

lista = []

dicio = {}
dicionario = {}


while h == 0:

   a = str(input("Digite:"))
   dicio = {a:{}}


   controle = int(input("Digite quanto quer alocar"))
   for i in range(controle):
        k = str(input("Digite o qualquer coisa:"))
        b = str(input("Digite o alguma coisa relacinado ao primeiro:"))

        dicio[a].update({k: b})
   for i in dicio:
       dicionario[i] = dicio[i]


   h = int(input("Se quiser sair digite 1\nSenão digite 0:"))
   if h != 0:
       continue

print(dicionario)







