# **PROCESAMIENTO DE SEÑALES DE ECG Y EMG MEDIANTE FILTROS DIGITALES**
Este trabajo ha sido hecho de forma individual.

## **INTRODUCCIÓN**

Para el presente trabajo se usaron señales ECG y EMG procedentes de laboratorios anteriores presentes en este mismo GitHub. Las señales seleccionadas son de distintos tipos de medición.

### **Señales ECG**

Las señales registradas fueron de diferentes momentos donde se usó diferentes configuraciones de derivaciones. Específicamente, para el análisis del filtro ECG usaremos las pertenecientes a la tercera derivación de las siguientes etapas: estado basal, estado de reposo medido; estado de pausa respiratoria, donde se registró el ECG después de que el estudiante mantuvo su respiración 10 segundos; y por último, el estado después de una actividad física, ECG registrado después de 5 minutos de actividad física.

Para su procesamiento se recurrió a tres distintos filtros. El primero es un filtro IIR de tipo Butterworth pasa bajas con una frecuencia de corte de 20 Hz. El segundo también es un tipo de filtro IIR de tipo Butterworth pasa banda con una frecuencia de 1 Hz a 100 Hz. Por último un filtro FIR de tipo Butterworth rechaza banda de frecuencias de 60 Hz, usando una ventana de Blackman.

### **Señales EMG**

Las señales registradas fueron de diferentes músculos: biceps braquial, el aductor del pulgar y el gastrocnemio, durante distintas fases de actividad. Específicamente, para el análisis del filtro EMG usaremos las señales del biceps braquila durante las fases de reposo, sin ningún movimiento; oposición leve, donde el estudiante hizo fuerza ligeramente; y oposición fuerte, donde el estudiante usó toda su fuerza contra la oposición.

Para su procesamiento se recurrió a tres distintos filtros. El primero es un filtro IIR de tipo Butterworth pasa bajas con una frecuencia de corte de 400 Hz. El segundo también es un tipo de filtro IIR de tipo Butterworth pasa bandas con una frecuencia de 20 Hz a 500Hz. Por último un filtro FIR de tipo Butterworth rechaza banda de frecuencias de 60 Hz, usando una ventana de Blackman.

## **ANÁLISIS Y FILTRADO DE LAS SEÑALES**

### **SEÑALES ECG**

**1\. ESTADO BASAL \- III DERIVACIÓN**

### 

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/ECG1.png)  | ![Texto alternativo](Imagenes/FFT_ECG1.png)  | ![Texto alternativo](Imagenes/STFT_ECG1.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/ECG1_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_ECG1_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_ECG1_FILTRO1.png) |                             |                                             |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/ECG1_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_ECG1_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_ECG1_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/ECG1_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_ECG1_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_ECG1_FILTRO3.png) |  

###

**2\. ESTADO DE PAUSA RESPIRATORIA \- III DERIVACIÓN**

### 

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/ECG2.png)  | ![Texto alternativo](Imagenes/FFT_ECG2.png)  | ![Texto alternativo](Imagenes/STFT_ECG2.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/ECG2_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_ECG2_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_ECG2_FILTRO1.png) |                             |                                             |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/ECG2_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_ECG2_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_ECG2_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/ECG2_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_ECG2_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_ECG2_FILTRO3.png) |  

###

**3\. ESTADO DESPUÉS DE ACTIVIDAD FÍSICA \- III DERIVACIÓN**

### 

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/ECG3.png)  | ![Texto alternativo](Imagenes/FFT_ECG3.png)  | ![Texto alternativo](Imagenes/STFT_ECG3.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/ECG3_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_ECG3_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_ECG3_FILTRO1.png) |                             |                                             |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/ECG3_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_ECG3_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_ECG3_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/ECG3_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_ECG3_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_ECG3_FILTRO3.png) |  

Analizando cada señal de ECG junto con cada filtro podemos llegar a observaciones generales. En primer lugar, las señales elegidas sí poseen un patrón típico de ECG mostrando a su vez la distorsión que poseen estas por el ruido producido. En segundo lugar, el filtro pasabajas es aquel que suaviza más la señal al eliminar los componentes de alta frecuencia que, con un análisis mayor podríamos determinar si se está perdiendo o no información, pero por la gráfica parece que no al dotarle de una morfología más cercana a lo que es un ECG. Por su parte, el filtro pasa banda permite un rango de frecuencias más amplio obteniendo un poco más de detalle a comparación del filtro pasa bajas y en su FFT se resalta la presencia de solamente las frecuencias de su rango (0.5 a 100 Hz). Por último, el filtro rechaza banda solo eliminó el ruido a 60 Hz y por ende mantuvo la forma más cercana a las señales en bruto.
###
###
### **ANÁLISIS DE SEÑALES EMG**

**1\. BICEPS BRAQUIAL EN REPOSO**
###

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/EMG1.png)  | ![Texto alternativo](Imagenes/FFT_EMG1.png)  | ![Texto alternativo](Imagenes/STFT_EMG1.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/EMG1_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_EMG1_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_EMG1_FILTRO1.png) |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/EMG1_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_EMG1_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_EMG1_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/EMG1_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_EMG1_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_EMG1_FILTRO3.png) |

###
**2\. BICEPS BRAQUIAL CON OPOSICIÓN LEVE**
###

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/EMG2.png)  | ![Texto alternativo](Imagenes/FFT_EMG2.png)  | ![Texto alternativo](Imagenes/STFT_EMG2.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/EMG2_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_EMG2_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_EMG2_FILTRO1.png) |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/EMG2_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_EMG2_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_EMG2_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/EMG2_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_EMG2_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_EMG2_FILTRO3.png) |

###
**3\. BICEPS BRAQUIAL CON OPOSICIÓN FUERTE**
###

| CAMPO             | DOMINIO DEL TIEMPO | DOMINIO DE LA FRECUENCIA (FFT). | ESPECTROGRAMA (STFT). |
|:------------------|:-------------------:|:--------------------------:|:-----------------------------------------:|
| **SEÑAL ORIGINAL**    | ![Texto alternativo](Imagenes/EMG3.png)  | ![Texto alternativo](Imagenes/FFT_EMG3.png)  | ![Texto alternativo](Imagenes/STFT_EMG3.png) |
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/EMG3_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO1.png)| ![Texto alternativo](Imagenes/STFT_EMG3_FILTRO1.png) |
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/EMG3_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO2.png)| ![Texto alternativo](Imagenes/STFT_EMG3_FILTRO2.png) |  
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/EMG3_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO3.png)| ![Texto alternativo](Imagenes/STFT_EMG3_FILTRO3.png) |

Analizando cada señal de EMG junto con cada filtro podemos llegar a observaciones generales. En primer lugar, podemos ver que las señales EMG difieren mucho entre sí dependiendo de la actividad del músculo.
En segundo lugar, el filtro pasabajas atenuó a la señal en general haciendo también que las señales de alta frecuencia se vean eliminadas. Por su parte, el filtro pasa banda permite un rango de frecuencias propio de un EMG más amplio y también atenuó a la señal EMG, incluso moviéndola. Por último, el filtro rechaza banda solo eliminó el ruido a 60 HZ, pero fue el filtro que más atenuó a las señales en comparación con los otros dos.

## **FILTROS**

### **ANÁLISIS DE LOS FILTROS USADOS**
| CAMPO             | DIAGRAMA DE POLOS Y ZEROS | DIAGRAMA DE BODE (MAGNITUD Y FASE).|
|:------------------|:-------------------:|:--------------------------:|
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/Zplane_Bajas.png)   | ![Texto alternativo](Imagenes/Bode_Bajas.png)| 
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/Zplane_Pasa.png)   | ![Texto alternativo](Imagenes/Bode_Pasa.png)| 
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/Zplane_Rechaza.png)   | ![Texto alternativo](Imagenes/Bode_Rechaza.png)| 

Gracias a las gráficas podemos ver como actúan los filtros y sus propiedades.

En el filtro pasa bajas podemos ver que los polos están dentro del círculo unitario, entonces como es un filtro IIR que depende de muestras pasadas y presentes tanto de la entrada como de la salida podemos concluir que el filtro es estable. A su vez, analizando el diagrama de Bode vemos como efectivamente el filtro deja pasar frecuencias bajas hasta que la mangitud decae cerca a los 20 Hz, a eso se le suma el desfase significativo que se aplica para las frecuencias altas.

En el filtro pasa bandas igualmente al ser IIR y poseer sus polos dentro del círculo se concluye que es estable. Respecto a su diagrama de Bode podemos ver que dentro del rango de 1 a 100 Hz las frecuencias no son atenuadas, pero fuera del rango si lo son. Por el diagrama de fase podemos ver que esta cambia todos los componentes de la frecuencia.

Finalmente podemos ver que en el filtro rechaza banda al ser FIR, no posee polos por lo que es estable, a su vez podemos ver que los ceros correspondientes a los componentes de frecuencia de 60 Hz están en el circulo unitario, indicando que están siendo cancelados. El gráfico de magnitud muestra la atenuación en 60Hz y se muestra el desfase constante para toda la señal.

### **JUSTIFICACIÓN DE LOS FILTROS USADOS**
#### **FILTRO PASA BAJAS**
Para el caso de un ECG el filtro IIR pasa bajas con una frecuencia de corte de 20 Hz es usado frecuentemente para eliminar el ruido de alta frecuencia [1, 2, 3]. Si bien la señal ECG posee un rango de frecuencias entre 0.05 Hz y 100 Hz, gran parte de la energía de la señal e información del complejo QRS, uno de los elementos más importantes del ECG, se encuentra entre los 10 y 25 Hz (o menor a los 40 Hz) [1, 2]. Además a esta frecuencia de corte no se pierde la información que con un filtro de 10 o 15 Hz [1]. 

En el caso de un EMG se usó con una frecuencia de corte de 400 Hz, porque la mayoría de las señales EMG su energía se encuentra en un rango menor a los 400 - 450 Hz [4]. A una mayor frecuencia se pierde el rango de interés de una señal EMG y se obtiene mayormente ruido. El uso de este filtro también tiene la razón de que, diseñar un filtro IIR es más sencillo que uno FIR, tanto porque el orden es mucho menor y porque el procesamiento es más rápido.

#### **FILTRO PASA BANDAS**
En caso del ECG el filtro IIR se usó por su menor complejidad en la programación y el menor orden, a diferencia del FIR que, usando un software como PYFDA, se generaban filtros de orden mayor a los 2000. El rango de frecuencias de este filtro es el mismo que el rango de interés de las señales de ECG [5].

Para el EMG se tomó en cuenta el rango de interés de 2 a 500 Hz y el uso de un pasa altas con un corte en 20 Hz [4]. Normalmente se usa un filtro pasa altas a esta frecuencia para eliminar los artefactos generandos por movimientos u otras fuentes de interferencia [4].

#### **FILTRO RECHAZA BANDAS**
El uso de una ventana de Blackman para el rechazo rechaza bandas fue su transición suave en el dominio de la frecuencia, evitando la distorsión de la señal y la reducción de los lóbulos secundarios en la respuesta en frecuencia, para que no se mantengan los ruidos de la señal.

El uso de un rechaza bandas a una frecuencia de 60 Hz o 50 Hz proviene de la red eléctrica de los paises donde el ruido se introduce en las señales fisiológicas capturadas como lo son el ECG y el EMG [1, 3]. Este ruido se debe a la cercanía de fuentes eléctricas o equipos electrónicos, ya que los electrodos y sus cables captan la interferencia electromagnética. Por ello, al ser un ruido común para ambas señales usé un filtro rechaza banda en 60 Hz, por estar en América Latina, buscando atenuar el ruido de la red eléctrica.

## **BIBLIOGRAFÍA**
**[1]** N. Singh, S. Ayub and J. P. Saini, "Design of Digital IIR Filter for Noise Reduction in ECG Signal," 2013 5th International Conference and Computational Intelligence and Communication Networks, Mathura, India, 2013, pp. 171-176, doi: 10.1109/CICN.2013.45.

**[2]** N. N. Samsudin, S. Isaak, and N. Paraman, “Implementation of Optimized Low Pass Filter for ECG filtering using Verilog,” Journal of Physics Conference Series, vol. 2312, no. 1, p. 012049, Aug. 2022, doi: 10.1088/1742-6596/2312/1/012049.

**[3]** F. Parola and J. García-Niebla, “Use of High-Pass and Low-Pass Electrocardiographic Filters in an International Cardiological Community and...,” ResearchGate, Dec. 2017, [Online]. Available: https://www.researchgate.net/publication/321683328_Use_of_High-Pass_and_Low-Pass_Electrocardiographic_Filters_in_an_International_Cardiological_Community_and_Possible_Clinical_Effects

**[4]** C. J. De Luca, L. D. Gilmore, M. Kuznetsov, and S. H. Roy, “Filtering the surface EMG signal: Movement artifact and baseline noise contamination,” Journal of Biomechanics, vol. 43, no. 8, pp. 1573–1579, Mar. 2010, doi: 10.1016/j.jbiomech.2010.01.027.

**[5]** A guide to ECG signal Filtering,” GE HealthCare (United States). https://www.gehealthcare.com/insights/article/a-guide-to-ecg-signal-filtering
