# VARIABLES, ESTRUCTURAS DE CONTROL, FUNCIONES

# SECUENCIAS - OBJETOS ITERABLES
# LISTAS, TUPLAS, DICCIONARIOS, SETS

# LISTAS - []
# APPEND, CLEAR, EXTEND, COUNT, INDEX, INSERT, POP, REMOVE

rosalia = ['CON ALTURA', 'DESPECHÁ']
motomami = ['SAOKO', 'LA FAMA', 'CHICKEN TERIYAKI', 'CON ALTURA', 'DESPECHÁ']
print(motomami)

motomami.append('HENTAI')
print(motomami)

motomami.clear()
print(motomami)

motomami.extend(rosalia)
print(motomami)

print(motomami.count('CANDY'))

print(len(motomami))

print(motomami.index('CON ALTURA'))

print(motomami[1])

motomami.insert(1, 'CANDY')
print(motomami)

motomami.remove('DESPECHÁ')
print(motomami)

print('-----------------------------------------------------')

# CICLO FOR
# POR CADA UNO DE LOS ELEMENTOS EN UN OBJETO -> PROCESO

motomamix = ['SAOKO', 'CANDY','CON ALTURA', 'LA FAMA', 'CHICKEN TERIYAKI', 'HENTAI', 'CON ALTURA', 'DESPECHÁ', 'CON ALTURA']

print(motomamix.count('CON ALTURA'))

index = 0

motomamix[4] = 'sakura'

for i in motomamix :
    print(i)
    if i == 'CON ALTURA' :
        print(f'El índice es {index}')
    index += 1

motomamix.remove('CON ALTURA')
print(motomamix)

print("---------------------------------------------------------")

# TUPLAS
# QUE NO SE PUEDA ALTERAR LA INFORMACIÓN
# CRUD - METODOLOGÍA DE EJECUCIÓN
# READ 

kardashians = ('KIM', 'KHLOE', 'KOURTNEY', 'KENDALL', 'KILEY')
print(kardashians.index('KIM'))
print(kardashians.count('KENDALL'))

for i in kardashians :
    print(i)

# DICCIONARIOS
# ESQUEMA KEY - VALUE

#               llave:valor
kardashiansx = {'KIM':41, 'KHLOE':38, 'KOURTNEY':43, 'KILEY':motomami, 'KENDALL':'JENNER'}

print(kardashiansx)

# get, keys, values, items, pop, clear, setdefault, update, popitem, fromkeys

print(kardashiansx.get('KOURTNEY'))
print(kardashiansx.get('KRIS'))

print(kardashiansx['KENDALL'])

print(kardashiansx.keys())

print(kardashiansx.values())

print(kardashiansx.items())

"""kardashiansx.pop('KIM')
print(kardashiansx)

kardashiansx.clear()
print(kardashiansx)"""

kardashiansx.setdefault('KRIS',True)
print(kardashiansx)

kardashiansx['BRUCE'] = 'caitlyn'
print(kardashiansx)
"""
print("---------------------------------------------------")
motomamix = ['SAOKO', 'CANDY','CON ALTURA', 'LA FAMA', 'CHICKEN TERIYAKI', 'HENTAI', 'CON ALTURA']
kxm = dict(zip(motomamix,kardashiansx))
kardashiansx.update(kxm)

kardashiansx.popitem()
print(kardashiansx)"""

vocals = ('a', 'e', 'i', 'o', 'u')
numbers = 3

mydict = dict.fromkeys(vocals, numbers)
print(mydict, 'EL DICCIONARIO')

for i,j in kardashiansx.items() :
    print(i, j)
    #print(f'LLAVE = {k}, VALOR = {v}')

vocals = ('a', 'e', 'i', 'o', 'u')
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
letter = ('b', 'c', 'd', 'f')

my_tuple = zip(vocals, numbers, letter)
print(my_tuple)

for v,n,l in my_tuple :
    print(f'vocal: {v}, number: {n}, letter: {l}')
    if n>1 :
        break

print("-----------------------------------------------------")

# SETS
# {} - NO HAY ORDÉN - "CRUD"

random = {'MOTOMAMI', 'KARDASHIANS', 69, 1.67, False, 'MOTOMAMI'}

print(random)

for i in random :
    print(i)

# ADD, CLEAR, COPY, DIFFERENCE, DIFFERENCEUPDATE, REMOVE

random.add(kardashians)
print(random)

random2 = random
print(random2)

