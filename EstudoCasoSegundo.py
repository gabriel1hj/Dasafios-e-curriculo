F  = 1
E = 1
Avi = 1

passageiro = []
aviao = {}
dicio = {}
B = ""
evi = 0
c = 0
r = 0
C = 0
tratador = 0
entrada = int(input("Digite até um número:"))

for i in range(1,entrada+1):
    passageiro.append(str(f"P|{i}"))


while c < len(passageiro):

    C = int(input("Digite:"))
    tratador = ord(str(input("Digite até aonde o alfabeto vai\n(coloque maiusculo):")))

    evi = 65
    r = 1
    for i in passageiro:
        if passageiro.index(i) == c:
            aviao.update({str(f"A{Avi}{chr(evi)}{r}"):i})
            r += 1
            c += 1
            if r == C + 1:
                evi += 1
                r = 1

    entrada = str(input("Digite a sua posição Sr nelson:"))
    for i in aviao.keys():
        if entrada == aviao[i]:
           B = i
    if B == None:
        print("Não tem Vaga")
    else:
        print(f"Tem vaga sua posição é {B}")

    Avi += 1

while chr(evi) <= chr(tratador)  :
   for i in range(1,C + 1):
       aviao.update({str(f"A{Avi}{chr(evi)}{i}"): ""})
   evi += 1



