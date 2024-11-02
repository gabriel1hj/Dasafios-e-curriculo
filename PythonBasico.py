def fun1():
  h = 0
  lista = ["Reinaldo","José","Pabblo"]
  for i in range(2):
    a = int(input("digite:"))
    Aplicador = lista[-a]
    aplicador2 = lista.remove(Aplicador)
    for j in lista:
      h += 1
      print(f"{h} -"+j)


def fun2():
  lista = str(["Rivaldo","Kaka","Risaldo"])
  for i in lista:
        print(lista.count(i))



def fun3():
    lista = ["Renaldo","Kanaldo","Ednaldo","Raimundo","Edimundo","Ricardo","Chaves"]
    for i in range(1):
        r = lista.pop()
    for i in lista:
        print(i)

def fun4():
    lista = [1245,1027,1221,2134]

    for i in lista:
        a = float(input("Digite um número"))
def test01():
    lista = [2, 3, 4, 5, 6, 7, 24, 2, 3, 5, 65, 6, 5, 63, 5, 3, 2, 1, 2, 4, 5, 2, 5, 6, 3, 5, 6, 7, 4, 3, 2, 1, 2, 3, 4,
             2, 12, 23, 4, 2, 4, 2, 1]
    print(lista.count(2))
test01()
fun2()