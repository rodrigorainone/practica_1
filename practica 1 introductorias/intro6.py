
lista = [1,2,3,4,5,6,7,8,9,10]

par =[]

impar = []

for i in lista:
    if not(i % 2 == 0):
        impar.append(i)
    else:
        par.append(i)

print(par)

print(impar)