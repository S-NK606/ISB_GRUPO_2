# **PROCESAMIENTO DE SEÑALES DE ECG Y EMG MEDIANTE FILTROS DIGITALES**
Este trabajo ha sido hecho de forma individual

## **METODOLOGÍA**

Para el presente trabajo se usaron señales ECG y EMG procedentes de laboratorios anteriores presentes en este mismo GitHub. Las señales seleccionadas son de distintos tipos de medición.

### **Señales ECG**

Las señales registradas fueron de diferentes momentos donde se usó diferentes configuraciones de derivaciones. Específicamente, para el análisis del filtro ECG usaremos las pertenecientes a la tercera derivación de las siguientes etapas: estado basal, estado de reposo medido; estado de pausa respiratoria, donde se registró el ECG después de que el estudiante mantuvo su respiración 10 segundos; y por último, el estado después de una actividad física, ECG registrado después de 5 minutos de actividad física.

Para su procesamiento se recurrió a tres distintos filtros. El primero es un filtro IIR de tipo Butterworth pasa bajas con una frecuencia de corte de 20 Hz. El segundo también es un tipo de filtro IIR de tipo Butterworth pasa banda con una frecuencia de 1 Hz a 100 Hz. Por último un filtro FIR de tipo Butterworth rechaza banda de frecuencias de 60 Hz, usando una ventana de Blackman.

### **Señales ECG**

Las señales registradas fueron de diferentes músculos: biceps braquial, el aductor del pulgar y el gastrocnemio, durante distintas fases de actividad. Específicamente, para el análisis del filtro EMG usaremos las señales del biceps braquila durante las fases de reposo, sin ningún movimiento; oposición leve, donde el estudiante hizo fuerza ligeramente; y oposición fuerte, donde el estudiante usó toda su fuerza contra la oposición.

Para su procesamiento se recurrió a tres distintos filtros. El primero es un filtro IIR de tipo Butterworth pasa bajas con una frecuencia de corte de 400 Hz. El segundo también es un tipo de filtro IIR de tipo Butterworth pasa bandas con una frecuencia de 20 Hz a 500Hz. Por último un filtro FIR de tipo Butterworth rechaza banda de frecuencias de 60 Hz, usando una ventana de Blackman.

## **RESULTADOS**

### **ANÁLISIS DE SEÑALES ECG**

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
| **F. PASA BAJAS**    | ![Texto alternativo](Imagenes/EMG3_FILTRO1.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO1.png)| 
| **F. PASA BANDAS**   | ![Texto alternativo](Imagenes/EMG3_FILTRO2.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO2.png)| 
| **F. RECHAZA BANDA** | ![Texto alternativo](Imagenes/EMG3_FILTRO3.png)   | ![Texto alternativo](Imagenes/FFT_EMG3_FILTRO3.png)| 


### **JUSTIFICACIÓN DE LOS FILTROS USADOS**

## **BIBLIOGRAFÍA**


### **Diseño del Filtro EEG**

En la adquisición de señales de EEG, estas resultan acompañadas de ruido o interferencia de la actividad muscular. En el desarrollo del laboratorio de EEG, los movimientos musculares presentes durante la adquisición de la señal fueron los movimientos faciales, movimientos oculares, hablar, abrir y cerrar los ojos. Ante ello, el estudio \[10\], propone el uso de un filtro tipo Butterworth pasa baja de orden 8 y frecuencia de corte de 35 Hz para la eliminación de contaminación o ruido producida por los movimientos musculares.

Para el presente trabajo se eligieron señales EMG y ECG 

Deberán presentar un archivo en formato Markdown que contenga el siguiente contenido:

1. **:**

   * Utilicen las señales EMG y ECG obtenidas en las sesiones anteriores.  
   * Seleccionen una señal de cada actividad realizada para EMG y ECG.  
   * Las señales deben ser filtradas utilizando filtros FIR o IIR.

1. **Análisis de señales:**  
* Para cada señal (original y filtrada), incluyan las siguientes gráficas:  
  * Gráfica en el dominio del tiempo.  
    * Gráfica en el dominio de la frecuencia.  
  * Transformada corta de Fourier (opcional).

1. **Análisis del filtro:**  
   * Incluyan el diagrama de polos y ceros.  
   * Diagrama de Bode (magnitud y fase).  
2. **Justificación:**  
   * Expliquen por qué eligieron esos tres filtros.

METODOLOGÍA

ECG:  
Pasa baja \-Butterworth \- Fifth order filter \- 20Hz  
Pasa alta \- Butterworth \- 0.5Hz

ISB1  
ISB2  
[https://academy.theortusgroup.com/en-gb/ecg-filtering-that-can-help-save-lives\#:\~:text=The%20intended%20use%20plays%20a,pass%20filter%20with%20150%20Hz](https://academy.theortusgroup.com/en-gb/ecg-filtering-that-can-help-save-lives#:~:text=The%20intended%20use%20plays%20a,pass%20filter%20with%20150%20Hz).  
[https://www.medteq.net/article/2017/4/1/ecg-filters](https://www.medteq.net/article/2017/4/1/ecg-filters)
