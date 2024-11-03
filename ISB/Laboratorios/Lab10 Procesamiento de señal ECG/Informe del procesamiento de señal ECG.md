# Análisis y Procesamiento de Señal ECG

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
<p style="font-size: 4px;">
El electrocardiograma (ECG) es una herramienta fundamental en la práctica médica moderna para el diagnóstico y monitoreo de enfermedades cardiovasculares, una de las principales causas de mortalidad a nivel mundial [1]. Su facilidad de uso y naturaleza no invasiva lo convierten en un método eficiente para detectar irregularidades en el ritmo y la morfología del latido cardíaco, permitiendo identificar condiciones como arritmias, hipertensión y enfermedades isquémicas [2]. La interpretación precisa de estas señales es crítica en contextos de alto riesgo, donde la detección temprana de anomalías puede prevenir complicaciones graves e incluso salvar vidas.
</p>

El procesamiento automatizado de señales de ECG ha cobrado importancia con el avance de técnicas de procesamiento de señales y algoritmos de inteligencia artificial, que mejoran la precisión en la detección de patrones cardíacos [3]. Sin embargo, la complejidad intrínseca de las señales de ECG, afectadas por factores externos y variabilidad morfológica, supone un desafío significativo para la interpretación computacional [4]. 

La detección del complejo QRS, que representa la despolarización ventricular, es un elemento esencial en el análisis de ECG. Algoritmos como el de Pan y Tompkins, que utilizan filtros digitales y umbrales adaptativos, siguen siendo ampliamente empleados por su eficacia en mejorar la precisión de detección bajo condiciones de ruido [5]. Más recientemente, los avances en inteligencia artificial han facilitado la implementación de modelos de clasificación en tiempo real, particularmente útiles en telemedicina y dispositivos portátiles [6]. 

Este informe explora los métodos actuales de procesamiento de señales de ECG, abarcando enfoques tradicionales y sistemas basados en aprendizaje automático. Se revisan las etapas clave en el procesamiento de la señal y se analizan las metodologías empleadas para su implementación en sistemas de monitoreo en tiempo real, proporcionando una visión integral del estado actual y las direcciones futuras en el análisis automatizado de ECG para aplicaciones diagnósticas.

## 2. Marco Teórico

### 1 Filtrado y Eliminación de Ruido

El procesamiento de señales de ECG implica una serie de etapas que permiten convertir los datos crudos en información significativa para su interpretación clínica. La señal de ECG, que consiste en la captura de los impulsos eléctricos del corazón, requiere técnicas avanzadas de procesamiento para eliminar el ruido y resaltar características clave, como el complejo QRS, que son esenciales para el diagnóstico de condiciones cardíacas [2]. Los algoritmos clásicos se centran en la filtración de ruido, identificación de puntos críticos y extracción de características temporales y frecuenciales.

### 1.1 Filtrado y Eliminación de Ruido

Dado que las señales de ECG están expuestas a varios tipos de ruido (como interferencia de línea de potencia y movimiento muscular), el filtrado es un paso esencial. Los filtros digitales de banda pasante son comunes, ya que reducen la interferencia sin distorsionar las características morfológicas de la señal [5]. Además, la transformada wavelet se ha utilizado para descomponer la señal en diferentes escalas, facilitando la identificación de componentes de alta y baja frecuencia relevantes [3].

### 1.2 Detección del Complejo QRS

La detección del complejo QRS es fundamental, ya que representa la actividad de los ventrículos y proporciona información sobre el ritmo cardíaco. Los métodos tradicionales, como el algoritmo de Pan y Tompkins, emplean filtros de banda pasante, diferenciación y umbrales adaptativos para identificar el complejo QRS incluso en condiciones de ruido [4]. Estudios posteriores han optimizado estos métodos utilizando transformadas de wavelet y técnicas de procesamiento en tiempo real [2].

## 2. Inteligencia Artificial y Aprendizaje Automático en ECG

La integración de técnicas de inteligencia artificial ha permitido un avance significativo en el análisis de ECG. Algoritmos de aprendizaje profundo pueden clasificar automáticamente los patrones cardíacos al entrenarse con grandes conjuntos de datos. Estos modelos son especialmente útiles para el diagnóstico de arritmias y otras anomalías en aplicaciones de telemedicina, donde se requiere monitoreo continuo y detección en tiempo real [6].

### 2.1 Extracción de Características

La extracción de características permite reducir la dimensionalidad de los datos y enfocarse en patrones específicos de la señal ECG, como los intervalos de latido y las características morfológicas del complejo P-QRS-T [1]. Los métodos tradicionales emplean transformadas en el dominio del tiempo y frecuencia, mientras que los modelos actuales utilizan redes neuronales convolucionales para extraer automáticamente características de interés [3].

### 2.2 Clasificación y Detección de Anomalías

Los modelos de clasificación supervisados, como redes neuronales y máquinas de soporte vectorial, han demostrado ser efectivos en la detección de arritmias y otras condiciones a partir de señales de ECG. Además, los modelos basados en aprendizaje profundo, como el aprendizaje por transferencias y redes neuronales recurrentes, han mostrado un rendimiento robusto en la clasificación de patrones complejos en señales de ECG [6].

## 3. Objetivos

### Objetivo General

- Evaluar y analizar los métodos de procesamiento de señales de ECG, destacando tanto los enfoques tradicionales como los modernos basados en inteligencia artificial, con el propósito de identificar mejoras en la precisión y eficacia en la detección de anomalías cardíacas.

### Objetivos Específicos

1. Describir las técnicas de filtrado y eliminación de ruido en señales de ECG y evaluar su efectividad en la detección precisa del complejo QRS.
2. Analizar los métodos de extracción de características y clasificación en señales de ECG y su aplicación en el diagnóstico de enfermedades cardíacas.
3. Evaluar el impacto de los algoritmos de inteligencia artificial en el procesamiento de señales de ECG, especialmente en aplicaciones de telemedicina y dispositivos portátiles.
4. Identificar los desafíos y limitaciones en el procesamiento automatizado de ECG y proponer áreas de investigación futura que puedan mejorar la detección de condiciones cardíacas en entornos clínicos y domésticos.

## 4. Materiales y equipos 


<div align="center">

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| NeuroKit2 | - | -       |
|       -       |   Laptop o PC | 1        |

</div>
<p align="justify">

<p align="justify">
 
## 5. Metodología

## Metodología para Preprocesamiento y Análisis de Señal ECG usando NeuroKit2

En este documento se describe la metodología para procesar y analizar una señal de ECG utilizando la librería **NeuroKit2** en Python. Esta librería facilita el procesamiento de señales neurofisiológicas mediante funciones específicas para la limpieza y el análisis de datos de ECG. 

### 1. Preparación e Instalación

Para comenzar, instala la librería **NeuroKit2** y otras necesarias como `matplotlib` y `pandas`.

- **Instalación de NeuroKit2**: 
  ```python
  pip install neurokit2

Importación de librerías: A continuación, importa las librerías requeridas:

  import neurokit2 as nk
  import matplotlib.pyplot as plt
  import pandas as pd

### 2. Carga y conversión de los Datos de ECG
Es importante que los datos estén organizados en un formato adecuado (por ejemplo, en un archivo CSV) y que la señal de ECG esté contenida en una columna específica.
   - Carga la señal de ECG desde un archivo CSV u otro formato compatible:
     ```python
     data = pd.read_csv("ruta/a_tu_archivo.csv")
     ecg_signal = data["ECG"]  # Cambia "ECG" por el nombre de la columna en tu archivo
     ```
Este código lee los datos desde un archivo CSV y almacena la señal de ECG en la variable ecg_signal.

Para la conversión digital de los datos de la señal ecg se usa una función de transferencia disponible en el manual ECG del BITalino [7], donde se nos indica la conversión de las muestras para medirlas en mV.

<p align="center">
 <img src="./imagenes/transfer_ecg.png" alt="Gráfico de ECG" width="230" height="100"/>
</p>

- Donde ADC sería la señal, 1024 sería la resolución de 10 bits, el VCC sería 3.3V y la ganancia del sensor sería 1100. Dándonos como resultado la señal en V, para luego multiplicarlo por 1000 y obtener, finalmente, la señal en mV.
  ```python
  ecg_signal = (((ecg_signal/1024)-0.5)*3.3)/(1100) # Datos en V
  ecg_signal = ecg_signal * 1000 # Datos en mV
  ```

### 3. Preprocesamiento de la Señal ECG
El preprocesamiento es fundamental para reducir el ruido en la señal de ECG. NeuroKit2 proporciona la función ecg_clean(), que filtra la señal automáticamente.

Objetivo: Limpiar la señal de ECG para remover artefactos y ruido.
```python
ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=1000)  # Ajusta la tasa de muestreo a la de tus datos
```

La función ecg_clean() aplica filtros y suaviza la señal de ECG, eliminando el ruido. La tasa de muestreo (sampling_rate) debe coincidir con la tasa de los datos originales.

### 4. Análisis de la Señal ECG
El siguiente paso es extraer características específicas de la señal de ECG, como la frecuencia cardíaca y la variabilidad de la frecuencia cardíaca (HRV), mediante la función ecg_analyze().

Objetivo: Calcular características clave de la señal.
```python
ecg_analysis = nk.ecg_analyze(ecg_cleaned, sampling_rate=1000)
```
La función ecg_analyze() permite obtener métricas importantes de la señal, como la frecuencia cardíaca promedio y la HRV. Estos datos son útiles en estudios de salud y diagnóstico.

### 5. Procesamiento Completo con `ecg_process()`
Para simplificar el flujo de trabajo, NeuroKit2 ofrece la función ecg_process(), que combina el preprocesamiento y el análisis de la señal en una sola llamada.

Objetivo: Realizar el preprocesamiento y análisis completo de una sola vez.
```python
signals, info = nk.ecg_process(ecg_signal, sampling_rate=1000)
```
ecg_process() integra ecg_clean() y ecg_analyze() y devuelve dos elementos: signals, que contiene la señal limpia y procesada, y info, un diccionario con detalles y métricas sobre la señal.

### 6. Visualización de Resultados
Para visualizar los datos y verificar el procesamiento, utiliza ecg_plot().

Código para visualizar:
```python
nk.ecg_plot(signals, sampling_rate=1000)
plt.show()
```
La gráfica permite observar la señal limpia, mostrando los picos R y las fases cardíacas. Esto es útil para validar visualmente el preprocesamiento y los resultados de la detección de picos.

### 7. Análisis e Interpretación de los Datos
El objeto info contiene métricas clave como la frecuencia cardíaca promedio y HRV, que se pueden extraer y analizar.
Ejemplo de extracción de métricas:
```python
print("Frecuencia cardíaca promedio:", info["Heart_Rate_Mean"])
print("HRV (RMSSD):", info["HRV_RMSSD"])
```
#### HRV
Es la variabilidad de la frecuencia cardiaca, una medida de las pequeñas variaciones en el tiempo, los llamados intervalos R-R, entre cada latido del corazón. Su ánalisis corresponde a evaluar como el cuerpo responde al estrés, un valor alto indicado un cuerpo bien regulado y uno bajo, es signo de estrés o fatiga [8, 9].

- HRV_SDNN:
Representa la desviación estándar de los intervalos NN (intervalos entre latidos sucesivos), siendo una variabilidad a su vez de los intervalos RR, midiendo cómo varían estos respecto a un valor promedio en un periodo largo [8, 9].

- HRV_RMSSD:
Representa la raíz cuadrada de la media de las diferencias al cuadrado entre intervalos sucesivos, es decir, mide las variaciones rápida de latido a latido evaluando la actividad del sistema parasimpático [8, 9].

####ECG rate mean
Es la frecuencia cardiaca media calculada durante un tiempo específico y es útil para conocer el estado de reposo y actividad del corazón.

Estas métricas permiten interpretar el estado de salud del sujeto y son útiles para investigaciones en fisiología y salud.

### 8. Conclusión y Reportes
Finalmente, en el informe, resume los resultados clave obtenidos, destacando el impacto del preprocesamiento en la señal y cualquier patrón relevante en las métricas, como la frecuencia cardíaca y la HRV.

Resumen de puntos clave:
 - Preprocesamiento exitoso de la señal ECG.
 - Análisis y obtención de métricas relevantes.
 - Visualización y validación de resultados.
Incluye gráficos y observaciones sobre la calidad de la señal, haciendo énfasis en la eficacia del preprocesamiento y los resultados obtenidos con NeuroKit2.

Nota: Esta metodología sigue las mejores prácticas de NeuroKit2 para asegurar un procesamiento reproducible y eficiente de señales neurofisiológicas, ofreciendo una implementación simplificada para el análisis de ECG.


<p align="justify">
## 6. Resultados y discusiones
#### ECG originales: ecg_plot()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8.png) |
 
#### Preprocesamiento: ecg_clean()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9_b.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10_b.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11_b.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1_b.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2_b.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3_b.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12_b.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13_b.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14_b.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4_b.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5_b.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6_b.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15_b.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16_b.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7_b.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8_b.png) |
 
#### Análisis: ecg_analyze()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9_e.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10_e.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11_e.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1_e.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2_e.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3_e.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12_e.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13_e.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14_e.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4_e.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5_e.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6_e.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15_e.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16_e.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7_e.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8_e.png) |
 
#### Preprocesamiento y Análisis: ecg_process()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9_a.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10_a.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11_a.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1_a.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2_a.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3_a.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12_a.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13_a.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14_a.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4_a.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5_a.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6_a.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15_a.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16_a.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7_a.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8_a.png) |
 
#### Compute Signal Rate: ecg_rate()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9_c.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10_c.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11_c.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1_c.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2_c.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3_c.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12_c.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13_c.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14_c.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4_c.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5_c.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6_c.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15_c.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16_c.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7_c.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8_c.png) |
 
#### Respiración derivada de ECG (EDR): ecg_rsp()
 | Señales | Gráficas|
 | --- | --- |
 |Reposo 1ra derivada|![Imagen 1](./imagenes/ECG_9_d.png)  |
 |Reposo 2da derivada|![Imagen 1](./imagenes/ECG_10_d.png)  |
 |Reposo 3ra derivada|![Imagen 1](./imagenes/ECG_11_d.png)  |
 |Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_1_d.png) |
 |Respiración 2da derivada|![Imagen 2](./imagenes/ECG_2_d.png) |
 |Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_3_d.png) |
 |Sin Respiración 1ra derivada|![Imagen 1](./imagenes/ECG_12_d.png) |
 |Sin Respiración 2da derivada|![Imagen 2](./imagenes/ECG_13_d.png) |
 |Sin Respiración 3ra derivada|![Imagen 3](./imagenes/ECG_14_d.png) |
 |Ejercicio 1ra derivada|![Imagen 1](./imagenes/ECG_4_d.png) |
 |Ejercicio 2da derivada|![Imagen 2](./imagenes/ECG_5_d.png) |
 |Ejercicio 3ra derivada|![Imagen 3](./imagenes/ECG_6_d.png) |
 |Simulación a 60bpm|![Imagen 2](./imagenes/ECG_15_d.png) |
 |Simulación a 90bpm|![Imagen 3](./imagenes/ECG_16_d.png) |
 |Simulación a 120bpm|![Imagen 2](./imagenes/ECG_7_d.png) |
 |Simulación a 150bpm|![Imagen 3](./imagenes/ECG_8_d.png) |


## 7. Discusiones
La función ecg_clean() de NeuroKit2 demostró ser eficaz en la eliminación de ruidos en la señal de ECG, especialmente frente a artefactos comunes como el ruido de línea de potencia y el movimiento muscular. Esto resultó en una señal más clara que facilita la identificación de complejos QRS sin afectar la estructura morfológica de la señal, aunque es importante ajustar parámetros como la tasa de muestreo para optimizar los resultados según el origen y la calidad de los datos iniciales. Además, el uso de la transformada wavelet para descomponer la señal en escalas permitió distinguir componentes de alta y baja frecuencia, lo cual fue esencial para mejorar la precisión en la detección del complejo QRS, incluso en presencia de ruidos de baja frecuencia. Esta técnica representa un avance respecto a métodos de filtrado tradicionales en ECG, ya que permite reducir interferencias específicas.

Por otra parte, la función ecg_analyze() permitió extraer métricas relevantes de variabilidad de la frecuencia cardíaca (HRV), como el RMSSD, un indicador de la variabilidad cardíaca en el tiempo que refleja respuestas fisiológicas del sistema autónomo y puede ser útil para el diagnóstico de arritmias o la evaluación de la respuesta al estrés. Sin embargo, la calidad de estos indicadores depende de un preprocesamiento adecuado, lo que subraya la importancia de eliminar correctamente el ruido en la señal inicial.

Finalmente, aunque NeuroKit2 ofrece una metodología de procesamiento estandarizada que es rápida y reproducible, presenta limitaciones en señales con niveles de ruido particularmente altos o en individuos con alta variabilidad interindividual. Para mejorar la precisión en estos casos, sería conveniente explorar el uso de filtros más especializados o de técnicas de aprendizaje automático que ajusten el procesamiento a las características específicas de cada paciente.


## 7. Conclusiones
Las funciones de preprocesamiento de NeuroKit2, como ecg_clean() y ecg_process(), facilitan un procesamiento rápido y estandarizado de señales de ECG, lo cual es ideal para aplicaciones de telemedicina y dispositivos portátiles debido a su eficiencia y facilidad de uso. La metodología utilizada permitió una detección confiable del complejo QRS incluso en condiciones de ruido moderado, destacándose la efectividad de la transformada wavelet en mejorar la precisión para el diagnóstico de arritmias y otras anomalías cardíacas. Además, NeuroKit2 permite la extracción automática de métricas clave para el monitoreo continuo de la salud cardíaca, lo cual facilita tanto el diagnóstico temprano como el monitoreo en tiempo real de la respuesta fisiológica del paciente. Para mejorar aún más estos resultados, se recomienda explorar la integración de algoritmos de aprendizaje automático, como redes neuronales, los cuales podrían optimizar la clasificación de patrones de ECG en escenarios clínicos complejos.

## 8. Referencias Bibliográficas

1. V. A. Ardeti, V. R. Kolluru, G. T. Varghese, y R. K. Patjoshi, "An overview on state-of-the-art electrocardiogram signal processing methods: Traditional to AI-based approaches," *Expert Systems With Applications*, vol. 217, 2023, pp. 119561.  
2. A. K. Singh y S. Krishnan, "ECG signal feature extraction trends in methods and applications," *BioMedical Engineering OnLine*, vol. 22, 2023.  
3. E. J. da S. Luz, W. R. Schwartz, G. Cámara-Chávez, y D. Menotti, "ECG-based heartbeat classification for arrhythmia detection: A survey," *Computer Methods and Programs in Biomedicine*, vol. 127, 2016, pp. 144–164.  
4. J. Pan y W. J. Tompkins, "A Real-Time QRS Detection Algorithm," *IEEE Transactions on Biomedical Engineering*, vol. BME-32, no. 3, 1985, pp. 230–236.  
5. P. Hamilton, "Open source ECG analysis," *Computers in Cardiology*, vol. 29, 2002, pp. 101–104.  
6. D. Makowski, T. Pham, Z. J. Lau, et al., "NeuroKit2: A Python toolbox for neurophysiological signal processing," *Behavior Research Methods*, vol. 53, 2021, pp. 1689–1696.
7. “BITalino documentation.” https://support.pluxbiosignals.com/knowledge-base/bitalino-documentation/
8. Welltory, “RMSSD and other HRV measurements,” Welltory, Dec. 22, 2022. https://welltory.com/rmssd-and-other-hrv-measurements/
9. F. Shaffer and J. P. Ginsberg, “An overview of heart rate variability metrics and norms,” Frontiers in Public Health, vol. 5, Sep. 2017, doi: 10.3389/fpubh.2017.00258.

