if __name__ == '__main__':
    students = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    # este bucle esta correcto
        """
        debe salir el nombre del estudiante 
        con la nota mas baja. 
        """
    scores = [] #name students
    for i in students:
        scores.append(i[1])
    #print(scores) se obtuvieron las notas de los estudiantes
    del_duplicados = set(scores)
    second = sorted(del_duplicados)[1]
    # sus nombres deben estar en orden alfabetico
    for flojos in students:
        if second == flojos[1]:
            names.append(flojos[0])
    for name in sorted(names):
        print(name)

# Nested Lists

"""
Leer estudiantes: nombre y calificación
Guardar en lista anidada: [['Harry', 37.21], ['Berry', 37.21], ...]
Encontrar la segunda calificación más baja (no la segunda más alta)
Imprimir los nombres de quienes tienen esa calificación, en orden alfabético

"""

if __name__ == '__main__':
        n = int(input())
        student = []

        for i in range(n):
            name = input()
            score = float(input())
            student.append([name,score])

        second = sorted(set([s[1] for s in student]))[1]
        """ EXTENDIDO  
        
        notas = [s[1] for s in student]
        del_duplicados = set(notas)
        orden = sorted(del_duplicados)
        segundo = orden[1]
        
        """

        names = sorted([flojos[0] for flojos in student if second == flojos[1]])
        for y in names:
            print(y)

        """
        for flojos in student:
            if second == flojos[1]:
                sorted(names.append(flojos[0]))
                print(names)
        """