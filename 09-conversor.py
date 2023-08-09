constante = 32
constant = 1.8
opc = input("Ingrese la escala Celsius C o Farenhit F:").lower()
numero = float(input("Ingrese el numero a calcular:"))
if numero > 100:
    print("Valor elevado.")
    exit
if opc == "f" and numero < 101:
    numero = (numero-constante)*5/9
    print("Escala Celsius:")
    print(numero)
elif opc == "c" and numero < 101:
    numero = numero*constant+32
    print("Escala Farenhit:")
    print(numero)
else:
    print("Escala o numero incorrectos..")
