# LABORATORIO 4: – USO DE BITalino PARA EMG

### Tabla de contenidos

1. [Introducción al laboratorio](#introducción-al-laboratorio)  
   1.1 [¿Qué es EEG?](#qué-es-eeg)  
   1.2 [Aplicaciones](#aplicaciones)  
   1.3 [Tipos de medición de EEG](#tipos-de-medición-de-eeg)  
   1.4 [¿De qué forma obtenemos la señal?](#de-qué-forma-obtenemos-la-señal)

2. [Objetivos](#objetivos)

3. [Materiales y equipos](#materiales-y-equipos)

4. [Procedimiento](#procedimiento)  
   4.1 [Medición y Adquisición por electrodos](#medición-y-adquisición-por-electrodos)</p>
   En general, los métodos desarrollados en este laboratorio para la adquisición de señales EEG seguirán el sistema de posicionamiento 10/20, que se detalla a continuación:
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/procedimientoeeg.png" width="100%" /> </p>
   <p align="center"> Figura X. Distribución de electrodos.</p> 
   Tipo de electrodo:</p>
   El electrodo del Bitalino es un sensor bipolar que consta de dos pines de medición y un pin de referencia, y se utiliza para captar las diferencias de potencial entre dos electrodos cercanos. 
    - Alta sensibilidad: La elevada ganancia del sistema (ganancia = 40,000) lo hace extremadamente sensible a interferencias externas, como artefactos generados por la luz ambiental, movimientos del sujeto y fuentes de        alimentación cercanas, como el ruido de línea de 50/60 Hz.</p>
    - Filtrado de señal: La señal capturada representa la diferencia amplificada entre los dos puntos de medición. Esta señal se procesa mediante un filtro paso de banda de 0,8 a 48 Hz, que ayuda a suprimir las señales         indeseadas comunes, como la actividad muscular y otras fuentes de ruido.</p>
    - Preparación de la piel: Es crucial preparar adecuadamente la piel antes de colocar los electrodos para asegurar una buena conductividad. Esto implica desinfectar la superficie cutánea para eliminar células muertas 
      y otras impurezas, así como retirar cualquier vello que pueda interferir con la adherencia y el contacto del electrodo.</p>
   Además, es recomendable usar un gel conductor para reducir la impedancia de contacto y mejorar la calidad de la señal. Asegurarse de que el área esté seca antes de aplicar los electrodos también es fundamental para       evitar artefactos relacionados con la humedad.
   
   4.2 [Protocolo de adquisición](#protocolo-de-adquisición)</p>

   El proceso de adquisición y medición de señales EEG con BITalino involucra el uso de este dispositivo de adquisición de datos, junto con un conjunto de sensores EEG. Estos sensores capturan las señales bioeléctricas      del cerebro y las convierten en señales digitales que luego pueden ser analizadas con el software especializado OpenSignal. A continuación, se describe el procedimiento empleado para la adquisición y medición de estas 
   señales:

   1. Posición de electrodo bipolar (fp1-fp2):
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/protocoloimagen.png" width="70%" /> </p>
   2. Adquisición de datos</p>
   Procedimiento para la Adquisición y Medición de Señal EEG con BITalino:</p>
      1. Abrir el software OpenSignals y conectar el BITalino.</p>
      2. Conectar el sensor EEG al canal especificado del BITalino, según lo indicado en la ficha técnica.</p>
      3. Colocar los electrodos húmedos en los pines de los sensores EEG, aplicando el gel conductor adecuado.</p>
      4. Ubicar los electrodos en la cabeza del participante:</p>
         - Colocar los electrodos en las zonas **Fp1 y Fp2** del cráneo, asegurándose de seguir las recomendaciones sobre el tipo de electrodo mencionadas anteriormente.</p>
         - Posicionar el electrodo de referencia en la **parte posterior de la oreja**.</p>
      5. Iniciar el registro de señal:</p>
         a. Registrar una **línea base** de la señal durante 30 segundos, asegurándose de que haya poco ruido y sin movimientos (respiración normal, sin movimientos oculares, ojos cerrados).</p>
         b. Realizar cinco ciclos alternados de **ojos abiertos y ojos cerrados**, manteniendo cada fase durante cinco segundos.</p>
         c. Registrar otra fase de referencia de 30 segundos (similar al paso 5.a).</p>
         d. Mientras un compañero lee en voz alta una serie de ejercicios matemáticos, resolverlos mentalmente, manteniendo la mirada en un punto fijo para evitar artefactos.</p>
         e. Detenga la grabación y guarde sus datos</p>
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/preguntas.png" width="70%" /> </p>
   <p align="center"> Figura X. Preguntas de distinta complejidad.</p> 


6. [Resultados](#resultados)  
   5.1 [Fotos de conexión usada](#fotos-de-conexión-usada)  
   5.2 [Señales con OpenBCI](#Señales-con-OpenBCI)  
      5.2.1 [Gráficas del OpenBCI](#gráficas-del-openbci)  
   5.3 [Señal con Bitalino](#señal-con-bitalino)  
      5.3.1 [Videos utilizando el Bitalino](#videos-utilizando-el-bitalino)  
      5.3.2 [Análisis de gráficas](#análisis-de-gráficas)

7. [Conclusiones](#conclusiones)

8. [Referencias](#referencias)


## Introducción al laboratorio

### 1.1. ¿Qué es EEG?

### 1.2. Aplicaciones

### 1.3. Tipos de medición de EEG

### 1.4. ¿De qué forma obtenemos la señal?

## Objetivos

## Materiales y equipos

## Procedimiento

### 4.1. Medición y Adquisición por electrodos

### 4.2. Protocolo de adquisición

## Resultados

### 5.1. Fotos de conexión usada

### 5.2. Señales con OpenBCI

 - 5.2.1. Basal 1
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_GENERAL.png" width="700" height="700"></p></p>
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_FFT_POWER.png" width="700" height="700"></p></p>
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_HEAD.jpg" width="700" height="350"></p></p>
    - Se puede observar más actividad en la sección 8 (lóbulo occipital 2), la cual está encargada de la visión. Posiblemente, esto se dio debido a que el sujeto se encontraba con los ojos cerrados pero despierto. También, se aprecia una menor actividad en las zonas 1, 2 y 7 (lóbulo frontal y occipital 1). [4] Además, en el gráfico de bandas de poder, se ve la predominancia de la onda Alpha, la cual esta relacionada con la meditación y relación. Posiblemente, el sujeto procuro estar lo mas relajado posible para el experimento. En las siguientes graficas de los canales, se observa la casi nula actividad de las ondas Delta, ya que esta mas relacionada a los ciclos de sueño.

   - Canal 1
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C1_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C1_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 2
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C2_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C2_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 3
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C3_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C3_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 4
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C4_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C4_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 5
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C5_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C5_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 6
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C6_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C6_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 7
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C7_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C7_FFT_POWER.png" width="700" height="700"></p></p>
   - Canal 8
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C8_SIGNAL.png" width="700" height="350"></p></p>
     <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_C8_FFT_POWER.png" width="700" height="700"></p></p>

 - 5.2.2. Durante el Pestañeo
    - De 0 a 5 segundos (Ojos cerrados)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_0_5_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_0_5_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_0_5_HEAD.png" width="700" height="350"></p></p>
      Se ve mayor actividad en las secciones 1 y 2 (lóbulo frontal) y la menor actividad en la sección 6 (lóbulo temporal). El lóbulo frontal esta relacionado a la elaboración de pensamientos [3]. Esto puedo darse debido a que el sujeto estaba esperando el toque en el hombro para poder abrir los ojos. Se ve una predominancia en la onda Beta. Esta onda está relacionada al enfoque consciente.[2]

    - De 5 a 10 segundos (Ojos abiertos)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_HEAD.png" width="700" height="350"></p></p>
      Se ve mayor actividad en la sección 8 (lóbulo occipital 2) y la menor actividad en la sección 1 y 2 (lóbulo frontal). Esto se puede deber a que el sujeto ya tiene abiertos los ojos. Además, hay una predominancia en la onda Beta.
      
    - De 10 a 15 segundos (Ojos cerrados)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_HEAD.png" width="700" height="350"></p></p>
      Se ven resultados similares al tiempo de 0 a 5 segundos, como se tomó de referencia el tiempo a los 10 segundos, justo cuando el sujeto debe cerrar los ojos, se ve como es que hay una actividad incrementada en la sección 3, relacionada a la función motora. También se ve una predominancia de la onda Beta.
      
    - De 15 a 20 segundos (Ojos abiertos)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_HEAD.png" width="700" height="350"></p></p>
      Se ven resultados parecidos al tiempo 0 a 5 y 10 a 15 segundos. Aun que en este caso hay una predominancia de las ondas Gamma, la cual esta relacionada con las funciones motoras y cognitivas específicas [1].
      
 - 5.2.3. Basal 2
    - 5 segundos de señal
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_HEAD.png" width="700" height="350"></p></p>
      Se ve una gran irregularidad en todas las graficas adquiridas como picos de 500uV en las señales. En el ploteo de la FFT, se ve como son demasiado parecidas a pesar de ser distintos canales. Las bandas de potencia muestran predominancia alta para casi todas las ondas y el ploteo de cabeza indica alta actividad en todas las secciones. Esto puede deberse a algún error por parte del dispositivo.
      
 - 5.2.4. Durante Matemática mental
    - De 0 a 10 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_POWER.png" width="700" height="350"></p></p>
      Alta actividad en la sección 8, 6 y 4. Estas áreas están relacionadas a la comprensión del lenguaje e inteligencia, a la sección auditiva y al procesamiento visual de las palabras. Esto puede deberse a que el sujeto estaba escuchando con atención la pregunta. Tiene una predominancia de onda Beta.
      
    - De 10 a 20 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_POWER.png" width="700" height="350"></p></p>
      Se ven resultados similares al primer tiempo. Existe una predominancia de la onda Theta, la cual esta relacionada con la imaginación. Posiblemente, esto se debe a que el sujeto esta escuchando el problema matemático con los ojos cerrados. Además, la onda Beta también predomina debido a su relación con la solución de problemas, memoria y concentración.
      
    - De 20 a 30 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_POWER.png" width="700" height="350"></p></p>
      Resultados similares a los tiempos 0-10 y 10-20 segundos, pero en menor intensidad.
      
    - De 30 a 40 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_POWER.png" width="700" height="350"></p></p>
      Resultados similares a los tiempos 0-10 y 10-20 segundos.
      
    - De 40 a 50 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_POWER.png" width="700" height="350"></p></p>
      Resultados similares a los tiempos 0-10 y 10-20 segundos.
      
    - De 50 a 58 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_POWER.png" width="700" height="350"></p></p>
      Resultados similares a los tiempos 0-10 y 10-20 segundos.

### 5.3. Señal con Bitalino

 - 5.3.1. Videos utilizando el Bitalino

 - 5.3.2. Análisis de gráficas
   a. Basal 1:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_IBASAL.png" width="700" height="350"></p></p>

   b. Durante el Pestañeo:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FILTRA_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FILTRA.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_MOVIOJOS.png" width="700" height="350"></p></p>
   c. Basal 2:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_IIBASAL.png" width="700" height="350"></p></p>
   d. Durante Matemática mental
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_MAT.png" width="700" height="350"></p></p>

## 6. Conclusiones

## 7. Referencias
[1] Satapathy, S. K., Dehuri, S., Jagadev, A. K., & Mishra, S. (2019). Introduction. En EEG Brain Signal Classification for Epileptic Seizure Disorder Detection (pp. 1–25). Elsevier.
[2] Attar, E. T. (2022). Review of electroencephalography signals approaches for mental stress assessment. Neurosciences (Riyadh, Saudi Arabia), 27(4), 209–215. https://doi.org/10.17712/nsj.2022.4.20220025
[3]Nosotros, P. C. (2021, julio 22). Áreas funcionales de la corteza cerebral humana. Www.elsevier.com; Elsevier. https://www.elsevier.com/es-es/connect/areas-funcionales-de-la-corteza-cerebral-humana
[4] GUI Widget guide. (s/f). Openbci.com. Recuperado el 29 de septiembre de 2024, de https://docs.openbci.com/Software/OpenBCISoftware/GUIWidgets/


