# LABORATORIO 5: – USO DE BITalino PARA ECG

### Tabla de contenidos

------------

1. [Introducción](#Introduccion)
2. [Objetivos](#objetivos)
3. [Materiales y equipos](#materiales-y-equipos)
4. [Resultados](#resultados)
   1. [Conexión usada](#conexion-usada)
   2. [Video de la señal](#video-de-la-señal)
   3. [Ploteo de la señal en Python](#ploteo-de-la-señal-en-python)
5. [Referencias](#referencias)

## Introducción
El electrocardiograma (ECG) es una prueba diagnóstica fundamental en la medicina que registra la actividad eléctrica del corazón. Utilizando electrodos colocados en la piel, el ECG mide los impulsos eléctricos que desencadenan cada latido cardíaco, proporcionando un gráfico que muestra el ritmo, la frecuencia y la forma de las ondas eléctricas. Esta información es crucial para detectar diversas afecciones cardíacas, como arritmias, infartos y enfermedades del músculo cardíaco. El ECG es una herramienta no invasiva, rápida y ampliamente utilizada en entornos clínicos para evaluar la salud cardiovascular y guiar decisiones terapéuticas.

El presente laboratorio se centra en el uso de la placa de desarrollo Bitalino para capturar señales de electrocardiograma (ECG) de interés. Esta innovadora herramienta nos brinda la capacidad de registrar y analizar la actividad eléctrica del corazón de manera no invasiva y en tiempo real. A lo largo de esta experiencia práctica, se busca adquirir conocimientos sobre la obtención y el análisis de señales ECG, además de familiarizarse con los procedimientos y protocolos necesarios para la utilización de los electrodos de ECG.

## Objetivos

- **Implementar** el uso de BITalino para la adquisición de señales ECG.
- **Analizar** las señales obtenidas usando un entorno de desarrollo como Python.
- **Filtrar** y procesar las señales para eliminar ruido y obtener datos claros.
  
## Materiales y equipos

- BITalino (r)evolution kit
- Electrodos ECG
- Computadora con Bluetooth
- Software OpenSignals
- Entorno de desarrollo Python

## Resultados

### 3.1. Conexión usada

Se utilizó la conexión estándar de BITalino con los siguientes pasos:

1. Colocación de los electrodos en el pecho del sujeto para medir la actividad cardíaca.
2. Conexión del dispositivo BITalino vía Bluetooth con la computadora.
3. Uso de la aplicación **OpenSignals** para la visualización en tiempo real de las señales.

### 3.2. Video de la señal

Aquí puedes ver un video demostrando la señal de ECG capturada en tiempo real:

# ![Video placeholder](https://example.com/video-link) <!-- Cambia este enlace por el video correcto si lo tienes o un GIF -->

### 3.3. Ploteo de la señal en Python

Para el análisis de la señal obtenida, se utilizó Python para filtrar las señales usando Mediana (Reduce el ruido []), Butterworth (0.05Hz - 150Hz), Notch (60Hz) y visualizar la señal:

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
[] J. Cheng, Q. Zou y Y. Zhao, “ECG signal classification based on deep CNN and BiLSTM”, BMC Med. Inform. Decis. Making, vol. 21, n.º 1, diciembre de 2021. Accedido el 21 de septiembre de 2024. [En línea]. Disponible: https://doi.org/10.1186/s12911-021-01736-y
