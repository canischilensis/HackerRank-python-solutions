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