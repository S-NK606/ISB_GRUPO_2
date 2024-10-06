**Entregable:**

## **METODOLOGÍA**

Para el presente trabajo se usaron señales ECG y EMG procedentes de laboratorios anteriores presentes en este mismo GitHub. Las señales seleccionadas son de distintos tipos de medición.

### **Señales ECG**

Las señales registradas fueron de diferentes momentos donde se usó diferentes configuraciones de derivaciones. Específicamente, para el análisis del filtro ECG usaremos las pertenecientes a la tercera derivación de las siguientes etapas: estado basal, estado de reposo medido; estado de pausa respiratoria, donde se registró el ECG después de que el estudiante mantuvo su respiración 10 segundos; y por último, el estado después de una actividad física, ECG registrado después de 5 minutos de actividad física.

Para su procesamiento se recurrió a tres distintos filtros. El primero es un filtro IIR de tipo Butterworth pasa bajas con una frecuencia de corte de 20 Hz. El segundo también es un tipo de filtro IIR de tipo Butterworth pasa altas con una frecuencia de 0.5 Hz. Por último un uwu

pite con una configuración de derivación distinta.

El procesamiento de las señales ECG se puede dar cPara procesar la señal de electromiografía, se recurre a un filtro IIR de tipo Butterworth debido a su uso recurrente en procesamiento de dichas señales \[5, 6\]. Específicamente, el filtro contará con características idénticas así como el implementado por Mello R. G. T, et al en \[6\], que además mostró resultados óptimos. Los componentes del filtro general son un filtro pasa altas (orden 2, fc \= 10 Hz), filtro pasa bajas (orden 8, fc \= 400 Hz) y seis filtros rechaza banda (orden 2, 60 Hz y armónicos hasta 360 Hz). Por otro lado, basándonos en la investigación de Drake y Callaghan \[7\], el filtro FIR adecuado para reducir el ruido y la contaminación generada por la actividad eléctrica cardiaca en las señales de EMG debe ser de pasa alta con una ventana tipo Hamming y una frecuencia de corte de 30 Hz.

### **Diseño del Filtro ECG**

Para el filtro de señales ECG, estudios \[8,9\] comparan el uso de filtros IIR como Butterworth o Chebyshev I y I; sin embargo, muestran que el filtro más adecuado para este tipo de señales es el Butterworth de orden 8\. De manera específica, el estudio \[8\] muestra que un filtro Butterworth pasa bajas de orden 8 con una frecuencia de corte de 60 Hz muestra un Ratio Señal a Ruido (SNR por sus siglas en ingles) en decibelios 11.84, donde un alto valor de SNR indica que la señal no tenderá a perderse en el ruido. En comparación a otros filtros Butterworth implementados en el mismo estudio \[8\] pero con menor orden y distinta frecuencia de corte, este filtro resulta ser el que mejor ante el ruido. Por ello, se tomará como referencia este filtro Butterworth pasa bajas de orden 8 y fc= 60 Hz para el filtro IIR de las señales.

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

| das | asd | ads |
| :---- | :---- | :---- |
| ads | ads | dasads |
| ![][image1] |  |  |

[image1]: <data:image/png;base64,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>