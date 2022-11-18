print("------Bienvenidos a la plataforma de Comfenalco------ ")

def matricula_curso():
    # BASE DE DATOS
    lista_cursos = ("PHP", "JAVA", "PYTHON", "HTML", "INGLES", "HABILIDADES BLANDAS", "SQL")
    lista_creditos = (5, 5, 5, 4, 3, 2, 4)

    nombre =  (input("Escribe tu nombre por favor: "))

    indice = 0
    for i in lista_cursos:
        print(indice, i)
        indice += 1   

    listaax=[]

    while True:      
        cursos = int(input("Escribe tu curso por favor: "))
        lista_matricula=[lista_cursos[cursos],lista_creditos[cursos]]
        listaax.append(lista_matricula)
        flag = input("Deseas matricular otro cuso: S/N: ")        
        if flag == "N":
            print("Has terminado")
            break        
    nose = {nombre:listaax}
    return nose

alumnos=matricula_curso()
print(alumnos)

def subir_notas(lista_alumnos=dict) :
    nombre = input('Nombre del alumno a evaluar: ')
    if nombre in lista_alumnos.keys() : 
        alumno = lista_alumnos.get(nombre)
        for i in alumno :
            nota = input(f'Cual fue la nota del curso {i[0]} - ')
            i.append(nota)
        print(alumno)
    else :
        print('EL ALUMNO NO SE ENCUENTRA EN LISTA')

subir_notas(alumnos)




