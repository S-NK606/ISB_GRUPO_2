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


## 4. Resultados
