# Laboratorio de Edge Impulse 

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Resultados](#5-resultados)


## 1. Introducción

Edge Impulse es una plataforma para desarrollar algoritmos de aprendizaje automático (machine learning) diseñados para sistemas embebidos, dispositivos que realizan tareas en tiempo real,con la finalidad de simplificar el proceso de adquisición y procesamiento de datos. El propósito de esta plataforma es facilitar el desarrollo de modelos de machine learning.

Por ello, para una tarea como lo es el análisis y procesamiento de señales biomédicas en tiempo real como el ECG, el uso de Edge Impulse es importante en aplicaciones como el diagnóstico y monitoreo.

En el presente informe se mostrará la adquisición de datos para la plataforma Edge Impulse como inicio de la creación de un proyecto de esta herramienta.


## 2. Objetivos
1. Organizar y adquirir señales de ECG en diferentes estados con un formato adecuado para su futuro uso y análisis.

2. Subir y organizar en el Edge Impulse las señales adquiridas, categorizándolas por sus estados.
 
 
## 3. Metodología
1. **Adquisición de data y conversión del formato:**
   En este mismo GitHub se documentó la adquisición previa de señales de ECG en distintos estados:

    - **Estado Basal:**
    Estado de reposo evaluado donde el estudiante se mantiene calmado y relajado.


    - **Estado de pausa respiratoria (durante y después):**
    El estudiante mantiene la respiración durante 10 segundos, mientras se registra su ECG en ese intervalo. Al concluir, se realiza un nuevo registro del ECG para observar las variaciones posteriores al ejercicio de contención de la respiración. 

    - **Estado después de una actividad física:**
    Durante 5 minutos aproximadamente, el estudiante realiza ejercicios aeróbicos intensos hasta llegar al cansancio. 

    - **Simulación - ProSim4:**
    Se obtuvo señales patrón gracias al ProSim 4, un simulador de signos vitales portátil diseñado para realizar pruebas rápidas en distintos bpm: 60, 120, 150 y 90.

    Las señales fueron adquiridas mediante el software OpenSignals y este las exportaba en un formato txt. Para su conversión se usó el siguiente código donde se especifica que cada señal sea dividida en segmentos de 10 segundos, con la finalidad de una estandarización al subirlo al Edge Impulse.

      ```
      import os
      import pandas as pd
      
      #Rutas de entrada y salida
      input_folder = 'D:\\Marco Ichillumpa\\Semestre 2024 - 2\\ISB\\EdgeImpulse - Lab 11\\data'
      output_folder = 'D:\\Marco Ichillumpa\\Semestre 2024 - 2\\ISB\\EdgeImpulse - Lab 11\\csvs'

      #Configuración
      fs = 1000  #Frecuencia de muestreo (Hz)
      segmento = 10  #Duración de cada segmento en segundos
      samples_per_segment = fs * segmento  #Muestras por segmento

      #Recorrer todos los archivos en la carpeta de entrada
      for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):  #Filtrar solo los archivos .txt
            input_file = os.path.join(input_folder, file_name)
            
            #Leer el archivo, omitiendo las líneas de encabezado con #
            data = pd.read_csv(input_file, delimiter='\t', comment='#', header=None)
            
            #Solo importa la data de la columna 0 y 5
            selected_columns = data[[0, 5]]
            
            #Renombro la data
            selected_columns.columns = ['timestamp', 'data']
            
            #División de los segmentos
            num_segments = len(selected_columns) // samples_per_segment
            for segment_idx in range(num_segments):
                start_idx = segment_idx * samples_per_segment
                end_idx = start_idx + samples_per_segment
                segment = selected_columns.iloc[start_idx:end_idx]
                
                #Creación del archivo para cada segmento
                segment_file_name = f"{file_name.replace('.txt', '')}_segment_{segment_idx + 1}.csv"
                segment_output_path = os.path.join(output_folder, segment_file_name)
                
                #Guardado de los segmentos
                segment.to_csv(segment_output_path, index=False)
                
                print(f"Segmento creado: {segment_file_name}")
        print("Proceso completado.")
        ```
        
2. **CSV Wizard:**
   Para garantizar una correcta integración de los segmentos en el dataset, se utilizó la herramienta **CSV Wizard**, configurada para procesar los archivos de manera uniforme. A continuación, se detallan los pasos realizados:

      | **Pasos** | **Imágenes** |
      | --- | --- |
      | **Paso 1:** Cargar un archivo de datos al **CSV Wizard** para iniciar la configuración de los parámetros necesarios. Esto permite establecer las reglas de procesamiento desde el inicio. | <img src="./Imagenes/paso_1.png" width="500"> |
      | **Paso 2:** Configurar las delimitaciones del archivo: <ul><li>Separador: **Comas**</li><li>Omitir líneas: **Ninguna**</li><li>Encabezado: **"No header row"**</li></ul> Estas configuraciones aseguran que todos los datos sean interpretados correctamente. | <img src="./Imagenes/paso_2.png" width="500"> |
      | **Paso 3:** Establecer la frecuencia de muestreo a **1000 Hz**, reflejando el intervalo de tiempo con el que los datos fueron registrados. Este paso es crucial para mantener la integridad del análisis de las señales. | <img src="./Imagenes/paso_3.png" width="500"> |
      |  | <img src="./Imagenes/paso_4.png" width="500"> |
      | **Paso 4:** Seleccionar la columna de datos correspondiente, especificando la señal o información relevante dentro del archivo CSV. | <img src="./Imagenes/paso_5.png" width="500"> |
      |  | <img src="./Imagenes/paso_6.png" width="500"> |
      | **Paso 5:** Indicar la duración de las muestras seleccionando **"Unlimited"** en la opción *How long do you want your samples to be*. Esto permite que las muestras se procesen completas sin restricciones de longitud. | <img src="./Imagenes/paso_7.png" width="500"> |
      | **Paso 6:** Confirmar la configuración. Una vez finalizado, se muestra un mensaje indicando que cualquier archivo CSV subido al proyecto será procesado según las reglas definidas en este asistente (*Any CSV files that you upload into your project will be processed according to the rules you set up here*). Este paso garantiza la uniformidad en el tratamiento de los datos. | <img src="./Imagenes/paso_8.png" width="500"> |

3. **Dataset:**
   Se subieron 6 segmentos de cada tipo de señal al dataset principal (Basal, Ejercicio, ProSim, etc). Los segmentos sobrantes se utilizaron para balancear las proporciones entre las partes de entrenamiento (*training*) y prueba (*testing*) de la base de datos.
      <div style="text-align: center;">
        <img src="./Imagenes/paso_10.png" width="500">
      </div>

## 5. Resultados
1. **Link:**
   [https://studio.edgeimpulse.com/studio/55816](https://studio.edgeimpulse.com/public/558161/live)
   
2. **Tabla de Señales**
      | **Training Dataset** | **Test Dataset** |
      | --- | --- |
      | <img src="./Imagenes/paso_11.png" width="500"> | <img src="./Imagenes/paso_12.png" width="500"> |

      | **Categoria de señal ECG** | **Señal** |
      | --- | --- |
      | Estado Basal |  <img src="./Imagenes/paso_13.png" width="500"> |
      | Estado con respiración | <img src="./Imagenes/paso_14.png" width="500"> |
      | Estado sin respiración | <img src="./Imagenes/paso_15.png" width="500"> |
      | Ejercicio | <img src="./Imagenes/paso_16.png" width="500"> |
      | Simulación (ProSim) | <img src="./Imagenes/paso_17.png" width="500"> |

