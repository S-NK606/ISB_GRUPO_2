# LABORATORIO 5: – USO DE BITalino PARA ECG

### Tabla de contenidos

------------

1. [Objetivos](#objetivos)
2. [Materiales y equipos](#materiales-y-equipos)
3. [Resultados](#resultados)
   1. [Conexión usada](#conexion-usada)
   2. [Video de la señal](#video-de-la-señal)
   3. [Ploteo de la señal en Python](#ploteo-de-la-señal-en-python)
4. [Referencias](#referencias)

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
   - Respiración (1ra derivación)
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
   - Post-Respiración (1ra derivación)
   - Respiración (2da derivación)
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
   - Post-Respiración (2da derivación)
   - Respiración (3ra derivación)
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
   - Post-Respiración (3ra derivación)
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
     

## Referencias
[] J. Cheng, Q. Zou y Y. Zhao, “ECG signal classification based on deep CNN and BiLSTM”, BMC Med. Inform. Decis. Making, vol. 21, n.º 1, diciembre de 2021. Accedido el 21 de septiembre de 2024. [En línea]. Disponible: https://doi.org/10.1186/s12911-021-01736-y
