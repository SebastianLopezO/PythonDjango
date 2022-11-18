# SOFTWARE PARA LA UNIVERSIDAD DE BUCARAMANGA
# Definir la clase alumnos
# nombre, programa, semestre, matricula, pago, kardex
# {carrera: ((id, curso, creditos, semestre))}

class Alumno() : # ATRIBUTOS & MÉTODOS

    def __init__(self, name, program) : # MÉTODO CONSTRUCTOR
        self.nombre = name
        self.programa = program
        self.semestre = 1
        self.matricula = False
        self.pago  = False
        self.kardex = list() # registros académicos del estudiante
        self.pga = 0.0

        # método de matricula de cursos: nombre & creditos ingresar desde consola 12>creditos<20
    def matricular(self) :
        print('BIENVENIDO A LA PLATAFORMA DE MATRICULA')
        sum_creditos = 0
        while True :
            curso = input("Ingrese el nombre del curso: ")
            # TRATAMIENTO DE EXCEPCIONES: CAPTURAR LOS ERRORES DE EJECUCIÓ PARA EVITARLOS
            # try - except
            while True:
                try : 
                    creditos = int(input("Ingrese la cantidad de créditos: "))
                    break
                except ValueError:
                    print("SOLO ADMITE VALORES NUMÉRICOS")

            creditos_restantes = 20 - sum_creditos
            aux = [curso, creditos]
            if creditos<=creditos_restantes :
                self.kardex.append(aux) 
                sum_creditos += creditos
            else :
                print('Los créditos inscritos superan el máximo permitdo')

            if sum_creditos>=20 :
                break
            elif sum_creditos>=12 :
                flag = int(input("Desea matricular otro curso\n1.SI 2.NO: "))
                if flag == 2:
                    break
            else:
                pass
        print(self.kardex)
        self.cuenta_cobro()
    
    def cuenta_cobro(self) :
        valor_credito = 15000
        self.total = 0
        for curso in self.kardex :
            self.total += curso[1] * valor_credito
        print(f'EL MONTO A PAGAR ES {self.total}')
    
    def pagar_matricula(self, monto) :
        if monto == self.total :
            print("EXCELENTE, TE VEREMOS EN CLASE!")
            self.pago = True
            self.matricula= True
        else :
            print('EL MONTO INGRESADO NO ES EL CORRESPONDIENTE AL VALOR DEL SEMESTRE\nINTÉNTALO DE NUEVO')

    def cancelar_cursos(self) :
        index = 0
        print("RESUMEN DE CURSOS MATRICULADOS")
        for i in self.kardex :
            print(index, i[0])
            index += 1
        while True :
            flag = int(input("Ingrese el código del curso de desea cancelar: "))
            try :
                self.kardex.pop(flag)
                break
            except IndexError :
                print("ESTE CURSO NO EXISTE, INGRESA UNO VÁLIDO.")
        print(self.kardex)
    
    def subir_notas(self) :
        sum_cxn = 0
        sum_creditos = 0
        for i in self.kardex :
            nota = float(input(f"Ingrese la nota final de {i[0]}: "))
            i.append(nota)
            sum_cxn += i[1] * i[2]
            sum_creditos += i[1]
        
        self.pga = round(sum_cxn/sum_creditos,2)
    
        print(self.kardex)
        print(f'Su promedio este semestre fue de {self.pga}')

        if self.pga>=3.5 :
            self.semestre += 1
            print(f"FELICIDADES! HA SIDO ASCENDIDO AL SEMESTRE {self.semestre}")
        else :
            print("NO LOGRÓ PASAR AL SEMESTRE")

a01 = Alumno('Pepito Perez','Programación')  # INSTANCIAR UNA CLASE
a01.matricular()
a01.pagar_matricula(210000)
a01.cancelar_cursos()
a01.subir_notas()
#a02 = Alumno()


                      #a01.matricular()