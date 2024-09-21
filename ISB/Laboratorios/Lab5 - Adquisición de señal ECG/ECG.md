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

Para el análisis de la señal obtenida, se utilizó Python para filtrar y visualizar la señal:

- Estados de reposo
   - 1ra derivación
     ![FFT de la señal filtrada](ISB/Laboratorios/Lab5-Adquisición-de-señal-ECG/Imagenes/ECG/Estado_con_respiración_1ra_derivación_fft_senal_filtrada.png)
   - 2da derivación
   - 3ra derivación
- ECG durante la conteción de respiración
   - Respiración (1ra derivación)
   - Post-Respiración (1ra derivación)
   - Respiración (2da derivación)
   - Post-Respiración (2da derivación)
   - Respiración (3ra derivación)
   - Post-Respiración (3ra derivación)
- Estado de ejercicio
   - 1ra derivación
   - 2da derivación
   - 3ra derivación

## Referencias

