import punto_a as pa
import matplotlib.pyplot as plt
import seaborn as sns

def graficador_uniforme(valores, intervalos):
    sns.histplot(valores, bins=intervalos, color='green')
    plt.title("Distribución Uniforme")
    plt.xlabel("Valores Aleatorios Generados")
    plt.ylabel("Frecuencia")
    plt.show()

n = 10
intervalos = 2
valores = pa.generador_uniforme(5, 20, n)

# print(valores)
# for rnd in pa.generadorRandom(100):
#     print(rnd)

graficador_uniforme(valores, intervalos)
