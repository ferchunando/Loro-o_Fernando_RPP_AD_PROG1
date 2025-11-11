import os
from listas_estudiantes import *

#Punto 1
def listar_estudiantes(estudiantes: list, calificaciones: list): 
    ''' 
    Funcion: Pide el ingreso de una materia e imprime los nombres de los estudiantes junto con sus calificaciónes. 
    Parámetros: 
    - estudiantes como una lista de str. 
    - calificaciónes: como una lista de int. 
    Retorno: No retorna nada, solo imprime en consola.
    ''' 
    flag_iniciar = True 
    while flag_iniciar: 
        opciones = int(input("1) Matemáticas.\n2) Historia\n3) Ciencias\n4) Salir.\nElija la materia a la que desea acceder para ver las notas: ")) 
        match opciones: 
            case 1: 
                columna = 0 
                materia = "Matemática" 
            case 2: 
                columna = 1 
                materia = "Historia" 
            case 3: 
                columna = 2 
                materia = "Ciencias" 
            case _:
                print("No hay materias para evaluar! Saliendo al menú principal!!") 
                break 
            
        print(f"Lista de estudiantes con sus calificaciónes en {materia}:\n") 
        for i in range(len(estudiantes)): 
            nombre_estudiante = estudiantes[i] 
            notas_materias = calificaciones[i][columna] 
            print(f"Los estudiantes son: {nombre_estudiante} y las notas de la materia son: {notas_materias}")

def mostrar_estudiantes_con_calificacion_alta(estudiantes: list, calificaciones: list):
    '''
    Función: 
    - Recorrer todas las notas de todos los estudiantes y determinar la nota mas alta (o más baja) encontrada y el nombre del estudiante que la alcanzo.
    Parámetros: 
    - estudiantes como una lista de strings.
    - calificaciónes como una lista de ints.
    Retorno:
    - No retorna nada, solo imprime a los estudiantes con sus calificaciónes.
    '''
    mayor_calificacion = calificaciones[0][0]
    menor_calificacion = calificaciones[0][0]
    estudiante_mayor = estudiantes[0]
    estudiante_menor = estudiantes[0]

    for i in range(len(estudiantes)):
        for j in range(len(calificaciones[i])):
            nota = calificaciones[i][j]

            if nota > mayor_calificacion:
                mayor_calificacion = nota
                estudiante_mayor = estudiantes[i]

            if nota < menor_calificacion:
                menor_calificacion = nota
                estudiante_menor = estudiantes[i]
    
    print(f"El estudiante con la calificación más alta es {estudiante_mayor} con una nota de {mayor_calificacion}.")
    print(f"El estudiante con la calificación mas baja es {estudiante_menor} con una nota de {menor_calificacion}.")

def mostrar_estudiantes_por_promedio(estudiantes: list, calificaciones: list):
    '''
    La funcion muestra el promedio de calificaciónes de los estudiantes ordenados de manera ascendente (menor a mayor)    
    Parámetros:
    - estudiantes como una lista de str.
    - calificaciones como una lista de int.
    Retorno:
    - No retorna nada, muestra el promedio en la terminal
    '''
    lista_promedios = []
    suma = 0

    for i in range(len(estudiantes)):
        for j in range(len(calificaciones[i])):
            suma += calificaciones[i][j]
        promedio = suma / len(calificaciones[i])
        lista_promedios.append([estudiantes[i], promedio])

    for i in range(len(lista_promedios) -1):
        for j in range(i + 1, len(lista_promedios)):
            if lista_promedios[i][1] > lista_promedios[j][1]:
                aux = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = aux

    print(f"Estudiantes ordenados por el promedio de calificaciones de menor a mayor: ")
    for estudiantes, calificaciones in lista_promedios:
        print(f"{estudiantes}: {calificaciones:.2f}.")
        
def limpiar_pantalla():
    os.system('cls')