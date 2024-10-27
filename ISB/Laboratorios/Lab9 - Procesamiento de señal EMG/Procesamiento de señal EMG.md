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

**2.1 Normalización mediante Contracción Voluntaria Máxima (MVC)**
<p align="justify">
La normalización mediante Contracción Voluntaria Máxima (MVC) es un método ampliamente utilizado en el análisis de señales electromiográficas para estandarizar y comparar los niveles de activación muscular. Este proceso implica registrar la contracción máxima del músculo de interés en condiciones controladas, lo que permite establecer una referencia de activación máxima. De esta forma, los valores obtenidos de la señal sEMG pueden ser expresados como un porcentaje del valor máximo de contracción, facilitando la comparación entre individuos, músculos y condiciones experimentales. La normalización MVC es particularmente útil en estudios donde se evalúan patrones de fatiga muscular, esfuerzos de contracción, y en aplicaciones de rehabilitación, ya que elimina la variabilidad inherente a cada sujeto y permite analizar la respuesta muscular de forma objetiva.

**2.2  Transformada Wavelet Discreta (DWT) en sEMG**
   
<p align="justify">
La DWT es una herramienta de análisis de señales en los dominios de tiempo y frecuencia, ideal para capturar la variabilidad dinámica de la sEMG debido a su naturaleza transitoria. A diferencia de la Transformada de Fourier, que solo descompone la señal en términos de frecuencia, la DWT permite analizar cambios de frecuencia en función del tiempo, lo que es especialmente útil en señales biológicas como la sEMG, donde la actividad muscular varía en cortos periodos. La DWT descompone la señal en niveles de detalle sucesivos, lo que facilita identificar componentes específicos asociados a diferentes frecuencias de contracción muscular y permite el análisis detallado de eventos como contracciones sostenidas y picos de actividad. En el procesamiento de señales sEMG, la DWT se implementa típicamente usando funciones wavelet como las Daubechies, que son adecuadas para capturar las variaciones suaves y rápidas típicas de las señales biológicas.

**2.3 Extracción de Características**

La extracción de características en el análisis de señales sEMG es un paso crucial para la identificación y clasificación de patrones de activación muscular. Este proceso implica seleccionar y calcular métricas que capturen aspectos relevantes de la señal, facilitando así su análisis y comparación. En el contexto de señales sEMG procesadas mediante la DWT, la extracción de características se centra en resaltar patrones temporales, de frecuencia y, en algunos casos, espaciales, que reflejan la dinámica de la actividad muscular.

- **Características Temporales**: Las características temporales se extraen directamente de la amplitud de la señal sEMG en el dominio del tiempo. Son útiles para cuantificar la intensidad y la variación de la actividad muscular durante la contracción. Algunas de las métricas más utilizadas incluyen:

### Medidas de Señal: RMS e IAV

#### Raíz Cuadrada Media (RMS)
La RMS refleja la amplitud promedio de una señal en un período y se calcula como:

$$
RMS = \sqrt{\frac{1}{N} \sum_{i=1}^{N} x_i^2}
$$

donde $x_i$ representa cada muestra en la ventana de tiempo.

#### Integral Absoluta (IAV)
La IAV es una medida de la intensidad total de una señal en un intervalo y se define como:

$$
IAV = \sum_{i=1}^{N} |x_i|
$$

Esta métrica es útil para comparar niveles de esfuerzo entre contracciones.
  
- **Características de Frecuencia**: Las características de frecuencia analizan la distribución de la energía en diferentes bandas de frecuencia de la señal. Estas métricas son útiles para detectar cambios en la frecuencia asociados con fatiga muscular o diferentes tipos de contracción. Entre las características de frecuencia más comunes se encuentran:

\begin{itemize}
    \item **Frecuencia Media (MNF)**: Representa el promedio de todas las frecuencias en la señal y se calcula como:
    \[
    \text{MNF} = \frac{\sum_{f} f \cdot P(f)}{\sum_{f} P(f)}
    \]
    donde \( P(f) \) es la densidad espectral de potencia en la frecuencia \( f \).
    \item **Frecuencia Mediana (MDF)**: Es el valor de frecuencia que divide el espectro de la señal en dos partes de igual energía. La MDF se utiliza para identificar la fatiga, ya que esta frecuencia tiende a disminuir con la fatiga muscular.
\end{itemize}

- **Características Espaciales**: Las características espaciales se utilizan principalmente en señales HD-sEMG, donde los electrodos están dispuestos en matrices de alta densidad sobre la superficie muscular. Estas características permiten analizar la coordinación y sincronización de diferentes áreas musculares. Un ejemplo es:

\begin{itemize}
    \item **Sincronización Espacial (SS)**: Mide la correlación entre canales adyacentes en la matriz de electrodos, proporcionando información sobre la propagación de la actividad muscular.
\end{itemize}

Estas características temporales, de frecuencia y espaciales proporcionan una representación rica de la señal sEMG, permitiendo analizar la actividad muscular de manera más detallada y con aplicaciones prácticas en el control de prótesis y la rehabilitación muscular.


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
|WAMP: Willison amplitude|
|La amplitud de Willison o amplitud de Wilson (WAMP) es una medida de la información de frecuencia de la señal EMG, similar a la definida en la característica ZC (por ejemplo, Philipson, 1987; Zardoshti-Kermani et al., 1995). Es el número de veces que la diferencia entre la amplitud de la señal EMG entre dos segmentos contiguos supera un umbral predefinido. Además, está relacionada con la activación de los potenciales de acción de las unidades motoras (MUAP) y la fuerza de contracción muscular. [6]| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/WAMP.png">|
|SampEn: Entropía de la muestra|
|La Entropía de Muestra (SampEn) es un método de estimación de entropía utilizado en el análisis de señales biológicas, conocido por su bajo sesgo y alta consistencia. En el ámbito del sEMG, se aplica en el estudio de enfermedades como el accidente cerebrovascular y el Parkinson. SampEn ayuda a identificar la complejidad de las señales EMG, permitiendo diferenciar entre enfermedades neurológicas y personas sanas, así como evaluar trastornos neuromusculares y cambios en las unidades motoras tras un accidente cerebrovascular. [7]| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/SAMPEN.png">|
|Hjorth 2: Movilidad|
|La Hjorth 2 (movilidad o NDS 2) es la raíz cuadrada media (rms) de las pendientes de la señal dividida por la rms de la amplitud. Este segundo NSD se expresa como una relación por unidad de tiempo y puede considerarse como una estimación de la frecuencia media. La complejidad proporciona una medida de la rms de la tasa de cambios en la pendiente en referencia a una forma de curva ideal posible (sabiendo que la complejidad de una onda sinusoidal pura corresponde a uno). También, sirve para el análisis de EEG. [8]| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/Hjorth2.png">|
|Kurt: Kurtosis|
|KURT es una medida del sEMG que puede proporcionar información sobre las propiedades estadísticas de la señal relacionadas con su comportamiento en los picos o colas. Donde \(N\) define el número total de muestras en la señal sEMG, \(s(i)\) representa la amplitud de la señal sEMG en un punto de tiempo específico \(i\), y \(\bar{s}\) denota la media de los valores de la señal sEMG. (9)| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/Kurt.png">|
|SSC: Slope sign change|
|El cambio de signo de la pendiente (SSC) se relaciona con características como ZC, MYOP y WAMP. Este método mide la cantidad de veces que la pendiente de una señal EMG cambia de signo. Se evalúa el número de cambios entre pendientes positivas y negativas en tres segmentos secuenciales, aplicando una función de umbral para minimizar el ruido de fondo. La selección del valor de umbral para las características ZC, MYOP, WAMP y SSC se elige generalmente entre 50 µV y 100 mV, dependiendo de la configuración del instrumento y del ruido ambiental. [6]| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/SSC.png">|
|MDF: Median frequency|
|El MDF (frecuencia de densidad media) se refiere a la frecuencia en la que el espectro se divide en dos áreas con amplitudes iguales; en otras palabras, el MDF equivale a la mitad de la característica TTP. Esto indica que la suma de las probabilidades hasta el MDF es igual a la mitad de la suma total de probabilidades. [6]| <img src="/ISB/Laboratorios/Lab9 - Procesamiento de señal EMG/formulas/MDF.png">|

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

#### Biceps con Oposición Leve

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/B/3.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/B/4.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/B/1.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/B/2.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/B/5.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/B/6.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/B/7.png)|
|MYOP|![Imagen 2](./graficas_EMG/B/8.png)|
|V-Order|![Imagen 2](./graficas_EMG/B/9.png)|
|WAMP|![Imagen 2](./graficas_EMG/B/10.png)|
|SampEn|![Imagen 2](./graficas_EMG/B/11.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/B/12.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/B/13.png)|
|SSC|![Imagen 2](./graficas_EMG/B/14.png)|

#### Biceps con Oposición Fuerte


| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/B/17.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/B/18.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/B/15.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/B/16.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/B/19.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/B/20.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/B/21.png)|
|MYOP|![Imagen 2](./graficas_EMG/B/22.png)|
|V-Order|![Imagen 2](./graficas_EMG/B/23.png)|
|WAMP|![Imagen 2](./graficas_EMG/B/24.png)|
|SampEn|![Imagen 2](./graficas_EMG/B/25.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/B/26.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/B/27.png)|
|SSC|![Imagen 2](./graficas_EMG/B/28.png)|

#### Biceps en Reposo

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/B/31.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/B/32.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/B/29.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/B/30.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/B/33.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/B/34.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/B/35.png)|
|MYOP|![Imagen 2](./graficas_EMG/B/36.png)|
|V-Order|![Imagen 2](./graficas_EMG/B/37.png)|
|WAMP|![Imagen 2](./graficas_EMG/B/38.png)|
|SampEn|![Imagen 2](./graficas_EMG/B/39.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/B/40.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/B/41.png)|
|SSC|![Imagen 2](./graficas_EMG/B/42.png)|




#### Gastrocnemio con Oposición Leve

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/G/45.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/G/46.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/G/43.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/G/44.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/G/47.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/G/48.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/G/49.png)|
|MYOP|![Imagen 2](./graficas_EMG/G/50.png)|
|V-Order|![Imagen 2](./graficas_EMG/G/51.png)|
|WAMP|![Imagen 2](./graficas_EMG/G/52.png)|
|SampEn|![Imagen 2](./graficas_EMG/G/53.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/G/54.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/G/55.png)|
|SSC|![Imagen 2](./graficas_EMG/G/56.png)|

#### Gastrocnemio con Oposición Fuerte


| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/G/59.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/G/60.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/G/57.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/G/58.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/G/61.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/G/62.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/G/63.png)|
|MYOP|![Imagen 2](./graficas_EMG/G/64.png)|
|V-Order|![Imagen 2](./graficas_EMG/G/65.png)|
|WAMP|![Imagen 2](./graficas_EMG/G/66.png)|
|SampEn|![Imagen 2](./graficas_EMG/G/67.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/G/68.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/G/69.png)|
|SSC|![Imagen 2](./graficas_EMG/G/70.png)|

#### Gastrocnemio en Reposo

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/G/73.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/G/74.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/G/71.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/G/72.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/G/75.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/G/76.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/G/77.png)|
|MYOP|![Imagen 2](./graficas_EMG/G/78.png)|
|V-Order|![Imagen 2](./graficas_EMG/G/79.png)|
|WAMP|![Imagen 2](./graficas_EMG/G/80.png)|
|SampEn|![Imagen 2](./graficas_EMG/G/81.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/G/82.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/G/83.png)|
|SSC|![Imagen 2](./graficas_EMG/G/84.png)|



#### Dedo con Oposición Leve

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/D/87.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/D/88.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/D/85.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/D/86.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/D/89.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/D/90.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/D/91.png)|
|MYOP|![Imagen 2](./graficas_EMG/D/92.png)|
|V-Order|![Imagen 2](./graficas_EMG/D/93.png)|
|WAMP|![Imagen 2](./graficas_EMG/D/94.png)|
|SampEn|![Imagen 2](./graficas_EMG/D/95.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/D/96.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/D/97.png)|
|SSC|![Imagen 2](./graficas_EMG/D/98.png)|

#### Dedo con Oposición Fuerte


| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/D/101.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/D/102.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/D/99.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/D/100.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/D/103.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/D/104.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/D/105.png)|
|MYOP|![Imagen 2](./graficas_EMG/D/106.png)|
|V-Order|![Imagen 2](./graficas_EMG/D/107.png)|
|WAMP|![Imagen 2](./graficas_EMG/D/108.png)|
|SampEn|![Imagen 2](./graficas_EMG/D/109.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/D/110.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/D/111.png)|
|SSC|![Imagen 2](./graficas_EMG/D/112.png)|

#### Dedo en Reposo

| Tipo de Señal| Gráficas|
| --- | --- |
|Señal original| ![Imagen 1](./graficas_EMG/D/115.png) |
|Señal filtrada|![Imagen 2](./graficas_EMG/D/116.png) |
|FFT de la señal original|![Imagen 2](./graficas_EMG/D/113.png) |
|FFT de la señal filtrada|![Imagen 2](./graficas_EMG/D/114.png) |
|Señal rectificada|![Imagen 2](./graficas_EMG/D/117.png) |
|RMS y RMS normalizado|![Imagen 2](./graficas_EMG/D/118.png) |
| Características obtenidas| Gráficas|
|MFL|![Imagen 2](./graficas_EMG/D/119.png)|
|MYOP|![Imagen 2](./graficas_EMG/D/120.png)|
|V-Order|![Imagen 2](./graficas_EMG/D/121.png)|
|WAMP|![Imagen 2](./graficas_EMG/D/122.png)|
|SampEn|![Imagen 2](./graficas_EMG/D/123.png)|
|Hjorth2|![Imagen 2](./graficas_EMG/D/124.png)|
|Kurtosis|![Imagen 2](./graficas_EMG/D/125.png)|
|SSC|![Imagen 2](./graficas_EMG/D/126.png)|


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

[6] A. Phinyomark, P. Phukpattaranont, and C. Limsakul, “Feature Reduction and Selection for EMG Signal Classification,” Expert Systems with Applications, vol. 39, no. 8, pp. 7420–7431, Jun. 2012, doi: https://doi.org/10.1016/j.eswa.2012.01.102.

[7] L. Li, X. Wang, B. Yao, X. Zhang, and P. Zhou, “Sample Entropy-Based Surface Electromyographic Examination With a Linear Electrode Array in Survivors With Spinal Cord Injury,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 2944–2952, Jan. 2023, doi: https://doi.org/10.1109/tnsre.2023.3290607.

[8] M. Mouzé-Amady and F. Horwat, “Evaluation of Hjorth parameters in forearm surface EMG analysis during an occupational repetitive task,” Electroencephalography and Clinical Neurophysiology/Electromyography and Motor Control, vol. 101, no. 2, pp. 181–183, Apr. 1996, doi: https://doi.org/10.1016/0924-980X(96)00316-5.

[9] H. Naser and H. A. Hashim, “sEMG-Based Hand Gestures Classification Using a semi-supervised multi-layer Neural Networks with Autoencoder,” Systems and Soft Computing, vol. 6, pp. 200144–200144, Sep. 2024, doi: https://doi.org/10.1016/j.sasc.2024.200144.


