numero = input("Ingrese un número de tres cifras: ")

# Validar si no ingresó nada
if numero == "":
    print("Error al ingresar los datos")

else:
    # Convertir a entero
    numero = int(numero)

    # Validar si es negativo
    if numero < 0:
        print("El numero debe ser mayor a 0")

    else:
        # Validar si tiene 3 cifras
        if numero < 100 or numero > 999:
            print("El numero debe ser de 3 cifras")

        else:
            # Verificar si es capicúa
            centenas = numero // 100
            unidades = numero % 10
            print(f"Centenas: {centenas}")
            print(f"Unidades: {unidades}")
            
            if centenas == unidades:
                print("Es capicua")
            else:
                print("No es capicua")