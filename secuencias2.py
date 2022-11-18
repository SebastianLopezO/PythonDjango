# SECUENCIAS
# OBJETOS QUE CONTIENEN MÁS DE UN SOLO ELEMENTO (DATO)
# LEN

#   LISTAS

import mailbox


kardashians = ['KIM', 'KHLOE', 'KIM', 'KENDALL', 'KILEY']
andrew = ['KIM', 'KENDALL', 'KHLOE', 'KENDALL']

print(kardashians)
print(kardashians[2])
print(kardashians[2:3])

# CLEAR, EXTEND, APPEND, REMOVE, INDEX, INSERT, COUNT, POP, UPDATE

'''kardashians.clear()
print()'''

kardashians.extend(andrew)
print(kardashians, '*')

kardashians.append(andrew)
print(kardashians, '*')

kardashians.remove(andrew)
print(kardashians)

print(kardashians.index('KIM'))

kardashians.insert(2, 'KOURTNEY')
print(kardashians)

print(kardashians.count('KIM'), len(kardashians))

kardashians.pop(4)
print(kardashians)

"""kardashians[3:7] = 'K'
print(kardashians)"""

#   CICLO FOR

# por cada elemento en el objeto 
# imprimir cada uno de los elementos de la lista kardashians, si hay repetidos, omitirlo
kardashians.sort()
kardashians[3] = 'BRUCE'
print(kardashians)

index = 0
for i in kardashians :
    if index == 0 :
        print(i)
    else :
        aux = kardashians[index-1]
        if i==aux :
            pass
        else :
            print(i)        
    index += 1

print('--------------------------------------------------------')
# TUPLAS
# Read
# count, index

motomami = ('SAOKO', 'CANDY', 'LA FAMA', 'BULERÍAS', 'BIZCOCHITO')

print(motomami.index('BULERÍAS'))
print(motomami.count('SAOKO'))

for i in motomami :
    print(i)

# DICCIONARIOS
# CRUD, llave-valor
# get, pop, update, values, keys, clear, items, setdefault, 

print("--------------------------------------------------------")
motomami = {'SAOKO':2.17, 'CANDY':3.13, 'LA FAMA':3.08, 'BULERÍAS':2.35, 'BIZCOCHITO':1.49}
motomamix = {'CHICKEN TERIYAKI':2.02, 'HENTAI':2.42, 'DIABLO':2.45}

print(motomami)

print(motomami.get('HENTAI'))

print(motomami['CANDY'])

motomami.pop('CANDY')
print(motomami)

motomami.update(motomamix)
print(motomami)



print(motomami.keys(), '*')
print(motomami.values(), '*')
print(motomami.items(), '*')

"""motomami.clear()
print(motomami)"""

motomami.setdefault('COMO UN G', 4.22)
print(motomami)

motomami['LA FAMA'] = 3.46
print(motomami)

motomami['SAKURA'] = 3.21
print(motomami)

for i,j in motomami.items() :
    print(i, j)

name = ['DIEGO RUIZ', 'JUAN DÍAS', 'JUAN DÍAS', 'SOFÍA RUIZ']
age = [20, 23, 34, 30]
mail = ['diego@mail.com', 'juan1@mail.com', 'juan2@mail.com', 'sofia@mail.com']
course = ['PYTHON', 'JAVA', 'BLOCKCHAIN', 'PHP']

alumnos = zip(name, age, mail, course)
print(alumnos)

for i,j,k,l in alumnos :
    print(i,j,k,l)
