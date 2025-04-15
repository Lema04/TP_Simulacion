import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def validar_dist_teo():
    dist = input("\n¿Qué distribución teórica desea utilizar? (normal, uniforme, exponencial, poisson): ").strip().lower()
    while dist not in ["normal", "uniforme", "exponencial", "poisson"]:
        print("Error!! Distribución no válida, por favor elija entre normal, uniforme, exponencial o poisson")
        dist = input("\n¿Qué distribución teórica desea utilizar? (normal, uniforme, exponencial, poisson): ").strip().lower()
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
        media = float(input("\nIngrese la media: "))
        desviacion = float(input("\nIngrese la desviación estándar: "))
        return stats.norm(media, desviacion)
    if dist == "uniforme":
        a = float(input("\nIngrese el límite inferior: "))
        b = float(input("\nIngrese el límite superior: "))
        return stats.uniform(a, b-a)
    if dist == "exponencial":
        media = float(input("\nIngrese la media: "))
        return stats.expon(loc=0, scale=media)
    if dist == "poisson":
        media = float(input("\nIngrese la media: "))
        return stats.poisson(media)

def test_chi_cuadrado(datos, alpha):
    dist = dist_teorica()
    n = len(datos)
    
    if n < 30:
        raise ValueError("Se requieren al menos 30 datos para aplicar el test chi-cuadrado.")
    
    es_discreta = hasattr(dist, "pmf") # pmf = función de masa de probabilidad
    es_continua = hasattr(dist, "pdf") # pdf = función de densidad de probabilidad
    
    if es_discreta:
        max_val = max(datos)
        frec_obs = np.bincount(datos, minlength=max_val+1)
        k_vals = np.arange(len(frec_obs)) # Valores posibles de la variable [0,1,2,...,max_val]
        fe = dist.pmf(k_vals) * n

        frec_obs, fe = agrupar_intervalos(frec_obs, fe)

    elif es_continua:
        k = int(np.sqrt(n))

        min_val, max_val = min(datos), max(datos)
        limites = np.linspace(min_val, max_val, k + 1)
        
        frec_obs, _ = np.histogram(datos, bins=limites)

        fe = []
        for i in range(k):
            a, b = limites[i], limites[i + 1]
            prob = dist.cdf(b) - dist.cdf(a)
            fe.append(prob * n)
        fe = np.array(fe)

        frec_obs, fe = agrupar_intervalos(frec_obs, fe)
    
    else:
        raise ValueError("Distribución no soportada/no reconocida.")

    chi2_stat = np.sum((frec_obs - fe) ** 2 / fe)

    gl = len(frec_obs) - 1

    valor_critico = stats.chi2.ppf(1 - alpha, gl)

    print(f"H₀ = Los valores generados se ajustan a la distribución {dist.dist.name}\n")
    print(f"χ² calculado= {chi2_stat:.4f}\n")
    print(f"Grados de libertad = {gl}\n")
    print(f"Valor crítico (α = {alpha}): {valor_critico:.4f}\n")
    if chi2_stat < valor_critico:
        print("✔ No se rechaza H₀ (ajuste aceptable).\n")
    else:
        print("✘ Se rechaza H₀ (ajuste no aceptable).\n")