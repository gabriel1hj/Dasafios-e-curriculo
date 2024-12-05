N = []
L = int(input("Digite o número de ligações:"))
T = []
dicio = {}

for i in range(int(input("Digite o número vendedores:")) + 1):
    if i != 0:
        N.append(i)

for i in range(L):
    T.append(int(input("Digite o numero:")))

alterador = 0
ligação = []
Nliga = 0
c = 0

for i in N:
    Nliga = 0
    dicio.update({i: T[c]})
    ligação.append(Nliga + 1)

    c += 1

R = 0

Nliga = 0

while c < L:
    alterador = min(dicio.values())

    for i in dicio.keys():
        s = dicio[i]
        if s == alterador:
           R = i
           for i in dicio.keys():
               dicio[i] -= alterador
               dicio.update({i:dicio[i]})

           break



    dicio.update({R: T[c]})
    ligação[N.index(R)] += 1
    c += 1

for i in N:
    print(f"O vendendor {i},Fez {ligação[N.index(i)]} ligações")
