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
## 5. Metodología
## 6. Resultados y discusiones
## 7. Conclusiones
## 8. Referencias Bibliográficas

1. V. A. Ardeti, V. R. Kolluru, G. T. Varghese, y R. K. Patjoshi, "An overview on state-of-the-art electrocardiogram signal processing methods: Traditional to AI-based approaches," *Expert Systems With Applications*, vol. 217, 2023, pp. 119561.  
2. A. K. Singh y S. Krishnan, "ECG signal feature extraction trends in methods and applications," *BioMedical Engineering OnLine*, vol. 22, 2023.  
3. E. J. da S. Luz, W. R. Schwartz, G. Cámara-Chávez, y D. Menotti, "ECG-based heartbeat classification for arrhythmia detection: A survey," *Computer Methods and Programs in Biomedicine*, vol. 127, 2016, pp. 144–164.  
4. J. Pan y W. J. Tompkins, "A Real-Time QRS Detection Algorithm," *IEEE Transactions on Biomedical Engineering*, vol. BME-32, no. 3, 1985, pp. 230–236.  
5. P. Hamilton, "Open source ECG analysis," *Computers in Cardiology*, vol. 29, 2002, pp. 101–104.  
6. D. Makowski, T. Pham, Z. J. Lau, et al., "NeuroKit2: A Python toolbox for neurophysiological signal processing," *Behavior Research Methods*, vol. 53, 2021, pp. 1689–1696.  

