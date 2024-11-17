# Laboratorio de Edge Impulse 

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Resultados](#4-resultados)


## 1. Introducción

Edge Impulse es una plataforma diseñada para desarrollar algoritmos de aprendizaje automático (machine learning) específicamente optimizados para sistemas embebidos y dispositivos que operan en tiempo real. Su principal objetivo es simplificar las etapas de adquisición, procesamiento de datos y generación de modelos de machine learning.

Esta herramienta resulta especialmente útil en aplicaciones como el análisis y procesamiento de señales biomédicas, por ejemplo, el electrocardiograma (ECG), donde se requiere precisión y rapidez en el procesamiento de datos para tareas como el monitoreo continuo y el diagnóstico médico.

En este informe se detallará el proceso de adquisición de datos y su integración con Edge Impulse como punto de partida para la creación de un proyecto completo. La documentación incluirá cada uno de los pasos necesarios, desde la recolección inicial de las señales hasta la configuración y entrenamiento del modelo, buscando optimizar el rendimiento en un entorno embebido y demostrar la utilidad de esta plataforma en el análisis en tiempo real de datos biomédicos.
<div align="center">
  <img src="./Imagenes/imagen1.png"><p>

  **Figura 1. Página inicial Edge Impulse**
  </p>
</div>

## 2. Objetivos
1. Organizar y adquirir señales de ECG: Capturar señales de ECG en diferentes estados fisiológicos (reposo, actividad, estrés, etc.) asegurando que estén en un formato adecuado para su uso y análisis posterior.
2. Procesar y pre-etiquetar las señales: Realizar una limpieza inicial de los datos adquiridos (remoción de ruido, normalización, etc.) y etiquetarlas según los estados fisiológicos correspondientes
3. Subir y organizar los datos en Edge Impulse: Integrar las señales preprocesadas en la plataforma Edge Impulse, categorizándolas de manera clara y sistemática para facilitar el entrenamiento del modelo.
4. Diseñar y entrenar un modelo de aprendizaje automático: Utilizar los datos organizados para crear un modelo de machine learning que pueda clasificar o analizar señales de ECG en tiempo real.
5. Validar y evaluar el modelo: Implementar pruebas para medir la precisión, sensibilidad y especificidad del modelo desarrollado, asegurando que cumpla con los estándares requeridos para aplicaciones biomédicas.
6. Optimizar el modelo para dispositivos embebidos: Reducir la complejidad del modelo para garantizar su desempeño eficiente en sistemas embebidos.


## 3. Metodología

# Adquisición de datos y conversión de formato

En este repositorio de GitHub se documentó el proceso de adquisición de señales de ECG bajo diferentes condiciones fisiológicas, detalladas de la siguiente manera:

## Estados registrados

- **Estado basal**  
  Se registró la actividad del ECG mientras el estudiante se encontraba en reposo, en un estado de calma y relajación.

- **Estado de pausa respiratoria (durante y después)**  
  El estudiante realizó una pausa respiratoria de 10 segundos, registrándose el ECG durante este intervalo. Posteriormente, se realizó un segundo registro para analizar las variaciones en la señal tras la contención de la respiración.

- **Estado posterior a actividad física**  
  El ECG se obtuvo después de que el estudiante realizara ejercicios aeróbicos intensos durante aproximadamente 5 minutos, alcanzando un estado de fatiga.

- **Simulación con ProSim 4**  
  Se incluyeron señales generadas por el ProSim 4, un simulador portátil de signos vitales utilizado para pruebas rápidas con frecuencias cardíacas específicas: 60, 90, 120 y 150 bpm.

## Procesamiento de las señales

Las señales fueron adquiridas utilizando el software **OpenSignals**, que permitió exportarlas en formato **.txt**. 

Para estandarizar los datos y prepararlos para su integración en Edge Impulse, se implementó un código que dividió cada señal en segmentos de 10 segundos. Esta segmentación facilita su manejo y análisis en etapas posteriores del proyecto.









## 4. Resultados
