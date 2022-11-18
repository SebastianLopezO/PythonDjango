class Alumno() :
    # nombre, programa, semestre, pago, matricula, kardex, pga
    def __init__(self, name, program) : # método constructor
        self.nombre = name
        self.programa = program
        self.semestre = 1
        self.pago = False
        self.matricula = False
        self.registros_academicos = list()
        self.pga = 0.0
    # inscribir cursos, liquidación de matricula, dar de baja un curso, subida notas, calculo pga

    def inscribir_cursos(self) :    # 12<creditos<20
        print("INSCRIPCIÓN DE CURSOS")
        self.contador = 0
        maximo = 20
        while True :
            curso = input("Ingrese el curso que desea matricular: ")
            creditos = int(input("Ingrese los créditos del curso: "))            

            if creditos>maximo :
                print("ESTE CURSO EXCEDE EL LÍMITE DE CRÉDITOS!")
            else :
                aux = [curso, creditos]
                self.registros_academicos.append(aux)
                self.contador += creditos
                maximo -= creditos
                print(f'Ha matriculado {self.contador} créditos, le quedan {maximo} créditos restantes')
                # TRATAMIENTO DE EXCEPCIONES: CAPTURAR LOS ERRORES EN EJECUCIÓN PARA EVITAR QUE EL PROGRAMA SE CAIGA
                # try - except
                while True :
                    try :
                        flag = int(input("Desea ingresar otro curso?\n1. SI 0. NO -> "))
                        break
                    except ValueError:
                        print("SOLO DEBE INGRESAR NÚMEROS -> 1. SI 0. NO")

            if self.contador<=12 and flag == 0:
                print('Aún no ha cumplido con el rango de créditos, go for it!')
            elif flag == 0 :
                break
            elif self.contador>=20 :
                break
            else :
                pass
        print(self.registros_academicos)
        self.calculo_matricula()
    
    def calculo_matricula(self) :
        valor_credito = 15500
        try :
            self.total_matricula = valor_credito*self.contador
            print(f"EL VALOR TOTAL DE SU MATRICULA ES DE ${self.total_matricula}")
        except AttributeError :
            print("Aún no ha hecho el proceso de matricula")
            self.inscribir_cursos()
            self.calculo_matricula()
    
    def pagar_matricula(self, monto) :
        if self.total_matricula == monto :
            print("Excelente, ya se procesó tu pago, te vemos en clase!!!")
            self.pago = True
            self.matricula = True 
        else :
            print(f"El valor pagado es incorrecto, recuenta tu dinero\nRecuerda que el monto a pagar es {self.total_matricula}")
        
    def cancelar_curso(self) :
        print("PLATAFORMA DE CANCELACIÓN DE CURSOS")
        print("Estos son los cursos que tiene inscritos")
        index = 0
        for i in self.registros_academicos :
            print(index, i[0])
            index += 1
        
        curso = int(input("Escriba el codigo del curso que desea cancelar"))
        try :
            self.registros_academicos.pop(curso)
        except IndexError :
            print('El curso que deseas eliminar no existe.')
        print(self.registros_academicos)
    
    def subir_notas(self) :
        for i in self.registros_academicos :
            nota = float(input(f'Ingrese la nota final del curso {i[0]}: '))
            i.append(nota)
        print(self.registros_academicos)
        self.calcular_pga()
    
    def calcular_pga(self) :
        # pga = sumatoria(creditos*nota) / sumatoria(creditos)
        sum_cxn = 0
        for i in self.registros_academicos :
            sum_cxn += i[1] * i[2]
        self.pga = sum_cxn/self.contador
        
        print(f"Su promedio este semestre fue de {self.pga}")
        if self.pga >= 3.5 :
            self.semestre += 1
            print(f"Felicidades, pasaste al semestre {self.semestre}")
        else :
            print("No lograste avanzar en tu malla curricular, sad :(")



        
       
a01 = Alumno('DIEGO ANDRÉS', 'DJANGO')
a01.inscribir_cursos()
a01.pagar_matricula(248000)
a01.cancelar_curso()
a01.subir_notas()
