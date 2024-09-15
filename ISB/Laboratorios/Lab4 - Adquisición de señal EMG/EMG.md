# LABORATORIO 4: – USO DE BITalino PARA EMG

### Tabla de contenidos

------------


1. Objetivos
2. Materiales y equipos
3. Resultados
 3.1 Conexión usada
 3.2 Video de la señal
 3.3 Ploteo de la señal en Python 
4. Referencias 

## Objetivos

- Adquirir señales biomédicas de EMG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y plotearlas usando Python.

## Materiales y equipos

<div align="center">

|	Modelo									   |  	Descripción			 | 	Cantidad	  |
| ------------ | ------------ | ------------ |
| 	(R)EVOLUTION						  |		Kit Bitalino   | 1  |
| -  | Laptop  | 1  |

</div>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/laptop.jpeg" width="400" height="266"></p>
</p>

## Resultados

#### Conexión usada

Se utilizo la placa Bitalino para poder capturar y mostrar las señales EMG del usuario. Se usó 3 electrodos como se muestra en la imagen.


<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/electrodos.jpeg" width="400" height="266"></p>
</p>

Los siguientes procedimientos se basan en la colocación de los electrodos en el usuario para poder obtener las señales EMG. Para ello nos basamos en el proyecto SENIAM , este proyecto contiene una guia completa de las ubicaciones de los electrodos. 

##### Video de la señal y ploteo usando Python
##### PRUEBA 1 MEDIR ACTIVIDAD EMG DEL BICEPS BRAQUIAL

En la primera prueba, se tomaron señales del reposo y contracción del biceps braquial, con la conexión de tierra ubicada en el codo.

[Dirigir enlace prueba 1 ](https://youtu.be/lDePVwGDqeE?si=C0gIWEndc8XIegMl)


##### PRUEBA 2 MEDIR ACTIVIDAD EMG DEL DEDO PULGAR

En la segunda prueba, se tomaron señales del reposo y contracción del dedo pulgar, con la conexión de tierra ubicada en el dorso de la mano. 

[Dirigir enlace prueba 2 ](https://youtu.be/xLJEiHnQbc8?si=1YqofOqCRNOEND-I)

##### PRUEBA 3 MEDIR ACTIVIDAD EMG DEL GASTROCNEMIO

En la segunda prueba, se tomaron señales del reposo y contracción del dedo pulgar, con la conexión de tierra ubicada en el dorso de la mano. 

[Dirigir enlace prueba 3 ](https://youtu.be/tBbQW8ibNt8?si=Lukw_Q6-Nm9Y7CEH)


------------


### Ploteo de la señal en Python

La primera prueba se realizo con el biceps braquial el cual se sometio a contra fuerza y contracción máxima.

- Señal de biceps en reposo

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepsrelajado.jpeg" width="400" height="266"></p>
</p>

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepsrelajadofft.jpeg" width="400" height="266"></p>
</p>

- Señal de biceps en  leve contracción 

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepsleve.jpeg" width="400" height="266"></p>
</p>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepslevefft.jpeg" width="400" height="266"></p>
</p>

- Señal de biceps en contracción total

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepsfuerte.jpeg" width="400" height="266"></p>
</p>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/bicepsfuertefft.jpeg" width="400" height="266"></p>
</p>
##### Fundamento 1 

El bíceps braquial es indispensable para nuestras actividades cotidianas y deportivas: levantar pesas, usar herramientas, lanzar objetos e incluso es importante para nuestras gesticulaciones al ser responsable de movimientos tan comunes como la flexión y extensión del codo, la supinación del antebrazo y la elevación del hombro [1, 2]. 
Por ello, este músculo es propenso a lesiones como tendinopatías o desgarros [1] generando que sea necesario el aprendizaje del uso de un EMG. La captura de estas señales permiten analizar la activación de las fibras musculares durante cada movimiento, midiendo el nivel de esfuerzo para mejorar el rendimiento y evaluación del músculo en conjunto para también prevenir las lesiones del mismo.
Por ello, investigaciones anteriores sobre EMG se concentran más en el rendimiento del músculo bíceps braquial con respecto a factores como edad y sexo, buscando sus influencias en características como el valor medio absoluto (MAV) y la raíz cuadrada media (RMS) de las señales EMG [2]. Así, permitiendo la comprensión de cómo varían los datos con estos factores.

------------

La segunda  prueba se realizo con el dedo pulgar en el cuál se tomaron muestras del dedo en reposo, contra fuerza y en posición de pinza con el dedo índice.

- Señal del dedo pulgar en reposo

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/dedoreposo.jpeg" width="400" height="266"></p>
</p>

- Señal del dedo pulgar  leve contracción 

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/opocisionleve.jpeg" width="400" height="266"></p>
</p>
- Señal del dedo pulgar contracción total

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/opocisionfuerte.jpeg" width="400" height="266"></p>
</p>

##### Fundamento 2
En el estudio “Two-dimensional biomechanical thumb model for pipetting” consideraron solo los músculos que afectan la flexión del pulgar directamente, como el Adductor Pollicis Oblique Head (ADDo), Adductor Pollicis Transverse Head (ADDt), Flexor Pollicis Brevis (FPB) y Flexor Pollicis Longus (FPL). [3] El estudio se realizó ya que el pipeteo manual impone movimientos repetitivos, fuerza elevada y posturas incómodas en el pulgar, los dedos y la muñeca, lo que aumenta el riesgo de lesiones musculoesqueléticas. El objetivo del estudio es proporcionar un modelo de regresión lineal para estimar la altura óptima de agarre del pipeteo basado en el modelo bidimensional biomecánico estático desarrollado en este estudio.


------------

En la tercera prueba, el usuario estuvo en posición sentado y parado, y de las dos formas se sometió a contracción el músculo gastrocnemio.

- Señal del gastrocnemio en reposo

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/pantorrillareposo.jpeg" width="400" height="266"></p>
</p>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/reposopanto.jpeg" width="400" height="266"></p>
</p>
En la gráfica, donde la señal EMG fue filtrada mediante un filtro Butterworth y un filtro Notch, la señal resultante tiene una amplitud más estable y un nivel de ruido mucho más bajo en comparación con la señal original, debido a la filtración de la interferencia de alta frecuencia. De esta manera, observamos una actividad eléctrica mínima, al verificar ell rango de amplitud en el gráfico, ya que la señal se mantiene mayormente entre una amplitud de -5 y 5 mV, lo cual es común en señales EMG filtradas en reposo. Cabe destacar, que para aplicar el filtro se utilizaron frecuencias de low pass y high pass de 18 y 499 Hz, respectivamente. Esto ha permitido limpiar la señal significativamente, eliminando tanto el ruido ambiental como la interferencia eléctrica para facilitar el análisis más preciso de la actividad muscular real.
En la gráfica para la Transformada Rápida de Fourier (FFT) se muestran picos significativos en frecuencias bajas, en torno a los 50 Hz, que podrían estar relacionados con la actividad muscular de bajo nivel en reposo. Sin embargo, también se evidencian picos adicionales en las otras frecuencias, los cuales pueden estar relacionados con interferencias eléctricas y otros artefactos de alta frecuencia que contaminan la señal. 
</p>
- Señal del gastrocnemio  leve contracción 

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/pantarrillalevecontra.jpeg" width="400" height="266"></p>
</p>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/levepanto.jpeg" width="400" height="266"></p>
</p>
En la señal EMG filtrada del gastrocnemio con oposición leve se muestra una forma más clara, con menos ruido luego de aplicar los filtros, lo que permite observar mejor las fases de actividad muscular. De esta manera, se destaca que la mayor parte de la actividad muscular destacable se encuentra entre los 5 y 25 segundos, coincidiendo con las contracciones musculares observadas en las gráficas de FFT y RMS. 
En la gráfica de FFT para la señal EMG del gastrocnemio con oposición leve, se observa cómo la energía de la señal se distribuye en las diferentes frecuencias, donde el rango más relevante se encontró entre los 20 y 150 Hz, ya que se observa una mayor concentración de la actividad muscular. A partir de este análisis, se recomendo aplicar un filtro notch en los 50 Hz para eliminar la interferencia de la red eléctrica y así mejorar la calidad de la señal.
</p>

- Señal del gastrocnemio contracción total

<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/pantorrillamaxcontraccion.jpeg" width="400" height="266"></p>
</p>
<p align="center"><img src="/ISB/Laboratorios/Lab4 - Adquisición de señal EMG/Imagenes/fuertepanto.jpeg" width="400" height="266"></p>
</p>

En la señal filtrada para el gastrocnemio con oposición fuerte, se puede observar que la amplitud de la señal aumenta significativamente a partir de los 5 segundos, alcanzando un pico máximo alrededor del segundo 15, lo que coincide con una contracción muscular intensa, desde ese punto la señal decrece gradualmente, lo que puede reflejar la relajación del músculo. En caso del gráfico para su FFT, se puede observan que los componentes entre las frecuencias de 0-50 Hz presentan magnitudes relativamente más altas en comparación con las frecuencias superiores
</p>

##### Fundamento 3

El gastrocnemio es un músculo clave en la biomecánica del cuerpo, especialmente para realizar movimientos como la flexión plantar, caminar, correr y saltar. Al ser un músculo superficial y grande, permite la fácil colocación de electrodos fácilmente colocándolos en lo que sería la "barriga" del músculo, que es la parte central y más gruesa con mínima interferencia de músculos adyacentes. La elección del centro del músculo y un espaciado adecuado entre los electrodos permite obtener señales específicas del gastrocnemio, minimizando la contaminación de otros músculos cercanos [4]. De esta manera se evita  la distorsión de las interpretaciones sobre la activación muscular y la magnitud de la fuerza generada. 
Sin embargo, no existe una relación directa entre la amplitud de la señal EMG y la fuerza ejercida debido a factores intrínsecos y extrínsecos, por lo que es necesario normalizar las grabaciones para realizar comparaciones entre sujetos o momentos. Las contracciones isométricas voluntarias máximas (MVIC) se utilizan frecuentemente para esta normalización[2].
Aunque la mayoría de los estudios basan la normalización de señales EMG en una única posición de isométricas voluntarias máximas (MVIC) , algunos han demostrado que se necesitan varias posiciones para lograr una activación máxima, especialmente en el músculo del gastrocnemio. A pesar de esto, no se ha explorado suficientemente la efectividad de combinar varias posiciones de MVIC en la reproducibilidad entre sesiones para las extremidades inferiores [5]. 



## Referencias

[1] “Biceps brachii,” Physiopedia. https://www.physio-pedia.com/Biceps_Brachii

[2]  N. Burhan, M. ‘Afif Kasno, R. Ghazali, M. R. Said, S. S. Abdullah, and M. H. Jali, “Analysis of the biceps brachii muscle by varying the arm movement level and load resistance band,” Journal of Healthcare Engineering, vol. 2017, pp. 1–8, Jan. 2017, doi: 10.1155/2017/1631384.

[3]	E. Kim y A. Freivalds, “Two-dimensional biomechanical thumb model for pipetting”, Int. J. Ind. Ergonom., vol. 68, pp. 165–175, noviembre de 2018. Accedido el 15 de septiembre de 2024. [En línea]. Disponible: https://doi.org/10.1016/j.ergon.2018.07.008

[4] De Luca, C. J., Kuznetsov, M., Gilmore, L. D., & Roy, S. H. (2012a). Inter-electrode spacing of surface EMG sensors: Reduction of crosstalk contamination during voluntary contractions. Journal of Biomechanics, 45(3), 555–561. https://doi.org/10.1016/j.jbiomech.2011.11.010

[5] Schwartz, C., Wang, F.-C., Forthomme, B., Denoël, V., Brüls, O., & Croisier, J.-L. (2020). Normalizing gastrocnemius muscle EMG signal: An optimal set of maximum voluntary isometric contraction tests for young adults considering reproducibility. Gait & Posture, 82, 196–202. https://doi.org/10.1016/j.gaitpost.2020.08.129



