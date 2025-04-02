import punto_a as pa

def menu_a():
    print("Menu Tp 1")
    print("1. Generar numeros aleatorios con distribución uniforme")
    print("2. Generar numeros aleatorios con distribución normal")
    print("3. Generar numeros aleatorios con distribución exponencial")
    print("4. Generar numeros aleatorios con distribución Poisson")
    print("5. Salir")

def menu():
    print("Menu principal")
    print("1. Punto A")
    print("2. Punto B")
    print("0. Salir")

def validar_cant_num():
    while True:
        try:
            n = int(input("Ingrese la cantidad de numeros a generar (máximo 50000): "))
            if n <= 1 or n > 50000:
                print("Error: la cantidad de números debe ser mínimo 1 y máximo 50000.")
                continue
            return n
        except ValueError:
            print("Error: debe ingresar un número entero.")

def main():
    opc = 0
    while opc != 5:
        menu()
        opc = int(input("Ingrese un número: "))
        if opc == 1:
            # Generar numeros aleatorios con distribución uniforme
            pass
        elif opc == 2:
            # Generar numeros aleatorios con distribución normal
            pass
        elif opc == 3:
            # Generar numeros aleatorios con distribución exponencial
            pass
        elif opc == 4:
            # Generar numeros aleatorios con distribución Poisson
            pass
        else:
            print("Opción no válida")
            
    print("Fin del programa")



if __name__ == "__main__":
    main()

""""""""""
    print("Menu del Punto A")
    print("1. Generar numeros aleatorios con distribución uniforme")
    print("2. Generar numeros aleatorios con distribución normal")
    print("3. Generar numeros aleatorios con distribución exponencial")
    print("4. Generar numeros aleatorios con distribución Poisson")
    print("5. Salir")
    opc = -1
    sub_opc = -1
    uso = False
    while opc != 0:
        menu()
        opc = int(input("Seleccione una opción: "))
        if opc == 1:
            while sub_opc != 5:
                menu_a()
                sub_opc = int(input("Seleccione una opción: "))
                if sub_opc == 1:
                    uso = True
                    a = float(input("Ingrese el limite inferior: "))
                    b = float(input("Ingrese el limite superior: "))
                    n = validar_cant_num()
                    valores_uniformes = pa.generador_uniforme(a, b, n)
                    pa.guardar_datos(valores_uniformes, "resultados.xlsx", "uniforme")
                
                elif sub_opc == 2:
                    uso = True
                    media = float(input("Ingrese la media: "))
                    desviacion = float(input("Ingrese la desviación estándar: "))
                    n = validar_cant_num()
                    valores_normal = pa.generador_normal(media, desviacion, n)
                    pa.guardar_datos(valores_normal, "resultados.xlsx", "normal")
                
                elif sub_opc == 3:
                    uso = True
                    lambd = float(input("Ingrese el valor de lambda: "))
                    n = validar_cant_num()
                    valores_expo = pa.generador_exponencial(lambd, n)
                    pa.guardar_datos(valores_expo, "resultados.xlsx", "exponencial")
                
                elif sub_opc == 4:
                    uso = True
                    lambd = float(input("Ingrese el valor de lambda: "))
                    n = validar_cant_num()
                    valores_poisson = pa.generador_poisson(lambd, n)
                    pa.guardar_datos(valores_poisson, "resultados.xlsx", "poisson")
                
                elif sub_opc == 5:
                    print("Saliendo al menu principal")
                    break
                else:
                    print("Opción no valida, intente nuevamente.")
        elif opc == 2:
            if uso is not False:
                intervalos = int(input("Ingrese la cantidad de intervalos para la gráfica: "))
                graficador_exponencial(valores_expo)
                graficador_normal(valores_normal)
                graficador_poisson(valores_poisson, intervalos)
                graficador_uniforme(valores_uniformes, intervalos)
        
        elif opc == 0:
            print("Finalizando el programa.")
            break
        else:
            print("Opción no valida, intente nuevamente.") """