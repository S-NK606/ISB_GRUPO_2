# Análisis y Procesamiento de Señal EMG para Clasificación de Movimientos Basado en la Transformada Wavelet y Extracción de Características

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
3. [Objetivos](#3-objetivos)
4. [Materiales y equipos](#4-materiales-y-equipos)
5. [Metodología](#5-metodología)
6. [Resultados y discusiones](#6-resultados-y-discusiones)
7. [Conclusiones](#7-conclusiones)
8. [Referencias bibliográficas](#8-referencias-bibliográficas)


## 1. Introducción

<div style="text-align: justify;">

La electromiografía de superficie (sEMG, por sus siglas en inglés) es una técnica ampliamente utilizada en el análisis de actividad muscular y aplicaciones de interfaces hombre-máquina, debido a su capacidad para capturar patrones eléctricos generados durante las contracciones musculares. Sin embargo, el sEMG enfrenta desafíos significativos, como la presencia de artefactos y ruidos, principalmente de origen cardíaco y del entorno, que afectan la precisión de las señales recolectadas [1], [2].

Para optimizar la calidad y utilidad de las señales EMG, los procesos de preprocesamiento y extracción de características son esenciales. Entre los métodos de procesamiento, la transformada wavelet ha demostrado ser una técnica poderosa para la descomposición y análisis en tiempo-frecuencia, permitiendo extraer información significativa de señales no estacionarias, como es el caso de las señales EMG [3]. La extracción de características a partir de estas transformadas facilita la clasificación de gestos o contracciones musculares mediante algoritmos de aprendizaje automático, mejorando así el reconocimiento de patrones en interfaces de control para prótesis y aplicaciones de rehabilitación [4].

Este trabajo presenta un análisis exhaustivo del procesamiento de señales EMG utilizando la transformada wavelet para extraer características robustas, que permitan una clasificación precisa de movimientos. Además, se exploran métodos de optimización de características para reducir la dimensionalidad y mejorar la eficiencia de los clasificadores, manteniendo la precisión en contextos de múltiples días, donde las variaciones en las señales pueden impactar negativamente el rendimiento de los modelos entrenados.
</div>

## 2. Marco teórico

<div style="text-align: justify;">

texto

</div>

## 3. Objetivos

### Objetivo general
Desarrollar un método efectivo de procesamiento de señales EMG utilizando la transformada wavelet y técnicas de extracción de características para mejorar la precisión en la clasificación de movimientos musculares y gestos, con aplicaciones en interfaces hombre-máquina y rehabilitación.

### Objetivos Específicos
1. Analizar y comparar diferentes métodos de preprocesamiento de señales EMG, incluyendo técnicas de eliminación de ruido y artefactos, para optimizar la calidad de las señales utilizadas en el estudio.

2. Implementar la transformada wavelet para la descomposición y análisis en tiempo-frecuencia de señales EMG, evaluando su capacidad para capturar patrones significativos en señales no estacionarias.

3. Extraer y seleccionar características relevantes de las señales EMG utilizando métodos de extracción de características basados en dominios de tiempo y frecuencia, con el fin de optimizar la clasificación de movimientos.

4. Desarrollar una estrategia de optimización de características para reducir la dimensionalidad de las señales EMG, manteniendo la precisión del modelo y mejorando la eficiencia computacional.


## 4. Materiales y equipos

<div align="center">

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| (R)EVOLUTION  | Kit BITalino  | 1        |
|      -      |Electrodos de contacto| 3|
|       -       | Laptop o PC   | 1        |

</div>
<p align="justify">
   
## 5. Metodología
**Recolección de datos**


**Características extraídas [5]**

|   Modelo      | Descripción   |
|---------------|---------------|
|MFL: Longitud fractal máxima|
|Para el cálculo de la longitud de la señal sEMG se debe: <ul><li>Calcular la longitud en diferentes escalas. \(k\)</li><li>Usar una fórmula basada en teoría de fractales para obtener el valor de la Longitud Máxima del Fractal.</li><li>Evaluar la intensidad y complejidad de la contracción muscular.</li></ul>| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/1_FML.png">|
|MYOP: Porcentaje de Miopulsos|
|Los momentos espectrales describen la distribución de la energía de la señal en función a una cierta frecuencia. Por ello, el VCF mide la dispersión y variabilidad de la energía del sMEG con el propósito de evaluar la consistencia de la contracción muscular y la presencia de fatigas. Se mide respecto a los momentos espectrales de primer y segundo orden (SM1 y SM2) en conjunto con el poder total del espectro de la señal. (SM0).| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/2_VCF.png">|
|SS: Sincronización espacial|
|La sincronización especial evalúa la sincronización de señales registradas en canales vecinos del electrodo, evaluando si poseen patrones similares que, en caso sea así, indica que la señal vecina proviene de la misma actividad muscular y no es ruido. Esta medida permite diferenciar la información verdadera del ruido distinguiendo señales de una actividad muscular en conjunto.| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/3_SS.png">|
|MYOP: Porcentaje de Miopulsos|
|Es una característica que mide la proporción de tiempo en la que un músculo está activo cuando la amplitud absoluta de la señal supera un valor de umbral definido. Cuantifica la actividad muscular distinguiendo valores altos y bajos según el umbral.| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/4_MYOP.png">|
|AR: Coeficientes autorregresivos|
|Son coeficientes obtenidos de un modelo autoregresivo, combinación lineal de valores previos, que se usa para predecir el valor actual de la señal EMG. Sirve para la búsqueda de patrones en la señal EMG, clasificar los coeficientes generados para identificar movimientos específicos y registrarlos.| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/5_AR.png">|
|V: Características del orden V|
|La característica v-Order (V) es un detector no lineal que se usa para estimar, indirectamente, la fuerza de contracción muscular con un modelo matemático. Es decir, representa la actividad e intensidad de los músculos durante la contracción.| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/6_V.png">|
|MNF: Frecuencia Media|
|Esta medida representa la frecuencia promedio en la cual se concentra la mayor parte de la energía de la señal EMG siendo un promedio ponderado que nos puede indicar la intensidad de la contracción. Cuando la MNF obtiene valores bajos indica la fatiga del músculo, a su vez, cuando un músculo se activa con mayor intensidad, el valor de la MNF capturará el aumento.| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|
|Titulo|
|Texto| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/7_MNF.png">|

### 5.1. Análisis de Señales EMG

Parametros usados en el filtrado de señales: </p> 
Se ha realizado un filtrado utilizando la wavelet biorthogonal 3.1 con un nivel de descomposición 4. Este método ha logrado reducir el ruido de las señales, manteniendo la integridad de las características esenciales para un análisis detallado. </p> 

*Preprocesamiento*

texto

*Transformada Wavelet Discreta (DWT)*

texto

#### Fórmula de la DWT
La **DWT** utiliza una **función madre wavelet** $$\( \psi(t) \)$$, que es escalada y trasladada para descomponer la señal $$\( x(t) \)$$ en coeficientes de detalle y aproximación. La DWT se define matemáticamente como:

$$
W_{\psi}(a, b) = \frac{1}{\sqrt{|a|}} \int_{-\infty}^{\infty} x(t) \psi^*\left(\frac{t - b}{a}\right) dt
$$

Donde:
- \( a \) es el parámetro de **escala**, que controla la compresión o expansión de la wavelet.
- \( b \) es el parámetro de **traslación**, que desplaza la wavelet a lo largo de la señal.
- $$\( \psi(t) \)$$ es la **función madre wavelet**.
- $$\( \psi^* \)$$ es la **conjugada compleja** de la función madre wavelet.

Para la DWT, los valores de $$\( a \)$$ y $$\( b \)$$ se toman en discretos pasos, típicamente potencias de 2, es decir, $$\( a = 2^j \)$$ y $$\( b = k2^j \)$$, donde $$\( j \)$$ y $$\( k \)$$ son enteros.

#### Selección de la función madre wavelet
texto

#### Descomposición y Umbralización
texto
  
### Reconstrucción de la señal
texto

#### Fórmula de la DWT inversa
La señal original \( x(t) \) se puede reconstruir mediante la DWT inversa usando la siguiente expresión:

$$
x(t) = \sum_{j} \sum_{k} W_{\psi}(a_j, b_k) \psi_{a_j, b_k}(t)
$$

Donde $$\( W_{\psi}(a_j, b_k) \)$$ son los coeficientes wavelet calculados en el proceso de descomposición.

### Caracteristicas extraidas

mas texto xd tabla no de resultados sino q de los cosos q se extraen

## 6. Resultados y discusiones

aqui si los resultados (sofia)

#### Discusiones de EMG

discutan uwu

## 7. Conclusiones

conclusiones xd

## 8. Referencias bibliográficas

[1] X. Jiang et al., "Optimization of HD-sEMG-Based Cross-Day Hand Gesture Classification by Optimal Feature Extraction and Data Augmentation," IEEE Transactions on Human-Machine Systems, vol. 52, no. 6, pp. 1281-1289, Dec. 2022. doi: 10.1109/THMS.2022.3175408.

[2] W. Lu, D. Gong, X. Xue, and L. Gao, "Improved multi-layer wavelet transform and blind source separation based ECG artifacts removal algorithm from the sEMG signal: in the case of upper limbs," Frontiers in Bioengineering and Biotechnology, vol. 12, pp. 1–10, May 2024. doi: 10.3389/fbioe.2024.1367929.

[3] N. Li, J. Ou, H. He, J. He, L. Zhang, Z. Peng, J. Zhong, y N. Jiang, "Exploration of a machine learning approach for diagnosing sarcopenia among Chinese community-dwelling older adults using sEMG-based data," *Journal of NeuroEngineering and Rehabilitation*, vol. 21, p. 69, 2024. doi: 10.1186/s12984-024-01369-y. 

[4] A. Phinyomark, P. Phukpattaranont, and C. Limsakul, "Feature reduction and selection for EMG signal classification," Expert Systems with Applications, vol. 39, no. 7, pp. 7420–7431, 2012. doi: 10.1016/j.eswa.2012.01.102.

[5] X. Jiang et al., “Optimization of HD-SEMG-Based Cross-Day hand gesture classification by optimal feature extraction and data augmentation,” IEEE Transactions on Human-Machine Systems, vol. 52, no. 6, pp. 1281–1291, May 2022, doi: 10.1109/thms.2022.3175408.
