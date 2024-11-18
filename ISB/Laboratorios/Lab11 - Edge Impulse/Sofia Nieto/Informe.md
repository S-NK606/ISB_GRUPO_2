# Informe del Laboratorio de Edge Impulse
## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Resultados](#4-resultados)

# 1. Introducción
Edge Impulse es una plataforma web diseñada específicamente para desarrollar modelos de aprendizaje automático (ML) que se ejecutan en dispositivos como microcontroladores, sensores, wearables y otro hardware con capacidad de procesamiento y memoria limitadas, simplificando la adquisición de datos al permitir a los desarrolladores recopilarlos y organizarlos directamente desde los dispositivos mencionados. Asimismo, esta plataforma contiene herramientas de procesamiento de señales y funciones que permiten extraer información significativa de los datos brutos de los sensores, con el fin de detectar patrones de movimiento a partir de las lecturas adquiridas. De esta manera, los modelos de aprendizaje automático pueden entrenarse directamente en Edge Impulse utilizando marcos populares como TensorFlow y ONNX, facilitando su uso en varios dispositivos, como Arduino, Raspberry Pi y placas STMicroelectronics.

La plataforma es especialmente valiosa por su capacidad de realizar procesamiento en tiempo real directamente en los dispositivos periféricos, eliminando la necesidad de servicios en la nube, reduciendo la latencia y ahorrando el ancho de banda, que permite una mayor privacidad de los datos. Por último, esta plataforma se utiliza ampliamente en sectores como la sanidad, donde impulsa wearables para la monitorización de la salud, y en el IoT industrial para tareas como el mantenimiento predictivo y el control de calidad

# 2. Objetivos

## 2.1. Objetivo General
- Clasificar señales EEG mediante un modelo de aprendizaje automático desarrollado en Edge Impulse.

## 2.2. Objetivos Específicos
- Adquirir y organizar señales EEG según los diferentes ejercicios en un formato compatible para subirlos a Edge Impulse
- Segmentar y etiquetar las señales EEG según eventos específicos o estados, asegurando compatibilidad con Edge Impulse.
- Subir las señales preprocesadas a Edge Impulse y organizarlas en categorías claras para entrenamiento.
- Diseñar y entrenar un modelo de aprendizaje automático en Edge Impulse utilizando técnicas optimizadas para la clasificación de EEG.

# 3. Metodología
## 3.1. Descripción y Adquisición de los Datos

Para este laboratorio se usaron las señales EEG adquiridas durante el laboratorio N° usando el kit BITalino (r) evolution y el programa OpenSignal para la visualización y adquisición de la señal. 

Las señales de EEG fueron adquiridas durante tres actividades:

- Primer estado de Reposo: Se realizó un registro inicial de la señal de EEG en condiciones de reposo absoluto. Durante este periodo, el participante permaneció en silencio, respirando de manera normal, con los ojos cerrados y evitando movimientos musculares oculares. Este paso fue fundamental para obtener una referencia base con bajo nivel de ruido, que sirviera como control para las actividades posteriores.

- Ejercicio de ciclo de ojos cerrados y ojos abiertos: Se llevaron a cabo cinco ciclos alternados de abrir y cerrar los ojos, cada fase manteniéndose durante cinco segundos. Este ejercicio permitió capturar variaciones en la actividad cerebral asociadas con estados de vigilia visual y relajación ocular. Los datos obtenidos reflejan la transición entre ritmos alfa (ojos cerrados) y ritmos beta (ojos abiertos), ayudando a evaluar la respuesta cortical a estímulos visuales.

- Segunto estado de Reposo: Se repitió el registro de señal en reposo bajo las mismas condiciones del paso 1, asegurando la comparabilidad de los datos en diferentes momentos del experimento. Este segundo registro permitió verificar la estabilidad de la línea base y evaluar posibles cambios en la señal tras los ciclos previos.

- Ejercicio de Razonamiento Matemático: Durante esta fase, un compañero del equipo leyó en voz alta una serie de ejercicios matemáticos diseñados para estimular el procesamiento cognitivo. El participante debía resolver mentalmente cada problema mientras mantenía la mirada fija en un punto específico, reduciendo al mínimo los movimientos oculares y posibles artefactos. Este paso tuvo como objetivo evaluar la actividad cerebral durante un estado de concentración cognitiva intensa y compararla con las señales registradas en reposo.

Las señales presentaron una frecuencia de muestreo de 1000 Hz, con intervalos de tiempo que variaron entre 30 y 90 segundos, las cuales se exportaron como archivos txt.





