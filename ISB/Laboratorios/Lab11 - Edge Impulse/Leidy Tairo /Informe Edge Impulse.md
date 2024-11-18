# Informe del Laboratorio: Procesamiento de ECG con Edge Impulse

## Tabla de Contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Resultados](#4-resultados)
5. [Conclusiones y Discusiones](#5-conclusiones-y-discusiones)

---

## 1. Introducción

El análisis de señales biomédicas, como el Electrocardiograma (ECG), desempeña un papel crucial en la detección y monitoreo de condiciones cardiovasculares. Este laboratorio tuvo como objetivo procesar señales de ECG adquiridas en diferentes escenarios fisiológicos y simulados, para integrarlas en la plataforma **Edge Impulse**. Mediante herramientas automatizadas, se logró estructurar y analizar estas señales, facilitando su aplicación en sistemas embebidos.

Este informe documenta el proceso completo, desde la recolección de datos hasta la validación del conjunto final en Edge Impulse.

<div align="center">
  
 ![image](https://github.com/user-attachments/assets/05439711-9959-4d8b-baa5-88c15a7bafa8)
 
</div>



---

## 2. Objetivos

1. Adquirir señales de ECG bajo diversas condiciones fisiológicas y simulaciones controladas.
2. Procesar y dividir los datos en segmentos de 10 segundos para su análisis.
3. Subir los segmentos procesados a Edge Impulse y configurar las herramientas disponibles para estructurar un conjunto de datos robusto.
4. Analizar y visualizar las señales procesadas en Edge Impulse para su eventual uso en modelos de aprendizaje automático.

---

## 3. Metodología

### 3.1 Estados Fisiológicos Analizados
Se adquirieron señales de ECG en las siguientes condiciones:
- **Estado Basal:** Registro de ECG en reposo, representando la actividad cardíaca en condiciones de calma.
- **Contención Respiratoria:** Registro durante y después de una pausa respiratoria de 10 segundos.
- **Actividad Física:** Registro tras ejercicios aeróbicos intensos.
- **Simulación (ProSim 4):** Señales simuladas a frecuencias específicas (60, 90, 120 y 150 bpm).

### 3.2 Proceso de Adquisición
Las señales se capturaron utilizando el software **OpenSignals**, exportándose en formato `.txt`. Posteriormente, se procesaron mediante un script en Python para dividir las señales en segmentos de **10 segundos**, asegurando uniformidad en los datos. 

#### Código de Procesamiento
El siguiente script automatizó la conversión y segmentación de los archivos `.txt` en archivos `.csv`:

```python
import numpy as np
import pandas as pd
import os

# Parámetros de Segmentación
Fs = 1000  # Frecuencia de muestreo
segment_duration = 10  # Duración por segmento
samples_per_segment = Fs * segment_duration

# Lista de archivos
file_paths = [
    "D:\\archivos_txt\\Simulacion 60 bpm.txt",
    "D:\\archivos_txt\\Simulacion 90 bpm.txt",
    "D:\\archivos_txt\\Simulacion 120 bpm.txt",
    "D:\\archivos_txt\\Simulacion 150 bpm.txt"
    "D:\\archivos_txt\\Ejercicio I deriv.txt",
    "D:\\archivos_txt\\Ejercicio II deriv.txt",
    "D:\\archivos_txt\\Ejercicio III deriv.txt",
    "D:\\archivos_txt\\Estado basal I deriv.txt",
    "D:\\archivos_txt\\Estado basal III deriv.txt",
    "D:\\archivos_txt\\Estado basal Toma 1 I deriv.txt",
    "D:\\archivos_txt\\Estado basal Toma 2 I deriv.txt",
    "D:\\archivos_txt\\Estado basal Toma 3 I deriv.txt",
    "D:\\archivos_txt\\Estado con Respiracion I deriv.txt",
    "D:\\archivos_txt\\Estado con Respiracion II deriv.txt",
    "D:\\archivos_txt\\Estado con Respiracion III deriv.txt",
    "D:\\archivos_txt\\Estado sin Respiracion I deriv.txt",
    "D:\\archivos_txt\\Estado sin Respiracion II deriv.txt",
    "D:\\archivos_txt\\Estado sin Respiracion III deriv.txt",
]

# Carpeta de salida
output_folder = "D:/archivos_csv"
os.makedirs(output_folder, exist_ok=True)

for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Localizar datos y convertir a array
    data_start = next(i for i, line in enumerate(lines) if "EndOfHeader" in line) + 1
    data = np.array([list(map(float, line.strip().split('\t'))) for line in lines[data_start:]])
    
    # Segmentar datos
    for i in range(len(data) // samples_per_segment):
        segment = data[i * samples_per_segment : (i + 1) * samples_per_segment]
        segment_file = os.path.join(output_folder, f"{os.path.basename(file_path).replace('.txt', '')}_seg_{i + 1}.csv")
        pd.DataFrame(segment).to_csv(segment_file, index=False)
```

### 3.3 Cantidad de Segmentos Generados
| Archivo                     | Segmentos |
|-----------------------------|-----------|
| Simulacion 60 bpm.txt                      | 2                 |
| Simulacion 90 bpm.txt                      | 2                 |
| Simulacion 120 bpm.txt                     | 2                 |
| Simulacion 150 bpm.txt                     | 2                 |
| Ejercicio I deriv.txt                      | 3                 |
| Ejercicio II deriv.txt                     | 3                 |
| Ejercicio III deriv.txt                    | 3                 |
| Estado basal I deriv.txt                   | 6                 |
| Estado basal III deriv.txt                 | 6                 |
| Estado basal Toma 1 I deriv.txt            | 6                 |
| Estado basal Toma 2 I deriv.txt            | 6                 |
| Estado basal Toma 3 I deriv.txt            | 6                 |
| Estado con Respiracion I deriv.txt         | 3                 |
| Estado con Respiracion II deriv.txt        | 3                 |
| Estado con Respiracion III deriv.txt       | 3                 |
| Estado sin Respiracion I deriv.txt         | 2                 |
| Estado sin Respiracion II deriv.txt        | 2                 |
| Estado sin Respiracion III deriv.txt       | 2                 |

### 3.4 Integración con Edge Impulse
1. **Subida de Archivos:** Los segmentos generados se subieron a Edge Impulse utilizando **CSV Wizard**.
2. **Configuración:**
   - Frecuencia de muestreo: **1000 Hz**.
   - Columna principal: Señal de ECG.
3. **Organización:** Los datos se dividieron en conjuntos de entrenamiento y prueba.


## 4. Resultados

### 4.1 Segmentos Generados y Distribución

| Categoría       | Entrenamiento | Prueba | Total de Segmentos | Duración Total (s) |
|------------------|---------------|--------|--------------------|--------------------|
| Estado Basal    | 45            | 14     | 59                 | 590                |

Cada segmento tiene una duración estándar de **10 segundos**.

---

### 4.2 Visualización de Señales

#### Estado Basal
Registro de ECG en reposo, representando la actividad cardíaca en condiciones de calma.

<div align="center">
  
 ![image](https://github.com/user-attachments/assets/6342ca8d-9b85-4ac9-8356-2f9d6f9c75be)
 
</div>

#### Contención Respiratoria:
Registro durante y después de una pausa respiratoria de 10 segundos.

<div align="center">
  
 ![image](https://github.com/user-attachments/assets/c29e99a2-824b-4d3b-8f63-52f68daeea9e)

</div>

#### Actividad Física:
Registro tras ejercicios aeróbicos intensos.

<div align="center">
  
![image](https://github.com/user-attachments/assets/9fad995f-2c48-4712-af10-6c3bb98bd084)

</div>

#### Simulación (ProSim 4):

Señales simuladas a frecuencias específicas (60, 90, 120 y 150 bpm).

<div align="center">
  
![image](https://github.com/user-attachments/assets/7ee7ce63-3e38-4973-af26-d44454af7fbd)

</div>
---

### 4.3 Dataset en Edge Impulse

El proyecto está organizado en los conjuntos de entrenamiento y prueba:

#### Conjunto de Entrenamiento
- **Total de Segmentos:** 45
- **Duración Total:** 450 segundos (7 minutos y 30 segundos)

#### Conjunto de Prueba
- **Total de Segmentos:** 14
- **Duración Total:** 140 segundos (2 minutos y 20 segundos)
  
<div align="center">
  
 ![image](https://github.com/user-attachments/assets/d59a5d9b-502a-4e1b-9d36-9bb78e6b9fdd)
 
</div>

---

### 4.4 Link al Proyecto

Puedes acceder al proyecto completo en Edge Impulse mediante el siguiente enlace:  
[Proyecto Leidy Tairo en Edge Impulse](https://studio.edgeimpulse.com/public/560603/live)

---

## 5. Conclusiones y Discusiones

### 5.1 Conclusiones

1. **Adquisición y Preprocesamiento de Señales:**
   - Se logró adquirir, segmentar y estructurar señales de ECG con un total de 59 segmentos, distribuidos entre conjuntos de entrenamiento y prueba. 
   - El procesamiento automatizado mediante un script en Python facilitó la conversión de señales en formato `.txt` a segmentos manejables en formato `.csv`.

2. **Uso de Edge Impulse:**
   - La plataforma Edge Impulse demostró ser una herramienta eficiente para organizar datos biomédicos, permitiendo la categorización y visualización de señales de ECG.
   - La funcionalidad del **CSV Wizard** simplificó la integración de los datos preprocesados, garantizando una configuración adecuada de la frecuencia de muestreo y las columnas de interés.
---

### 5.2 Discusiones

1. **Impacto de la Duración de los Segmentos:**
   - La elección de segmentos de 10 segundos proporciona una buena resolución temporal para el análisis de patrones en señales ECG. Sin embargo, explorar duraciones más cortas o más largas podría ser relevante dependiendo del caso de uso final.

2. **Edge Impulse como Plataforma:**
   - La facilidad para integrar datos y visualizar señales confirma el potencial de Edge Impulse en aplicaciones biomédicas. No obstante, el entrenamiento de modelos más complejos requerirá datasets más ricos y variados.

---

### 5.3 Recomendaciones

1. **Validar el Modelo:**
   - Una vez configurado el dataset completo, entrenar y evaluar un modelo de aprendizaje automático para clasificar las señales según las categorías definidas.

2. **Optimización para Dispositivos Embebidos:**
   - Reducir la complejidad de los modelos entrenados para garantizar su implementación en sistemas embebidos con recursos limitados.

---

Este proyecto establece una base sólida para futuros análisis y desarrollos, destacando la importancia de un dataset bien estructurado y preprocesado en aplicaciones de machine learning biomédico.

