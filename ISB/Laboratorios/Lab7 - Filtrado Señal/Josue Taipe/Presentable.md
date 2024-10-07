# **LABORATORIO 7: – Filtrado de señales EMG y ECG**

Este entregable fue elaboración personal - Josue Francisco Taipe Callañaupa (75504516)

# **Primera sección - EMG**



### Análisis de señales y del filtro  <br>

Usaré el tipo de filtro FIR <br>
<p align="justify">

### **Biceps reposo** <br>

<p align="center"> Señal BICEPS REPOSO - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/BicepreposoDOMTIEMPO.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS RELAJADO - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepreposoFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS RELAJADO - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepreposoTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS RELAJADO - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepreposoPOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS RELAJADO - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepreposoBOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Biceps con contracción leve** <br>
<p align="center"> Señal BICEPS LEVE - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepleveDOMINIO.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS LEVE - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepleveFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS LEVE - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepleveTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS LEVE - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/biceplevePOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS LEVE - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepleveBOLE.png" width="600" height="266"></p>
</p
<p align="justify">

### **Biceps con fuerte contracción** <br>

<p align="center"> Señal BICEPS FUERTE - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepfuerteDOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS FUERTE - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepfuerteFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS FUERTE - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepfuerteTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS FUERTE - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepfuertePOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal BICEPS FUERTE - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/bicepfuerteBOLE.png" width="600" height="266"></p>
</p
  
<p align="justify">

### Justificación  <br>

Para esta actividad, decidí usar un filtro pasabanda ya que permite conservar el rango de frecuencias donde se encuentra la información útil de la actividad muscular, mientras que un filtro pasabaja eliminaría parte de esa información.  <br>

1. Rango relevante de frecuencia: La mayor parte de la energía útil en una señal EMG está entre 20 Hz y 500 Hz. Un filtro pasabaja eliminaría las frecuencias por encima de un umbral, como 20 Hz, lo cual descartaría las frecuencias esenciales en este rango que contienen información crucial sobre la actividad muscular.<br>

2. Eliminación de ruido de baja y alta frecuencia: Un filtro pasabanda permite eliminar tanto el ruido de baja frecuencia (debido a movimientos lentos o interferencias de corriente alterna de 50/60 Hz) como el ruido de alta frecuencia (por ejemplo, artefactos electrónicos o térmicos), manteniendo únicamente la señal muscular.<br>

<p align="justify">

# **Segunda sección - ECG**



### Análisis de señales y del filtro  <br>

Usaré el tipo de filtro FIR <br>
<p align="justify">

### **Primera derivación** <br>

<p align="center"> Señal Primera derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/1derivDOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Primera derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/1derivFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Primera derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/1derivTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Primera derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/1derivPOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Primera derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/1derivBOLE.png" width="600" height="266"></p>
</p
<p align="justify">

### **Segunda derivación** <br>

<p align="center"> Señal Segunda derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/2derivDOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Segunda derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/2derivFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Segunda derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/2derivTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Segunda derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/2derivPOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Segunda derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/2derivBOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Tercera derivación** <br>
<p align="center"> Señal Tercera derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/3derivDOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Tercera derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/3derivFREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Tercera derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/3derivTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Tercera derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/3derivPOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Tercera derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/3derivBOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Estado Basal Primera derivación** <br>

<p align="center"> Señal Estado Basal Primera derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Basal Primera derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Basal Primera derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1FT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Basal Primera derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Basal Primera derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1BOLE.png" width="600" height="266"></p>
</p
<p align="justify">

  
### **Estado Respiración Primera derivación** <br>

<p align="center"> Señal Estado Respiración Primera derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/respiracion1DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Respiración Primera derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/respiracion1FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Respiración Primera derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/respiracion1TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Respiración Primera derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/respiracion1POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Respiración Primera derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/respiracion1BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Estado Sin Respiración Primera derivación** <br>
<p align="center"> Señal Estado Sin Respiración Primera derivación - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/sinrespi1DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Sin Respiración Primera derivación - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/sinrespi1FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Sin Respiración Primera derivación - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/sinrespi1TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Sin Respiración Primera derivación - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/sinrespi1POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal Estado Sin Respiración Primera derivación - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/sinrespi1BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Usando el fluke a 60 BPM** <br>
<p align="center"> Señal 60 BPM - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/60DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 60 BPM - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/60FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 60 BPM - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/60TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 60 BPM - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/60POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 60 BPM - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/60BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Usando el fluke a 90 BPM** <br>
<p align="center"> Señal 90 BPM - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/90DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 90 BPM - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/90FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 90 BPM- Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/90TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 90 BPM - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/90POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 90 BPM - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/90BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Usando el fluke a 120 BPM** <br>

<p align="center"> Señal 120 BPM - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/120DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 120 BPM - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/120FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 120 BPM - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/120TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 120 BPM - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/120POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 120 BPM - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/120BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### **Usando el fluke a 150 BPM** <br>


<p align="center"> Señal 150 BPM - Dominio del Tiempo 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150BPM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150BTFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150BPOLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150BBOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### Justificación  <br>

El filtro FIR pasabaja fue elegido específicamente para asegurar que la señal ECG mantenga su integridad y claridad, eliminando eficientemente las interferencias y el ruido que podrían afectar el análisis clínico de la señal. <br>

1. Rango de frecuencias de interés para ECG: Las señales ECG tienen frecuencias significativas en el rango de 0.5 Hz a 100 Hz. Los componentes de alta frecuencia suelen ser ruido o artefactos que pueden distorsionar la interpretación de la señal. <br>

2. Eliminación de ruido de alta frecuencia: Un filtro pasabaja es ideal para este caso, ya que permite preservar las frecuencias bajas que son características de la señal ECG, mientras que elimina las componentes de alta frecuencia que no contienen información relevante para el análisis del ECG.<br>

3.Uso de la ventana de Hamming: Esta ventana es utilizada por su capacidad de minimizar las ondulaciones en la respuesta del filtro (ripple), ofreciendo una buena atenuación en la banda de parada sin comprometer significativamente la respuesta de la señal en la banda de paso.

























