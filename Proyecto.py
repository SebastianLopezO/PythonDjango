# Programa de registro academico para matricular estudiantes, cursos, con nota, final y estatus de aprobado
# { nombre1 : [ [curso1, creditos1, nota1], [curso2, creditos2, nota2] ] }
list()

lista_alumnos = ('DIEGO' ,  'JUAN' , 'OMAIRA' , 'SOFIA' , 'JOSEPH' , 'LUNA')
lista_cursos = ("PHP", "JAVA", "PYTHON", "HTML", "INGLES", "HABILIDADES BLANDAS", "SQL")
lista_creditos = (5, 5, 5, 4, 3, 2, 4)

def matricula(alumnos, cursos, creditos):
    contador = 0
    while contador<3:
        nombre=input('¿Cuál es tu nombre?:')
        if nombre in alumnos: 
            print('Bienvenido a su proceso de matrícula')
            lista_grande = []
            indice = 0
            for i in cursos :
                print(indice, i)
                indice += 1
            flag = True
            while flag :
                codigo_curso = int(input(f'Eliga el curso que va a matricular'))
                lista_grande.append([cursos[codigo_curso], creditos[codigo_curso]])
                mas = input('DESEA MATRICULAR OTRA MATERIA? S/N')
                if mas == 'N' :
                    flag = False          
            break    
        else:
            print('Su nombre no está en la lista')
            contador += 1
    registro = {nombre : lista_grande} 
    return registro

def subir_notas(registros_acad=dict, cursos=list):
    for k,v in registros_acad.items():
        for i in v :
            nota = float(input(f'Ingrese la nota final de {i[0]} del estudiante {k}'))
            i.append(nota)
    else :
        print('ESE CURSO NO ESTÁ EN LA BASE DE DATOS')
    print(registros_acad)
    return registros_acad

def promedio(registros_acad=dict) :
    # promedio = sumatoria(creditos*nota)/sumatoria(creditos)
    for k,v in registros_acad.items() :
        sum_cxn = 0
        sum_cred = 0
        for i in v :
            print(i)
            sum_cxn += i[1] * i[2]
            sum_cred += i[1]
        prom = sum_cxn/sum_cred
        print(f'{k} - {prom}')

promedio(subir_notas(matricula(lista_alumnos, lista_cursos, lista_creditos),lista_cursos))
