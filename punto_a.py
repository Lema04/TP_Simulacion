import numpy as np
import pandas as pd


def generadorRandom(n, x0=123456789):
# #      X0 es la semilla
# #    a es la constante multiplicativa a = 1 + 4.k (con k un número entero positivos)
# #    c es una constante aditiva c debe ser relativamente primo a m 
# #    m es el módulo m = 2g  (con g un número entero positivos) 
# #    r es el número aleatorio

    
    # a = 166452557         # =1+4(41613139)
    # c = 1013904223
    # m = 2**32
    # x0 = 123456789
    # primera = True
    # if primera:
    #     print("primera", ant)
    #     x1 = (a*x0+c)%m
    #     primera = False
    # else:
    #     x1 = (a*ant+c)%m
    #     print("no primera", ant)
    # r = x1 / (m-1)
    # print(ant)
    # return r
    
    a = 166452557         # =1+4(41613139)
    c = 1013904223
    m = 2**32

    xi = x0
    for i in range(n):
        xi = (a * xi + c) % m
        yield xi / (m)
    

# a y b pide en menu de opciones
# a tiene q ser menor q b
def generador_uniforme(a , b, n):
    # random_numbers = generadorRandom(n)
    # return [a + rnd * (b - a) for rnd in random_numbers]
    valores = [(a + rnd * (b - a)) for rnd in generadorRandom(n)]
    return valores


def generador_normal(media, desviacion, n):
    valores = []
    for i in range(n):
        rnd1 = generadorRandom()
        rnd2 = generadorRandom()
        z = np.sqrt(-2*np.log(1-rnd1))*np.cos(2 * np.pi* rnd2)
        x = (media + desviacion*z)
        valores.append(x)
    return valores

def generador_exponencial_neg(media, n):
    valores = []
    for i in range(n):
        rnd = generadorRandom()
        x = (-1*media)*np.log(1-rnd)
        valores.append(x)
    return valores
     

def generador_poisson(media, n):
    valores = []
    for i in range(n):
        p = 1
        x = -1
        a = np.exp(-media)
        print(-media)
        # u = generadorRandom()
        # p = p * u
        # x = x + 1

        while p >= a:
            u = generadorRandom()
            p = p * u
            x = x + 1
        valores.append(x)
    return valores




