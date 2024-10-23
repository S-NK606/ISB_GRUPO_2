# INFORME LABORATORIO 8 - TRANSFORMADA WAVELET 

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
3. [Objetivos](#3-objetivos)
4. [Materiales y equipos](#4-materiales-y-equipos)
5. [Metodología](#5-metodología)
6. [Conclusiones](#6-conclusiones)
7. [Referencias bibliográficas](#7-referencias-bibliográficas)


## 1. Introducción

<div style="text-align: justify;">

En el ámbito de la ingeniería biomédica, el procesamiento de señales biomédicas juega un papel fundamental para el análisis, diagnóstico y monitoreo de diversas condiciones clínicas. Las señales biomédicas como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) contienen información valiosa sobre el estado fisiológico de los sistemas cardiovascular, muscular y cerebral, respectivamente. Sin embargo, estas señales suelen estar contaminadas por ruido y artefactos, lo que dificulta su análisis directo. En este contexto, las transformadas matemáticas, específicamente la transformada wavelet, han emergido como una herramienta poderosa para el procesamiento y análisis de estas señales complejas.

La transformada wavelet permite descomponer una señal en componentes de frecuencia y tiempo, lo que resulta en una representación multiresolución que es especialmente útil para la detección de eventos transitorios y la identificación de características en señales no estacionarias, como las biomédicas. A diferencia de la transformada de Fourier, que solo ofrece una visión global de la frecuencia, la transformada wavelet ofrece una flexibilidad adicional para estudiar señales con componentes de baja y alta frecuencia en diferentes momentos, lo cual es esencial para detectar anomalías en señales biomédicas [1]. En aplicaciones como el ECG, se ha demostrado que las transformadas wavelet son efectivas para la eliminación de ruido de alta frecuencia y para la detección de complejos QRS [2]. De igual manera, en el análisis de EMG, las wavelets permiten separar con precisión los patrones de activación muscular de los artefactos de movimiento [3], y en el caso del EEG, facilitan la identificación de ondas cerebrales anormales asociadas con epilepsia o trastornos del sueño [4].

En este informe, se abordará el uso de las transformadas wavelet en el procesamiento de señales biomédicas, con un enfoque en las señales ECG, EMG y EEG. Se discutirán los beneficios y limitaciones de su aplicación, así como ejemplos específicos de su implementación en estudios recientes.

</div>

## 2. Marco teórico

## 3. Objetivos

### Objetivo general
Evaluar el uso de la transformada wavelet en el procesamiento de señales biomédicas, específicamente en señales de electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG), con el fin de optimizar la detección de patrones fisiológicos y patológicos.

### Objetivos específicos
1. **Analizar la aplicación de la transformada wavelet en el procesamiento de señales ECG** para la identificación y detección precisa de los complejos QRS y eliminación de artefactos de ruido.
   
2. **Explorar el uso de la transformada wavelet en señales EMG** para separar patrones de activación muscular de artefactos y ruido, permitiendo un análisis más robusto de la actividad muscular en diferentes condiciones fisiológicas.

3. **Investigar la implementación de la transformada wavelet en señales EEG** para la identificación de eventos transitorios y anómalos, como ondas cerebrales características en condiciones como la epilepsia.

4. **Revisar estudios previos y actuales** sobre la aplicación de la transformada wavelet en señales biomédicas, para identificar mejoras potenciales en algoritmos de procesamiento que puedan ser implementados en dispositivos biomédicos de diagnóstico.


## 4. Materiales y equipos

## 5. Metodología
**Recolección de datos**
Para este estudio, se utilizaron datasets correspondientes a señales de electromiograma (EMG), electrocardiograma (ECG) y electroencefalograma (EEG). Estas señales, obtenidas en laboratorios previos, contienen información valiosa sobre la actividad fisiológica de músculos, corazón y cerebro, respectivamente, pero están contaminadas por diversos tipos de ruido.

### 5.1. Análisis de Señales ECG

*Preprocesamiento*

Antes de aplicar la Transformada Wavelet Discreta (DWT), cada señal fue filtrada utilizando técnicas de **filtro de paso bajo** y **filtro de paso alto** para mitigar el ruido de alta y baja frecuencia, respectivamente. Estos filtros son esenciales para eliminar interferencias como el ruido de línea base y los artefactos electromagnéticos, comunes en las señales biomédicas.

*Transformada Wavelet Discreta (DWT)*

La DWT fue aplicada para descomponer las señales en distintos niveles de resolución. Esta técnica permite separar las componentes de alta y baja frecuencia en diferentes escalas temporales, facilitando la identificación de patrones y la eliminación de ruido.

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
Se probaron varias funciones madre wavelet, como la wavelet de Daubechies, Coiflets y Symlets, para seleccionar la más adecuada para cada tipo de señal biomédica. La selección se basó en la **relación señal-ruido (SNR)** obtenida tras el procesamiento de la señal.

#### Descomposición y Umbralización
Cada señal fue descompuesta en **niveles de detalle (coeficientes D)** y **niveles de aproximación (coeficientes A)**. Se utilizó un esquema de **umbralización adaptativa** para reducir los coeficientes de detalle asociados al ruido, manteniendo la información relevante de la señal original. La fórmula para la umbralización suave aplicada a los coeficientes \( w \) es:

$$
w' = \text{sign}(w) \cdot \max(|w| - \lambda, 0)
$$

Donde:
- $$\( \lambda \)$$ es el umbral adaptativo, calculado para minimizar el ruido sin eliminar información relevante de la señal.
  
### Reconstrucción de la señal
Tras eliminar los coeficientes de ruido, se realizó la **transformada inversa de la DWT** para reconstruir la señal filtrada. La reconstrucción se hace sumando los coeficientes de detalle y aproximación modificados, preservando la estructura original de la señal.

#### Fórmula de la DWT inversa
La señal original \( x(t) \) se puede reconstruir mediante la DWT inversa usando la siguiente expresión:

$$
x(t) = \sum_{j} \sum_{k} W_{\psi}(a_j, b_k) \psi_{a_j, b_k}(t)
$$

Donde $$\( W_{\psi}(a_j, b_k) \)$$ son los coeficientes wavelet calculados en el proceso de descomposición.

### Métricas de evaluación

Para evaluar la calidad de la señal tras la eliminación del ruido, se utilizaron las siguientes métricas:

1. **Relación Señal-Ruido (SNR)**:

   $$\text{SNR} = 10 \log_{10} \left(\frac{\sum_{i=1}^{N} x_i^2}{\sum_{i=1}^{N} (x_i - \hat{x}_i)^2}\right)$$

2. **Error cuadrático medio (RMSE)**:

   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \hat{x}_i)^2}$$
   
Estas métricas permitieron comparar la señal original con la señal procesada, evaluando la efectividad de la DWT en la eliminación de ruido y preservación de la información relevante.


### 5.2. Análisis de Señales EMG
### 1. Recolección de Datos
Se recopilaron señales de electromiografía (EMG) utilizando electrodos superficiales en músculos específicos. Las señales se obtuvieron durante diversas actividades motoras, en laboratorios previos.

### 2. Adición de Ruido
Se añadió *ruido gaussiano blanco* a las señales EMG originales para simular condiciones reales de ruido. Los niveles de *relación señal a ruido (SNR)* utilizados fueron:
- SNR = 10 dB
- SNR = 15 dB
- SNR = 50 dB

### 3. Procesamiento de Señales

#### 3.1. Transformada Wavelet Discreta (DWT)
Se aplicó la *Transformada Wavelet Discreta (DWT)* para descomponer las señales EMG en componentes de tiempo y frecuencia, utilizando la siguiente fórmula:

$$
X(a, b) = \int x(t) \frac{1}{\sqrt{|a|}} \psi\left(\frac{t-b}{a}\right) dt
$$

Donde:
- $$\( x(t) \)$$ es la señal EMG.
- $$\( \psi(t) \)$$ es la *función wavelet madre*.
- $$\( a \)$$ es el factor de *escala*.
- $$\( b \)$$ es el factor de *traslación*.

#### 3.2. Umbralización
Se emplearon dos tipos de umbralización en los coeficientes wavelet:
1. *Umbralización dura*:
   
   $$w' = w \ \text{si } |w| \geq \lambda, \ 0 \ \text{si } |w| < \lambda$$

   
3. *Umbralización suave*:
   
   $$w' = \text{sign}(w) \cdot \max(|w| - \lambda, 0)$$

Donde:
- $$\( w \)$$ son los coeficientes wavelet.
- $$\( \lambda \)$$ es el *valor del umbral* adaptado según el ruido en la señal.

### 4. Reconstrucción de la Señal
Una vez aplicada la umbralización, se utilizó la *Transformada Inversa de Wavelet (IDWT)* para reconstruir la señal. La fórmula para la reconstrucción es:

$$x(t) = \sum_{a, b} X(a, b) \psi_{a, b}(t)$$

Donde $$\( X(a, b) \)$$ son los coeficientes wavelet umbralizados y \( \psi_{a, b}(t) \) son las wavelets escaladas y trasladadas.

### 5. Evaluación de la Calidad
La calidad de las señales denoised se evaluó utilizando las siguientes métricas:

1. *Relación Señal-Ruido (SNR)*:
   
   $$\text{SNR} = 10 \log_{10} \left(\frac{\text{Potencia de la señal}}{\text{Potencia del ruido}}\right)$$

3. *Error Cuadrático Medio (MSE)*:
   
   $$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (x_i - \hat{x}_i)^2$$

Donde:
- $$\( x_i \)$$ son los valores de la señal original.
- $$\( \hat{x}_i \)$$ son los valores de la señal reconstruida.

###RESULTADOS
La segundas señales son intervalos para que se pueda ver mejor la señal

#### EMG - Biceps braquial en reposo

| Señal original | Señal filtrada |
| --- | --- |
| ![Imagen 1](./WAVELET_EMG/EMG1_1.png) | ![Imagen 2](./WAVELET_EMG/EMG1_2.png) |
| ![Imagen 1](./WAVELET_EMG/EMG1_3.png) | ![Imagen 2](./WAVELET_EMG/EMG1_4.png) |


#### EMG - Biceps braquial con oposición leve

| Señal original | Señal filtrada |
| --- | --- |
| ![Imagen 1](./WAVELET_EMG/EMG2_1.png) | ![Imagen 2](./WAVELET_EMG/EMG2_2.png) |
| ![Imagen 1](./WAVELET_EMG/EMG2_3.png) | ![Imagen 2](./WAVELET_EMG/EMG2_4.png) |


#### EMG - Biceps braquial con oposición fuerte
| Señal original | Señal filtrada |
| --- | --- |
| ![Imagen 1](./WAVELET_EMG/EMG3_1.png) | ![Imagen 2](./WAVELET_EMG/EMG3_2.png) |
| ![Imagen 1](./WAVELET_EMG/EMG3_3.png) | ![Imagen 2](./WAVELET_EMG/EMG3_4.png) |



### 5.3. Análisis de Señales EEG


## 6. Conclusiones

## 7. Referencias bibliográficas

[1] M. Akay, "Wavelets in Biomedical Engineering," Annals of Biomedical Engineering, vol. 23, no. 5, pp. 531-542, doi: 10.1007/BF02584453.

[2] T. Sharma and K. K. Sharma, "QRS Complex Detection in ECG Signals Using the Synchrosqueezed Wavelet Transform," IETE Journal of Research, vol. 62, no. 6, pp. 885-892, Nov.-Dec. 2016, doi: 
    10.1080/03772063.2016.1221744.

[3] P. Zandiyeh, L. R. Parola, B. C. Fleming, and J. E. Beveridge, "Wavelet analysis reveals differential lower limb muscle activity patterns long after anterior cruciate ligament reconstruction," *Journal of Biomechanics*, vol. 133, p. 110957, 2022, doi: 10.1016/j.jbiomech.2022.110957.

[4] S. Mallat, "Chapter 3 - Discrete Revolution," in *A Wavelet Tour of Signal Processing*, 3rd ed., San Diego, CA, USA: Academic Press, 2009, pp. 59-88, doi: 10.1016/B978-0-12-374370-1.00007-0. 


