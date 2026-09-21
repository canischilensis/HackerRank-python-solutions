# Finding the porcentage

"""
name es la key el nombre
line es la lista con las notas 
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # se ingresa el nombre del cual se quiere obtener el pormedio query_name. 
    # Por lo tanto queda asi - student_marks[query_name]
    # funcion suma: sum()
    # asi queda lo primero: sum(student_marks[query_name])
    # contar la cantidad de notas a partir de la persona que se consulta: len(student_marks[query_name])


    mean = sum(student_marks[query_name])/len(student_marks[query_name])
    print('{0:.2f}'.format(mean))
    # 0 Indica la posición del valor (el primer argumento).
    # : Inicia las instrucciones de formato.
    # .2: Define la cantidad de decimales a mostrar (dos).
    # f: Configura el formato como decimal (punto flotante).