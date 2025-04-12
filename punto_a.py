import numpy as np
import pandas as pd

"""
# def generadorRandom(n, x0=123456789):
# #      X0 es la semilla
# #    a es la constante multiplicativa a = 1 + 4.k (con k un número entero positivos)
# #    c es una constante aditiva c debe ser relativamente primo a m 
# #    m es el módulo m = 2g  (con g un número entero positivos) 
# #    r es el número aleatorio
    
    # a = 166452557         # =1+4(41613139)
    # c = 1013904223
    # m = 2**32

    # xi = x0
    # for i in range(n):
    #     xi = (a * xi + c) % m
    #     yield xi / (m)
    
# def generador_uniforme(a , b, n):
#     valores = [(a + rnd * (b - a)) for rnd in generadorRandom(n)]
#     return valores


# def generador_normal(media, desviacion, n):
#     rnd_gen = generadorRandom(n*2)
#     valores = []
#     for i in range(n):
#         rnd1 = next(rnd_gen)
#         rnd2 = next(rnd_gen)
#         z = np.sqrt(-2*np.log(1-rnd1))*np.cos(2 * np.pi* rnd2)
#         x = (media + desviacion*z)
#         valores.append(x)
#     return valores

# def generador_exponencial_neg(media, n):
#     rnd_gen = generadorRandom(n)
#     valores = []
#     for i in range(n):
#         rnd = next(rnd_gen)
#         x = (-1*media)*np.log(1-rnd)
#         valores.append(x)
#     return valores
     

# def generador_poisson(media, n):
#     rnd_gen = generadorRandom(n)
#     valores = []
#     for i in range(n):
#         p = 1
#         x = -1
#         a = np.exp(-media)
#         u = np.random.random_integers(0, 1)
#         p = p * u
#         x = x + 1

#         while p >= a:
#             u = np.random.random_integers(0,1)
#             p = p * u
#             x = x + 1
#         valores.append(x)
#     return valores
"""

def generador_uniforme(a, b, n):
    valores = []
    for i in range(n):
        rnd = np.random.uniform()
        x = a + rnd * (b-a)
        valores.append(x)
    return valores

def generador_normal(media, desviacion, n):
    valores = []
    for i in range(n):
        rnd1 = np.random.uniform()
        rnd2 = np.random.uniform()

        z = np.sqrt(-2*np.log(1-rnd1))*np.cos(2*np.pi*rnd2)
        x = media + (desviacion * z)
        valores.append(x)
    return valores

def generador_exponencial_neg(media, n):
    valores = []
    for i in range(n):
        rnd = np.random.uniform()
        x = -media * np.log(1-rnd)
        valores.append(x)
    return valores

def generador_poisson(media, n):
    valores = []
    for i in range(n):
        p = 1
        x = -1
        a = np.exp(-media)
        u = np.random.random()
        p = p * u
        x = x + 1
        while p >= a:
            u = np.random.random()
            p = p * u
            x = x + 1
        valores.append(x)
    return valores

def guardar_datos(datos, nombre_archivo, distribucion):
    try:
        with pd.ExcelWriter(nombre_archivo, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            df = pd.DataFrame({"Valores": datos})
            df.to_excel(writer, sheet_name=distribucion, index=False)
            print(f"Datos guardados en {nombre_archivo}, en la hoja {distribucion}")
    except FileNotFoundError:
        with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
            df = pd.DataFrame({"Valores": datos})
            df.to_excel(writer, sheet_name=distribucion, index=False)
            print(f"Datos guardados en {nombre_archivo}, en la hoja {distribucion}")