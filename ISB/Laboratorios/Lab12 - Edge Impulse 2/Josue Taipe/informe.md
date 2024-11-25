# LABORATORIO 13: Generacion Impulso Edge Impulse


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
[https://studio.edgeimpulse.com/studio/560365/acquisition/training?page=1 ](https://studio.edgeimpulse.com/public/560482/live)

#### Imagen 1: Arreglo de Data
<div align="center">
  <img src="./Imagenes/TRAI.png"><p>

  </p>
</div>

### 1.2 Create Impulse <a name="id3"></a>
Creamos el diseño y lo configuramos:
Configuramos el window size de 1,9seg y un window increase de 1seg, la frecuencia de sampleo es de 1000 Hz, usamos Análisis Espectral y el clasificador.


<div align="center">
  <img src="./Imagenes/paso1.png"><p>

  </p>
</div>





### 1.3 Spectral features <a name="id4"></a>
Parámetros elegidos
#### Imagen 4: Parametros
<div align="center">
  <img src="./Imagenes/paso2.png"><p>

  </p>
</div>

### 1.4 Classifier <a name="id5"></a>
#### Imagen 5: Classifier
<div align="center">
  <img src="./Imagenes/paso3.png"><p>

  </p>
</div>

#### Imagen 5: Training output
<div align="center">
  <img src="./Imagenes/paso4.png"><p>
  <img src="./Imagenes/paso4.1.png"><p>

  </p>
</div>

### 1.5 Retrain <a name="id6"></a>
#### Imagen 6: Retraining output
<div align="center">
  <img src="./Imagenes/paso5.png"><p>

  </p>
</div>

### 1.6 Model Testing <a name="id7"></a>
#### Imagen 7: Matriz de Confusión:
<div align="center">
  <img src="./Imagenes/paso6.png"><p>
  <img src="./Imagenes/paso6.1.png"><p>

  </p>
</div>

Comentarios: 
El modelo presenta un bajo desempeño con un accuracy de 14.62%, lo que evidencia problemas significativos en la clasificación. Las métricas como precision, recall y F1 Score son muy bajas, y la matriz de confusión muestra que las clases tienen un alto nivel de incertidumbre ("UNCERTAIN") y solapamiento, siendo "BASAL" la única clase con un desempeño moderado (55.3%). Esto se debe  a una insuficiencia de datos, solapamiento entre clases, y características que no capturan adecuadamente las diferencias.

















