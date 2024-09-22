# LABORATORIO 5: – USO DE BITalino PARA ECG

### Tabla de contenidos

------------

1. [Introducción](#introduccion)
2. [Objetivos](#objetivos)
3. [Materiales y equipos](#materiales-y-equipos)
4. [Procedimiento](#procedimiento)
5. [Resultados](#resultados)
   1. [Conexión usada](#conexion-usada)
   2. [Video de la señal](#video-de-la-señal)
   3. [Ploteo de la señal en Python](#ploteo-de-la-señal-en-python)
6. [Referencias](#referencias)

## Introducción
El electrocardiograma (ECG) es una prueba diagnóstica fundamental en la medicina que registra la actividad eléctrica del corazón. Utilizando electrodos colocados en la piel, el ECG mide los impulsos eléctricos que desencadenan cada latido cardíaco, proporcionando un gráfico que muestra el ritmo, la frecuencia y la forma de las ondas eléctricas. Esta información es crucial para detectar diversas afecciones cardíacas, como arritmias, infartos y enfermedades del músculo cardíaco. El ECG es una herramienta no invasiva, rápida y ampliamente utilizada en entornos clínicos para evaluar la salud cardiovascular y guiar decisiones terapéuticas.

El presente laboratorio se centra en el uso de la placa de desarrollo Bitalino para capturar señales de electrocardiograma (ECG) de interés. Esta innovadora herramienta nos brinda la capacidad de registrar y analizar la actividad eléctrica del corazón de manera no invasiva y en tiempo real. A lo largo de esta experiencia práctica, se busca adquirir conocimientos sobre la obtención y el análisis de señales ECG, además de familiarizarse con los procedimientos y protocolos necesarios para la utilización de los electrodos de ECG.

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/C.png" width="500" height="266"></p>
</p>
Fig 1. Señales ECG con los diferentes intervalos y segmentos que la componen [1].

## Objetivos

- Adquirir señales biomédicas de ECG usando el BiTalino
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution.
- Interpretar el significado clínico de las señales ECG y observar posibles errores en la toma de datos.
  
## Materiales y equipos

- BITalino (r)evolution kit
- Electrodos ECG
- Computadora con Bluetooth
- Software OpenSignals
- Entorno de desarrollo Python

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/D.png" width="900" height="266"></p>
</p>

## Procedimiento

### 4.1. Conexión del OpenSignals:

La conexión correcta de la PC con la placa BITalino, el reconocimiento del modelo en la aplicación OpenSignals, junto con la configuración de la entrada A2 del BITalino para la medición del ECG.

### 4.2. Revisión de las Guías de laboratorio de BITalino:

La guía: “HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) [2]” posee como contenido la ubicación de electrodos recomendadas siendo, la elegida, la siguiente:

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/A.png" width="300" height="266"></p>
</p>
Fig 2. Colocación de electrodos para la 1era derivación: IN+ (izquierda - rojo) e IN- (derecha - negro) en las muñecas y la REF (blanco) en la cresta ilíaca [1].

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/B.png" width="500" height="266"></p>
</p>
Fig 3. Colocación de los electrodos en el estudiante elegido junto con la conexión con el BITalino.

### 4.3. Preparación del estudiante:

Se debe asegurar que las zonas correspondientes a la ubicación de los electrodos estén libres de obstrucciones, como prendas o accesorios, y que estén limpias para garantizar un contacto adecuado con los electrodos.

### 4.4. Registro de la señal ECG:

Una vez puestos los electrodos superficiales en las zonas descritas se empieza a registrar las señales tres veces en diferentes momentos, cada ocasión se repite con una configuración de derivación distinta.

- **Estado Basal:**
Estado de reposo evaluado donde el estudiante se mantiene calmado y relajado.

[Ver video 1](https://youtu.be/eoxMC3BR_5U)

- **Estado de pausa respiratoria (durante y después):**
El estudiante mantiene la respiración durante 10 segundos, mientras se registra su ECG en ese intervalo. Al concluir, se realiza un nuevo registro del ECG para observar las variaciones posteriores al ejercicio de contención de la respiración. Se repite este proceso tres veces, siendo seis registros en total.

[Ver video 2](https://youtu.be/8n2kfjqa50U)

[Ver video 3](https://youtu.be/anY9URw1vs4)

- **Estado después de una actividad física:**
Durante 5 minutos aproximadamente, el estudiante realiza ejercicios aeróbicos intensos hasta llegar al cansancio. En nuestro caso, el estudiante subió y bajó escaleras durante ese periodo de tiempo. Se busca registrar cada derivación lo más rápido posible para que no disipe el efecto del cansancio sobre el ECG.

[Ver video 4](https://youtu.be/AYHTVNsGHok)

[Ver video 5](https://youtu.be/aCMujE-tHtw)

### 4.5. Simulación - ProSim4:

Finalmente se puede observar señales patrón gracias al ProSim 4, un simulador de signos vitales portátil diseñado para realizar pruebas rápidas que, en este caso se dieron para simular el ECG en diferentes frecuencias cardiacas que fueron registradas con la aplicación OpenSignals.

   - Simulación de 60lpm - Estado basal
   - Simulación de 120lpm - Empieza a agitarse
   - Simulación de 150lpm - Haciendo ejercicio
   - Simulación de 90lpm - Reponiéndose

[Ver video 6](https://youtu.be/D4N19q_PkfQ)

## Resultados

### 5.1. Ploteo de la señal en Python

Para el análisis de la señal obtenida, se utilizó Python para filtrar las señales usando Mediana (Reduce el ruido [3]), Butterworth (0.05Hz - 150Hz), Notch (60Hz) y visualizar la señal:

- Estados de reposo
   - 1ra derivación
   - 2da derivación
   - 3ra derivación
- ECG durante la conteción de respiración
   - Sin Respiración (1ra derivación)        
   - Post-Respiración (1ra derivación)
     - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_1d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.75 segundos. Al comparar esta distancia con la del estado basal, podemos indicar que mantener la respiración por un tiempo de 20 segundos no influye en el aumento de la frecuencia cardiaca. 
        
   - Sin Respiración (2da derivación)
   - Post-Respiración (2da derivación)
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_2d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.70 segundos.
      
   - Sin Respiración (3ra derivación)
   - Post-Respiración (3ra derivación)
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_3d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.75 segundos. Al comparar esta distancia con la del estado basal, podemos indicar que mantener la respiración por un tiempo de 20 segundos seguidamente no influye en el aumento de la frecuencia cardiaca. Esto se puede deber a que la persona participe acostumbra a ejercitarse seguidamente.
        
- Estado de ejercicio
   - 1ra derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_1d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en el que solo se ven 3 complejos QRS, en un estado ejercitado, en la 1ra derivación, se ve como hay 4 complejos QRS en un tiempo de 2 a 4 segundos y aparecen cada 0.5 segundos aproximadamente.
        
   - 2da derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_2d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en la 2ra derivación, los complejos QRS y aparecen cada 0.45 segundos aproximadamente en un tiempo de 2 a 4 segundos. Es decir, se acorta la distancia el intervalo RR
        
   - 3ra derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_3d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en la 3ra derivación, los complejos QRS y aparecen cada 0.5 segundos aproximadamente en un tiempo de 2 a 4 segundos.
        
- Simulaciones
   - 60 bpm
   - 90 bpm
   - 120 bpm
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/S120_24.png" width="700" height="266"></p>
        </p>
        En el ECG del intervalo de 2 a 4 segundos, se puede observar un intervalo RR de 0.5 segundos. Esto podria indicar que en el estado de ejercicio, la persona alcanzo 120 bpm. Además, al ser una simulación se pueden ver mejor las caracteristicas del ECG.
        
   - 150 bpm
     - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/S150_24.png" width="700" height="266"></p>
        </p>
        En el ECG del intervalo de 2 a 4 segundos, se puede observar un intervalo RR de 0.4 segundos. Este rango es 0.1 segundos menor al del ECG a 120 bpm, lo cual puede indicar que a mayor bpms, mas corto es el intervalo RR. Además, al ser una simulación se pueden ver mejor las caracteristicas del ECG.
     

## Referencias
[1] D. J. Nelson, A. Alvarez, E. Dugarte, and G. Álvarez, “Técnicas de procesamiento de la señal ECGAR aplicadas en el prototipo DIGICARDIAC.” https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S0798-04772015000100007
[2] “BITalino Lab Guides (Home Guides).” https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/
[3] J. Cheng, Q. Zou y Y. Zhao, “ECG signal classification based on deep CNN and BiLSTM”, BMC Med. Inform. Decis. Making, vol. 21, n.º 1, diciembre de 2021. Accedido el 21 de septiembre de 2024. [En línea]. Disponible: https://doi.org/10.1186/s12911-021-01736-y
