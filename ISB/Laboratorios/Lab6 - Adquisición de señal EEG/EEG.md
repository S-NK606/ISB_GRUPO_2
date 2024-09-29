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
   <p align="center"> <img src="https://github.com/S-NK606/ISB_GRUPO_2/blob/main/ISB/Laboratorios/Lab6%20-%20Adquisici%C3%B3n%20de%20se%C3%B1al%20EEG/Imagenes/protocoloimagen.png" width="100%" /> </p>
   2. Adquisición de datos


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
    - De 5 a 10 segundos (Ojos abiertos)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_5_10_HEAD.png" width="700" height="350"></p></p>
    - De 10 a 15 segundos (Ojos cerrados)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_10_15_HEAD.png" width="700" height="350"></p></p>
    - De 15 a 20 segundos (Ojos abiertos)
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B2_15_20_HEAD.png" width="700" height="350"></p></p>
      
 - 5.2.3. Basal 2
    - 5 segundos de señal
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_FFT_POWER.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B3_HEAD.png" width="700" height="350"></p></p>
      
 - 5.2.4. Durante Matemática mental
    - De 0 a 10 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_0_10_POWER.png" width="700" height="350"></p></p>
    - De 10 a 20 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_10_20_POWER.png" width="700" height="350"></p></p>
    - De 20 a 30 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_20_30_POWER.png" width="700" height="350"></p></p>
    - De 30 a 40 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_30_40_POWER.png" width="700" height="350"></p></p>
    - De 40 a 50 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_40_50_POWER.png" width="700" height="350"></p></p>
    - De 50 a 58 segundos
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_SIGNAL.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_FFT_HEAD.png" width="700" height="700"></p></p>
      <p align="center"><img src="/ISB/Laboratorios/Lab6 - Adquisición de señal EEG/Imagenes/B4_50_58_POWER.png" width="700" height="350"></p></p>

### 5.3. Señal con Bitalino

 - 5.3.1. Videos utilizando el Bitalino

 - 5.3.2. Análisis de gráficas

## 6. Conclusiones

## 7. Referencias

