# funcion básica.
def multiplica(val1, val2):
    val1 = float(input("Ingrese el primer valor: "))
    val2 = float(input("Ingrese el segundo valor: "))
    valor = val1 * val2
    return valor


def resultado(r):
    r = float(multiplica(999, 9))
    print(r)


def FnCadena(cadena1):
    cadena1 = input("Ingrese su comentario: ")
    dato2 = "Chancho Feliz 2023"
    union = str(cadena1) + " " + str(dato2)
    print(union)
    return union


# multiplica(0, 0)
FnCadena("")
resultado(0)
