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


### Justificación  <br>

En una señal EMG, un filtro pasabanda es ideal porque permite conservar el rango de frecuencias donde se encuentra la información útil de la actividad muscular, mientras que un filtro pasabaja eliminaría parte de esa información.  <br>

1. Rango relevante de frecuencia: La mayor parte de la energía útil en una señal EMG está entre 20 Hz y 500 Hz. Un filtro pasabaja eliminaría las frecuencias por encima de un umbral, como 20 Hz, lo cual descartaría las frecuencias esenciales en este rango que contienen información crucial sobre la actividad muscular.<br>

2. Eliminación de ruido de baja y alta frecuencia: Un filtro pasabanda permite eliminar tanto el ruido de baja frecuencia (debido a movimientos lentos o interferencias de corriente alterna de 50/60 Hz) como el ruido de alta frecuencia (por ejemplo, artefactos electrónicos o térmicos), manteniendo únicamente la señal muscular.<br>

<p align="justify">

# **Segunda sección - ECG**
