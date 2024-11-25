# LABORATORIO 13: Nueva generación en Edge Impulse
Link del proyecto en EDGE IMPULSE (con correcciones del laboratorio anterior): https://studio.edgeimpulse.com/public/566105/live
## Contenido de la sesión

1. [Informe Laboratorio](#id1)
    - [Corrección Dataset](#id2)
    - [Create Impulse](#id3)
    - [Spectral features](#id4)
    - [Classifier](#id5)
    - [Retrain](#id6)
    - [Model Testing](#id7)


## 1. Informe Laboratorio <a name="id1"></a>

### 1.1 Corrección Dataset <a name="id2"></a>

#### Arreglo de Data
<div align="center">
  
  ![image](https://github.com/user-attachments/assets/7cf5058b-b97d-4d26-aa26-f901af433323)
  
  </p>
</div>

### 1.2 Create Impulse <a name="id3"></a>
Creamos el diseño y lo configuramos:
Configuramos el window size de 7000 milisegundos y un window increase de 500 milisegundos, la frecuencia de sampleo es de 1000 Hz, usamos Análisis Espectral y el clasificador.

<div align="center">
  
  ![image](https://github.com/user-attachments/assets/eb0cb5ce-87a8-4fb0-b1b0-99fd18cd2d1b)


  </p>
</div>

### 1.3 Spectral features <a name="id4"></a>
Parámetros elegidos
#### Parámetros
<div align="center">
  
  ![image](https://github.com/user-attachments/assets/9060fe4f-1e2f-4873-baa8-71b04613dcb2)

  </p>
</div>

### 1.4 Classifier <a name="id5"></a>
#### Classifier
<div align="center">

  ![image](https://github.com/user-attachments/assets/f9e6681a-420f-42b6-8605-a96ef9616d8a)

  </p>
</div>

#### Training output
<div align="center">

![image](https://github.com/user-attachments/assets/f52ee2b1-3757-4058-8428-4b2023fcf972)

![image](https://github.com/user-attachments/assets/66460bc2-338a-4de7-8a19-559ceda78728)




  </p>
</div>

### 1.5 Retrain <a name="id6"></a>
#### Retraining output
<div align="center">

  ![image](https://github.com/user-attachments/assets/36888050-76a2-4aa3-a8de-ca7176b19543)


  </p>
</div>

### 1.6 Model Testing <a name="id7"></a>
#### Métricas:
<div align="center">
  
 ![image](https://github.com/user-attachments/assets/1c021c0a-57a0-49fb-b512-248a4f761ca6)

  </p>
</div>

Comentarios: 
Las métricas mostradas indican un rendimiento deficiente del modelo en el conjunto de validación, con una precisión general del 29.3% y una pérdida de 2.30. La matriz de confusión evidencia problemas de clasificación, destacando que las clases como "CON RESPIRACIÓN" y "ESTADO BASAL" tienen una F1 Score de 0, lo que implica que el modelo no está identificando correctamente estas categorías. Aunque la clase "EJERCICIO" tiene el mejor desempeño relativo con un F1 Score de 0.51, el modelo sigue mostrando confusión significativa en la mayoría de las categorías. Las métricas globales, como un área bajo la curva (AUC) de 0.57 y un F1 Score ponderado de 0.22, refuerzan la necesidad de optimización y ajuste del modelo, posiblemente mediante una revisión del balance de clases, ajustes de hiperparámetros o mejoras en los datos de entrenamiento.
