print("------Bienvenidos a la plataforma de Comfenalco------ ")

def separar_registros(lista=dict) :
    nombre = input('DIGITE EL NOMBRE DEL ESTUDIANTE A BUSCAR')
    if nombre in lista :
        registros = lista.get(nombre)
        return registros
    else :
        print('NO SE ENCONTRÓ EL ESTUDIANTE')

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

def subir_notas(lista_alumnos=dict) :
    nombre = input('Nombre del alumno a evaluar: ')
    if nombre in lista_alumnos.keys() : 
        alumno = lista_alumnos.get(nombre)
        for i in alumno :
            nota = float(input(f'Cual fue la nota del curso {i[0]} - '))
            i.append(nota)
        return lista_alumnos
    else :
        print('EL ALUMNO NO SE ENCUENTRA EN LISTA')

def promedio(lista_alumnos=dict) :
    registro = separar_registros(lista_alumnos)
    acumulativo_notas=0
    acumulativo_creditos=0
    for i in registro :
        acumulativo_notas += i[1] * i[2]
        acumulativo_creditos += i[1]
        promedio= acumulativo_notas/acumulativo_creditos
        return promedio      

if promedio(subir_notas(matricula_curso())) >= 3.5 :
    print('APROBÓ')
else :
    print('REPROBÓ')