import numpy as np
import pandas as pd

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
            print(f"Datos guardados en {nombre_archivo}, en la hoja {distribucion}\n")
    except FileNotFoundError:
        with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
            df = pd.DataFrame({"Valores": datos})
            df.to_excel(writer, sheet_name=distribucion, index=False)
            print(f"Datos guardados en {nombre_archivo}, en la hoja {distribucion}\n")