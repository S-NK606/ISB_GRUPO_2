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
   
   4.2 [Protocolo de adquisición](#protocolo-de-adquisición)</p>


5. [Resultados](#resultados)  
   5.1 [Fotos de conexión usada](#fotos-de-conexión-usada)  
   5.2 [Señales con OpenBCI](#Señales-con-OpenBCI)  
      5.2.1 [Gráficas del OpenBCI](#gráficas-del-openbci)  
   5.3 [Señal con Bitalino](#señal-con-bitalino)  
      5.3.1 [Videos utilizando el Bitalino](#videos-utilizando-el-bitalino)  
      5.3.2 [Análisis de gráficas](#análisis-de-gráficas)

6. [Conclusiones](#conclusiones)

7. [Referencias](#referencias)


## Introducción al laboratorio

### 1.1. ¿Qué es EEG?
El electroencefalograma (EEG) es una prueba que evalúa la actividad eléctrica cerebral producida por las neuronas. Es una prueba neurofisiológica que evalúa los impulsos eléctricos y la conductividad del cerebro mediante electrodos colocados en el cuero cabelludo [1].
Las neuronas se comunican entre sí a través de estos impulsos eléctricos, siempre estando activas y esta actividad se manifiesta como las ondas cerebrales: Delta, Theta, Alpha, Beta y Gamma [2].

   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/IMAGENA.png" width="70%" /> </p>
   Figura 1. Ondas cerebrales.

- Ondas Delta:
Son las ondas con menor frecuencia y las de mayor amplitud. Se observan fisiológicamente en el sueño profundo y es más prominente en las regiones frontocentrales de la cabeza.

- Ondas Theta:
Este es el ritmo que se manifiesta con la somnolencia y las primeras etapas del sueño, como N1 y N2, en un estado inconsciente donde predomina los pensamientos y la reflexión. Es más prominente en las regiones frontocentrales de la cabeza y migra lentamente hacia atrás reemplazando al ritmo alfa debido a la somnolencia temprana.

- Ondas Alfa:
Las ondas alfa están presentes en estado despierto, pero relajado en estado de vigilia, en la región occipital de la cabeza. Se observa mejor con ojos cerrados y un estado de relajación, a su vez se atenúa al abrir los ojos o realizar esfuerzo mental.

- Ondas Beta:
Es el ritmo más frecuente observado en niños y adultos. Su amplitud aumenta durante la somnolencia, estado de alerta, concentración, el sueño N1 y disminuye en el sueño N2 y N3. Es más prominente en las regiones central y frontal de la cabeza.

- Ondas Gamma:
Atribuidas a la percepción sensorial, integrando diferentes áreas del cerebro para las tareas de alto procesamiento cognitivo.

### 1.2. Aplicaciones
El EEG se utiliza ampliamente en diversos campos debido a su capacidad para analizar la actividad eléctrica del cerebro en diferentes situaciones, lo que permite su aplicación en una gran variedad de estudios tanto en humanos como en animales [3]. Algunas de estas aplicaciones incluyen:
- El monitoreo del estado de alerta, coma y muerte cerebral
- La localización de áreas de daño tras una lesión en la cabeza
- Un accidente cerebrovascular o la ubicación de un tumor
- La monitorización del compromiso cognitivo;
- La regulación de la profundidad de la anestesia
- La investigación de la epilepsia y la localización del origen de las convulsiones junto con la evaluación de los efectos de medicamentos antiepilépticos
- La investigación de los trastornos del sueño y su fisiología.
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/IMAGENB.jpg" width="70%" /> </p>
Fig 2. Utilización médica del EEG

### 1.3. Tipos de medición de EEG
Existen dos tipos de formas básicas de disposición de electrodos para EEG y se diferencias en el registro de la actividad eléctrica [4]:
Monopolar: Se mide la diferencia de un potencial entre un electrodo colocado en una zona activa del cerebro, donde se espera el registro de la actividad eléctrica, y un electrodo de referencia en una zona neutra. Permite obtener una medida más focalizada en una región específica.
Bipolar: La diferencia del potencial es entre dos electrodos colocados en áreas de actividad principal, es decir, no hay un electrodo de referencia neutro. Se realiza de manera transversal, con una línea imaginaria que cruza el cerebro de lado a lado, o de manera longitudinal, de adelante hacia atrás o viceversa. Permite comparar la actividad eléctrica de dos áreas.
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/IMAGENC.png" width="70%" /> </p>
   Fig 3. Tipos de medición del EEG
   
### 1.4. ¿De qué forma obtenemos la señal?
En esta sesión de laboratorio obtendremos la señal mediante dos dispositivos. Usaremos la entrada para EEG del BITalino y veremos las señales producidas por el Ultracortex Mark IV EEG.
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/IMAGEND.png" width="70%" /> </p>
   Fig 4. BITalino y Ultracortex Mark IV EEG.

## Objetivos
- Adquirir señales biomédicas de EEG usando el BiTalino y el Ultracortex Mark IV EEG.
- Extraer la información de las señales EEG del software OpenSignals (r)evolution y del OpenBCI GUI.
- Interpretar el significado clínico de las señales EEG y observar posibles errores en la toma de datos.

## Materiales y equipos
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/IMAGENE.png" width="70%" /> </p>
   
## Procedimiento

### 4.1. Medición y Adquisición por electrodos
   En general, los métodos desarrollados en este laboratorio para la adquisición de señales EEG seguirán el sistema de posicionamiento 10/20, que se detalla a continuación:
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/procedimientoeeg.png" width="100%" /> </p>
   <p align="center"> Figura 5. Distribución de electrodos.</p> 
   Tipo de electrodo:</p>
   El electrodo del Bitalino es un sensor bipolar que consta de dos pines de medición y un pin de referencia, y se utiliza para captar las diferencias de potencial entre dos electrodos cercanos. 
    - Alta sensibilidad: La elevada ganancia del sistema (ganancia = 40,000) lo hace extremadamente sensible a interferencias externas, como artefactos generados por la luz ambiental, movimientos del sujeto y fuentes de        alimentación cercanas, como el ruido de línea de 50/60 Hz.</p>
    - Filtrado de señal: La señal capturada representa la diferencia amplificada entre los dos puntos de medición. Esta señal se procesa mediante un filtro paso de banda de 0,8 a 48 Hz, que ayuda a suprimir las señales         indeseadas comunes, como la actividad muscular y otras fuentes de ruido.</p>
    - Preparación de la piel: Es crucial preparar adecuadamente la piel antes de colocar los electrodos para asegurar una buena conductividad. Esto implica desinfectar la superficie cutánea para eliminar células muertas 
      y otras impurezas, así como retirar cualquier vello que pueda interferir con la adherencia y el contacto del electrodo.</p>
   Además, es recomendable usar un gel conductor para reducir la impedancia de contacto y mejorar la calidad de la señal. Asegurarse de que el área esté seca antes de aplicar los electrodos también es fundamental para       evitar artefactos relacionados con la humedad.

### 4.2. Protocolo de adquisición

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
   <p align="center"> Figura 6. Preguntas de distinta complejidad.</p> 
   
## Resultados

### 5.1. Fotos de conexión usada
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/WhatsApp Image 2024-09-28 at 11.25.39 PM.jpeg" width="70%" /> </p>

   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/WhatsApp Image 2024-09-28 at 11.26.59 PM.jpeg" width="70%" /> </p>   
### 5.2. Señales con OpenBCI

 - 5.2.1. Basal 1
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_GENERAL.png" width="700" height="700"></p></p>
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_FFT_POWER.png" width="700" height="700"></p></p>
    - <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B1_HEAD.jpg" width="700" height="350"></p></p>
    - Se puede observar más actividad en la sección 8 (lóbulo occipital 2), la cual está encargada de la visión. Posiblemente, esto se dio debido a que el sujeto se encontraba con los ojos cerrados pero despierto. También, se aprecia una menor actividad en las zonas 1, 2 y 7 (lóbulo frontal y occipital 1). [8] Además, en el gráfico de bandas de poder, se ve la predominancia de la onda Alpha, la cual esta relacionada con la meditación y relación. Posiblemente, el sujeto procuro estar lo mas relajado posible para el experimento. En las siguientes graficas de los canales, se observa la casi nula actividad de las ondas Delta, ya que esta mas relacionada a los ciclos de sueño.

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
      Se ve mayor actividad en las secciones 1 y 2 (lóbulo frontal) y la menor actividad en la sección 6 (lóbulo temporal). El lóbulo frontal esta relacionado a la elaboración de pensamientos [7]. Esto puedo darse debido a que el sujeto estaba esperando el toque en el hombro para poder abrir los ojos. Se ve una predominancia en la onda Beta. Esta onda está relacionada al enfoque consciente.[6]

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
      Se ven resultados parecidos al tiempo 0 a 5 y 10 a 15 segundos. Aun que en este caso hay una predominancia de las ondas Gamma, la cual esta relacionada con las funciones motoras y cognitivas específicas [5].
      
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
Una vez puestos los electrodos superficiales en las zonas descritas se empieza a registrar las señales según los movimientos requeridos.

- **Estado Basal 1:**
Estado de reposo evaluado donde el estudiante se mantiene calmado y relajado.

[Ver video 1](https://youtu.be/xE2c2RN0ELw)

- **Estado de Pestañeo:**
El estudiante cierra y abre los ojos 5 veces cada uno en intervalos de 5 segundos.

[Ver video 2](https://youtu.be/9A-EMl1lTdQ)
- **Estado Basal 2:**
El estudiante vuelve al estado de reposo manteniendose calmado luego del estado de pestañeo.

[Ver video 3](https://youtu.be/6K9KzS4KCaU)
- **Estado de Razonamiento Matemático:**
El estudiante es puesto a prueba con ejercicios de razonamiento matemático entre simples y complejos.

[Ver video 4](https://youtu.be/RdxDtemofSo)

 - 5.3.2. Análisis de gráficas
   a. Basal 1:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IBASAL_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_IBASAL.png" width="700" height="350"></p></p>
      - Análisis:
      Al realizar la bandas de potencia para cada rango de frecuencia, se observa que  la potencia de la banda Delta (0.5 - 4 Hz) es muy baja, esto se debe a que está más relacionada con el sueño profundo y no con un estado de relajación despierta. De la misma manera, la potencia de las bandas Theta (4 - 8 Hz) y Alpha (8 - 13 Hz) son mayores en comparación a la banda Delta, lo cual es típico en las bandas Theta para un estado de relajación profunda, donde el usuario no se encuentra dormido. Mientras que, la banda Alpha aunque es mayor a la banda Delta, sigue siendo baja comparada con las bandas Beta y Gamma, ya que normalmente  se esperaría un mayor incremento en la banda Alpha, ya que esta frecuencia está directamente relacionada con la calma mental y el cierre de los ojos, no obstante al observar la baja potencia de la onda Alpha, se denota que el usuario no alcanzó el estado óptimo de relajación. Además, esto también se corroborá en el estado dominante de la banda Beta (13 - 30 Hz) en la gráfica de bandas de potencia, ya que la banda Beta presenta la potencia más alta entre todas las bandas. Esto puede indicar que, a pesar de que la persona se trato de mantener en un estado de reposo, pudo estar experimentando actividad mental elevada o ansiedad durante la medición, ya que la banda Beta está asociada con actividad cognitiva intensa, de alerta o concentración. Asimismo, se destaca que, la potencia de la banda Gamma (> 30 Hz) es relativamente alta, lo cual es un poco inusual en un estado relajado de un usuario, ya que la banda Gamma  suele estar asociada con el procesamiento cognitivo avanzado y la actividad neuronal sincronizada. Esto podría indicar que, aunque la persona mantuvo un estado de reposo con los ojos cerrados, su cerebro siguió procesando información de manera activa.

   b. Durante el Pestañeo:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FILTRA_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MOVIOJOS_FILTRA.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_MOVIOJOS.png" width="700" height="350"></p></p>
      - Análisis:
      Para comprender mejor la respuesta EEG, durante los cambios de estado entre ojos abiertos y cerrados por intervalos, es necesario profundizar en la dinámica de las diferentes bandas de frecuencia del EEG y su relación con la actividad cortical subyacente. Al observar la banda de potencia, podemos rescatar que, la banda Delta aún refleja una baja potencia, esto se debe a que la persona se encuentra despierta y realizando cambios entre apertura y cierre de ojos. En caso de la banda Theta, la potencia en esta banda es considerablemente más alta que en el estado basal. Esto puede deberse a que la actividad de las ondas Theta puede aumentar durante tareas que implican relajación o meditación, pero también puede aparecer durante momentos de atención fluctuante, dado que el pestañeo involucra una cierta desconexión momentánea, esta actividad podría correlacionarse con la apertura y cierre repetido de los ojos, lo que interrumpe el flujo continuo de atención. También, se observa un aumento de la potencia en Alpha, en comparación al anterior estado de reposo, ya que la banda Alpha se origina principalmente en las áreas occipitales y se asocia con la inhibición de la corteza visual, lo que refleja una desconexión del procesamiento sensorial externo. En condiciones normales, al abrir los ojos, la potencia de la banda Alpha disminuye drásticamente, lo que se conoce como "bloqueo Alpha" o reactividad Alpha. Esto es eventualmente notorio, ya que la banda Alpha no presenta un potencial dominante como podría esperarse en un estado de relajación prolongado con los ojos cerrados, ya que la alternancia entre apertura y cierre de los ojos, provoca fluctuaciones rápidas en la potencia de la onda Alpha, lo que afecta la capacidad del cerebro para generar ritmos Alpha estables.
Asimismo,  la banda Beta muestra la mayor potencia,ya que representa una actividad mental activa, concentración y procesamiento sensorial. Cabe destacar que, el acto de pestañear requiere cierta atención visual, y el procesamiento visual constante cuando los ojos están abiertos podría explicar el alto nivel de actividad en esta banda.
En caso de, la potencia de Gamma, se destaca por ser moderada y estar relacionada con procesos de alta complejidad cognitiva y de integración sensorial. El hecho de que no sea tan alta podría sugerir que la tarea de pestañear no implica un nivel elevado de procesamiento cognitivo o integración multisensorial.
Finalmente, se puede analizar que, el hecho de que la persona alterne entre ojos abiertos y cerrados provoca un cambio en la dinámica cortical, ya que la entrada de información visual estimula áreas occipitales y parietales, mientras que el cierre de ojos inhibe parcialmente estas áreas.

   c. Basal 2:
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/IIBASAL_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_IIBASAL.png" width="700" height="350"></p></p>
     - Análisis:
     Al realizar el análisis comparativo EEG en estado de reposo tras el ejercicio de apertura y cierre de ojos se observo que en la banda Delta, la potencia permanece baja, indicando que el sujeto no está en un estado de relajación profunda ni en sueño, siendo coherente con un estado de vigilia ligera. En la banda Theta, se observa un ligero aumento de la potencia en comparación con el estado de alternancia de ojos, lo que sugiere un reposo estable pero consciente. Dado que la banda Theta está asociada con la relajación y somnolencia ligera, esta disminución sugiere menos actividad relacionada con la fluctuación visual.
Por otro lado, la potencia de la banda Beta sigue siendo alta, lo que tiene sentido, ya que está relacionada con la atención y el procesamiento mental activo. En este estado de reposo, es probable que la persona todavía esté procesando información del entorno o enfocándose en su relajación consciente, lo que mantendría una alta actividad en esta banda. Por último, la potencia de la banda Gamma ha aumentado significativamente en comparación con el estado de pestañeo, siendo esto interesante, ya que la banda Gamma está vinculada con el procesamiento de información a nivel más profundo y la integración de actividades cognitivas complejas, por lo que podría estar reflejando una mayor consolidación cognitiva después del ciclo de pestañeo, donde el cerebro integra la información procesada durante los momentos previos de atención y cierre de ojos, aunque también puede deberse a una menor relajación por parte del usuario.
   
   d. Durante Matemática mental
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_orig.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_filtra_FFT.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/MATE_filtra.png" width="800" height="450"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/SEÑALES EEG/BANDA_POT_MAT.png" width="700" height="350"></p></p>
   - Análisis:
     Como último análisis, se tomo el caso donde el usuario estuviera resolviendo ejercicios de razonamiento matemático, donde la banda Delta se mantuvo en una potencia significativamente baja, mientras que, la banda Theta presento una disminución notable de su potencia, ya que estas son más prominentes en estados relajados o meditación, aunque también pueden activarse  durante la ejecución de tareas cognitivas, así como, en la resolución de problemas
En contraste, la banda beta muestra una mayor potencia con respecto a las demás frecuencias, lo que es típico en procesos que requieren concentración consciente y actividades mentales intensas. Este incremento en la actividad beta, particularmente en el hemisferio izquierdo, sugiere que el cerebro está involucrado en la representación mental abstracta y en la ejecución de tareas cognitivas. Por otro lado, la banda gamma también muestra una potencia considerable, aunque no tan alta como la beta. Las ondas gamma están relacionadas con la integración de información entre diferentes regiones cerebrales, esenciales para la memoria a largo plazo y la atención focalizada. Esta actividad gamma es clave en la integración y consolidación de información durante tareas complejas, lo que permite una coordinación eficiente entre las áreas corticales involucradas en el razonamiento. Aunque el razonamiento matemático es una tarea que generalmente requiere un alto nivel de integración cognitiva, la intensidad de la activación Gamma depende de la complejidad de los problemas y el tipo de procesamiento requerido, por lo que no es sorpresivo que en este caso el potencial de la banda Gamma no destacará frente a otras frecuencias,  ya que es posible que en las condiciones experimentales actuales, las tareas matemáticas realizadas no demanden un procesamiento tan intensivo como para activar fuertemente la banda Gamma. 

## 6. Conclusiones

## 7. Referencias

- [1] A. I. De Riquer, “Electroencefalograma | ¿Qué es un electroencefalograma | PortalCLÍNIC,” Clínic Barcelona. https://www.clinicbarcelona.org/asistencia/pruebas-y-procedimientos/electroencefalograma
- [2] C. S. Nayak and A. C. Anilkumar, “EEG Normal waveforms,” StatPearls - NCBI Bookshelf, Jul. 24, 2023. https://www.ncbi.nlm.nih.gov/books/NBK539805/
- [3] P. A. Abhang, B. W. Gawali, and S. C. Mehrotra, “Technological basics of EEG recording and operation of apparatus,” in Elsevier eBooks, 2016, pp. 19–50. doi: 10.1016/b978-0-12-804490-2.00002-6.
- [4] F. Ramos-Argüelles, G. Morales, S. Egozcue, R. M. Pabón, and M. T. Alonso, “Técnicas básicas de electroencefalografía: principios y aplicaciones clínicas.” https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600006

 - [5] Satapathy, S. K., Dehuri, S., Jagadev, A. K., & Mishra, S. (2019). Introduction. En EEG Brain Signal Classification for Epileptic Seizure Disorder Detection (pp. 1–25). Elsevier.
 - [6] Attar, E. T. (2022). Review of electroencephalography signals approaches for mental stress assessment. Neurosciences (Riyadh, Saudi Arabia), 27(4), 209–215. https://doi.org/10.17712/nsj.2022.4.20220025
 - [7]Nosotros, P. C. (2021, julio 22). Áreas funcionales de la corteza cerebral humana. Www.elsevier.com; Elsevier. https://www.elsevier.com/es-es/connect/areas-funcionales-de-la-corteza-cerebral-humana
 - [8] GUI Widget guide. (s/f). Openbci.com. Recuperado el 29 de septiembre de 2024, de https://docs.openbci.com/Software/OpenBCISoftware/GUIWidgets/


