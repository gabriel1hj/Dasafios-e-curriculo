def exercício1_adap_exercicio2_1(y,s):
    return y - s

#print(exercício1_adap_exercicio2_1(2024,2006))

def exercício2(a,b):
    s =  a + b
    z = a - b
    t = a * b
    w = a / b

    return s,z,t,w
#print(exercício2(4,2))



def exercício3(a,b):
    s = a / b
    return s
#print(exercício3(1545,1000))

def exercício4(a,b):
    d = 100

    Calculo = a * b
    Calculo = str(Calculo)
    y = Calculo.count('0')

    if y == 1:
        Calculo = float(Calculo)
        d /= 10
        Calculo /= d
        Calculo /= 10
        Calculo += a
        return Calculo
    if  y >= 2:
        Calculo = float(Calculo)
        d /= 100
        Calculo /= d
        Calculo /= 100
        Calculo += a
        return Calculo
    else:
        Calculo = float(Calculo)
        Calculo /= d
        return Calculo

print(exercício4(13000.45,15))

def exercício5(a):
    c = a
    c += 160
    c /= 5
    return c

#print(exercício5(24))

def exercício6(a):
    a = float(a)
    a /= 5
    return a

#print(exercício5(1203.40))







