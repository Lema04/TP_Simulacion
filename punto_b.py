import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def validar_dist_teo():
    dist = input("¿Qué distribución teórica desea utilizar? (normal, uniforme, exponencial, poisson): ").strip().lower()
    while dist not in ["normal", "uniforme", "exponencial", "poisson"]:
        print("Error!! Distribución no válida, por favor elija entre normal, uniforme, exponencial o poisson")
        dist = input("¿Qué distribución teórica desea utilizar? (normal, uniforme, exponencial, poisson): ").strip().lower()
    return dist

def graficador(data, intervalos):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    datos_uniforme = data["Uniforme"]
    datos_normal = data["Normal"]
    datos_exponencial = data["Exponencial"]
    datos_poisson = data["Poisson"]

    sns.histplot(datos_uniforme, bins=intervalos, color="green", kde=False, stat="count", ax=axes[0,0])
    axes[0,0].set_title("Distribución Uniforme")
    axes[0,0].set_xlabel("Valores Aleatorios Generados")
    axes[0,0].set_ylabel("Frecuencia")

    sns.histplot(datos_poisson, bins=intervalos, color="blue", kde=False, stat="count", ax=axes[0,1])
    axes[0,1].set_title("Distribución Poisson")
    axes[0,1].set_xlabel("Valores Aleatorios Generados")
    axes[0,1].set_ylabel("Frecuencia")

    sns.histplot(datos_normal, color="red", kde=True, stat="density", bins=intervalos, ax=axes[1,0])
    axes[1,0].set_title("Distribución Normal")
    axes[1,0].set_xlabel("Valores Aleatorios Generados")
    axes[1,0].set_ylabel("Densidad")

    sns.histplot(datos_exponencial, color="purple", kde=True, stat="density", bins=intervalos, ax=axes[1,1])
    axes[1,1].set_title("Distribución Exponencial")
    axes[1,1].set_xlabel("Valores Aleatorios Generados")
    axes[1,1].set_ylabel("Densidad")

    plt.tight_layout()
    plt.show()

def agrupar_intervalos(f_obs, f_esp, min_freq=5):
    obs_agrupada = []
    esp_agrupada = []
    acum_obs = 0
    acum_esp = 0

    for fo, fe in zip(f_obs, f_esp):
        acum_obs += fo
        acum_esp += fe
        if acum_esp >= min_freq:
            obs_agrupada.append(acum_obs)
            esp_agrupada.append(acum_esp)
            acum_obs = 0
            acum_esp = 0

    # Si sobró algo al final, agrégalo al último grupo
    if acum_esp > 0:
        if obs_agrupada:
            obs_agrupada[-1] += acum_obs
            esp_agrupada[-1] += acum_esp
        else:
            obs_agrupada.append(acum_obs)
            esp_agrupada.append(acum_esp)

    return np.array(obs_agrupada), np.array(esp_agrupada)


def dist_teorica():
    dist = validar_dist_teo()
    if dist == "normal":
        media = float(input("Ingrese la media: "))
        desviacion = float(input("Ingrese la desviación estándar: "))
        return stats.norm(media, desviacion)
    if dist == "uniforme":
        a = float(input("Ingrese el límite inferior: "))
        b = float(input("Ingrese el límite superior: "))
        return stats.uniform(a, b-a)
    if dist == "exponencial":
        media = float(input("Ingrese la media: "))
        return stats.expon(loc=0, scale=media)
    if dist == "poisson":
        media = float(input("Ingrese la media: "))
        return stats.poisson(media)

def test_chi_cuadrado(datos, alpha):
    dist = dist_teorica()
    n = len(datos)
    
    if n < 30:
        raise ValueError("Se requieren al menos 30 datos para aplicar el test chi-cuadrado.")

    k = int(np.sqrt(n))
    
    # Crear los límites de los intervalos
    min_val, max_val = min(datos), max(datos)
    limites = np.linspace(min_val, max_val, k + 1)
    
    # Frecuencia observada
    frec_obs, _ = np.histogram(datos, bins=limites)
    
    # Frecuencia esperada usando la CDF de scipy
    fe = []
    for i in range(k):
        a, b = limites[i], limites[i + 1]
        prob = dist.cdf(b) - dist.cdf(a)
        fe.append(prob * n)
    fe = np.array(fe)

    # Agrupar intervalos si es necesario
    frec_obs, fe = agrupar_intervalos(frec_obs, fe)

    # Estadístico chi-cuadrado
    chi2_stat = np.sum((frec_obs - fe) ** 2 / fe)

    # Grados de libertad
    gl = len(frec_obs) - 1

    # Valor crítico y p-value
    valor_critico = stats.chi2.ppf(1 - alpha, gl)

    print(f"H₀ = Los valores generados se ajustan a la distribución {dist.dist.name}")
    print(f"χ² calculado= {chi2_stat:.4f}")
    print(f"Grados de libertad = {gl}")
    print(f"Valor crítico (α = {alpha}): {valor_critico:.4f}")
    if chi2_stat < valor_critico:
        print("✔ No se rechaza H₀ (ajuste aceptable).")
    else:
        print("✘ Se rechaza H₀ (ajuste no aceptable).")