import punto_a as pa
import punto_b as pb

def menu_a():
    print("Menu Punto A")
    print("1. Generar numeros aleatorios con distribución uniforme")
    print("2. Generar numeros aleatorios con distribución normal")
    print("3. Generar numeros aleatorios con distribución exponencial")
    print("4. Generar numeros aleatorios con distribución Poisson")
    print("5. Salir\n")

def menu():
    print("Menu principal")
    print("1. Punto A")
    print("2. Punto B (Graficador)")
    print("3. Punto B (Test Chi Cuadrado)")
    print("0. Salir\n")

def validar_cant_num():
    n = int(input("Ingrese la cantidad de numeros a generar (máximo 50000): "))
    while n < 1 or n > 50000:
        print("Error!! La cantidad de números a generar debe ser hasta 50000")
        n = int(input("Ingrese la cantidad de numeros a generar (máximo 50000): "))
    return n

def validar_limites():
    a = float(input("Ingrese el límite inferior: "))
    b = float(input("Ingrese el límite superior: "))
    while a >= b:
        print("Error!! El límite inferior debe ser menor que el límite superior")
        b = float(input("Ingrese el límite superior: "))
    return a, b

def validar_datos(datos):
    for valor in datos.values():
        if valor is not None:
            return True
    return False

def validar_intervalos():
    intervalos = int(input("Seleccione la cantidad de intervalos (10, 15, 20, 25): "))
    while intervalos not in [10, 15, 20, 25]:
        print("Error!! La cantidad de intervalos debe ser 10, 15, 20 o 25")
        intervalos = int(input("Seleccione la cantidad de intervalos (10, 15, 20, 25): "))
    return intervalos

def validar_alpha():
    alpha = float(input("Ingrese el nivel de aceptación (0.1; 0.05; 0.025; 0.01; 0.005): "))
    while alpha not in [0.1, 0.05, 0.025, 0.01, 0.005]:
        print("Error!! El nivel de aceptación debe ser 0.1; 0.05; 0.025; 0.01 o 0.005")
        alpha = float(input("Ingrese el nivel de aceptación (0.1; 0.05; 0.025; 0.01; 0.005): "))
    return alpha

def validar_distribucion(datos):
    dist_validas = []
    for key, value in datos.items():
        if value is not None:
            dist_validas.append(key.lower())
    dist = input(f"Seleccione el generador a testear {dist_validas}: ").strip().lower()
    while dist not in dist_validas:
        print("Error!! Aún no ha generado números con esa distribución, seleccione otra o genere valores primero")
        dist = input(f"Seleccione el generador a testear {dist_validas}: ").strip().lower()
    return dist.capitalize()

def main():
    print("Bienvenido al generador de números aleatorios")
    NOMBRE_ARCHIVO = "resultados.xlsx"
    datos = {
        "Uniforme": None,
        "Normal": None,
        "Exponencial": None,
        "Poisson": None
    }
    opc = -1
    sub_opc = -1
    while opc != 0:
        menu()
        opc = int(input("Seleccione una opción: "))
        if opc == 1:
            while sub_opc != 5:
                menu_a()
                sub_opc = int(input("Seleccione una opción: "))

                if sub_opc == 1:
                    a, b = validar_limites()
                    n = validar_cant_num()
                    datos["Uniforme"] = pa.generador_uniforme(a, b, n)
                    pa.guardar_datos(datos["Uniforme"], NOMBRE_ARCHIVO, "Uniforme")
                
                elif sub_opc == 2:
                    media = float(input("Ingrese la media: "))
                    desviacion = float(input("Ingrese la desviación estándar: "))
                    n = validar_cant_num()
                    datos["Normal"] = pa.generador_normal(media, desviacion, n)
                    pa.guardar_datos(datos["Normal"], NOMBRE_ARCHIVO, "Normal")
                
                elif sub_opc == 3:
                    media = float(input("Ingrese la media: "))
                    n = validar_cant_num()
                    datos["Exponencial"] = pa.generador_exponencial_neg(media, n)
                    pa.guardar_datos(datos["Exponencial"], NOMBRE_ARCHIVO, "Exponencial")

                elif sub_opc == 4:
                    media = float(input("Ingrese la media: "))
                    n = validar_cant_num()
                    datos["Poisson"] = pa.generador_poisson(media, n)
                    pa.guardar_datos(datos["Poisson"], NOMBRE_ARCHIVO, "Poisson")
                
                elif sub_opc == 5:
                    print("Regresando al menú principal")
                    break

                else:
                    print("Opción no válida, intente nuevamente")

        elif opc == 2:
            if validar_datos(datos):
                intervalos = validar_intervalos()
                pb.graficador(datos, intervalos)
            else:
                print("Error!! No hay datos generados para graficar")
                continue

        elif opc == 3:
            if validar_datos(datos):
                alpha = validar_alpha()
                dist = validar_distribucion(datos)
                pb.test_chi_cuadrado(datos[dist], alpha)

        elif opc == 0:
            print("Finalizando el programa...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()