# Informe de Análisis de Señales EMG y ECG

Este informe presenta el análisis de seis señales EMG y ECG obtenidas en las sesiones previas, donde se aplicaron tres tipos de filtros a cada señal: FIR, Butterworth y Chebyshev. El análisis incluye visualizaciones de las señales originales y filtradas, así como la respuesta en frecuencia y los diagramas de polos y ceros de cada filtro.

---

## 1. Señal ECG - Estado Basal III Derivación

### Descripción de la Señal

Esta señal ECG representa el estado basal del corazón, capturando la actividad eléctrica durante el reposo. La señal está propensa a interferencias de red y ruido de alta frecuencia que deben ser eliminados sin afectar las ondas importantes (P, QRS, T).

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Se seleccionó un filtro FIR con ventana de Hamming para asegurar una fase lineal y evitar distorsión en la temporalidad de las ondas.
   - **Parámetros**: Frecuencia de corte de 40 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: El filtro Butterworth fue elegido por su respuesta plana en la banda de paso, lo que evita distorsionar la amplitud de las ondas importantes.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: Proporciona una atenuación rápida en la banda de parada, útil para eliminar interferencias de alta frecuencia, aunque introduce ondulaciones en la banda de paso.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, ondulación de 5 dB en la banda de paso.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**: 
- **Gráfica en el Dominio de la Frecuencia**: 
- **Transformada corta de Fourier**: 

### Análisis del Filtro

- **Diagrama de Polos y Ceros**: 
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## 2. Señal ECG - Estado con Respiración III Derivación

### Descripción de la Señal

Esta señal ECG incluye variaciones debidas a la respiración, lo que puede introducir artefactos por el movimiento del tórax. Es esencial filtrar este ruido mientras se preservan las características de la señal.

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Al igual que en la señal en reposo, el filtro FIR con ventana de Hamming es ideal para mantener la integridad temporal de la señal, crucial para el análisis ECG.
   - **Parámetros**: Frecuencia de corte de 40 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: Se utiliza el filtro Butterworth por su capacidad de mantener la amplitud de las ondas en la banda de paso.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: Permite una atenuación más rápida de las frecuencias no deseadas debidas a la respiración.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, ondulación de 5 dB en la banda de paso.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**: 
- **Gráfica en el Dominio de la Frecuencia**:
- **Transformada corta de Fourier**: 

### Análisis del Filtro

- **Diagrama de Polos y Ceros**: 
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## 3. Señal ECG - Estado sin Respiración III Derivación

### Descripción de la Señal

La señal ECG sin respiración elimina el movimiento del tórax, facilitando la evaluación directa de la actividad cardíaca. El ruido de red y las frecuencias más altas aún pueden estar presentes, lo que justifica el uso de filtros para limpiarla.

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Este filtro asegura una fase lineal, importante para mantener la integridad de la señal cardíaca.
   - **Parámetros**: Frecuencia de corte de 40 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: Su respuesta plana en la banda de paso permite eliminar eficientemente el ruido sin distorsionar la señal.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: El Chebyshev permite una rápida atenuación de las frecuencias fuera de la banda de interés.
   - **Parámetros**: Orden 5, frecuencia de corte de 40 Hz, ondulación de 5 dB.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**: 
- **Gráfica en el Dominio de la Frecuencia**: 
- **Transformada corta de Fourier**:

### Análisis del Filtro

- **Diagrama de Polos y Ceros**:
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## 4. Señal EMG - Bíceps Braquial en Reposo

### Descripción de la Señal

La señal EMG en reposo refleja la actividad muscular del bíceps sin contracción. Los principales artefactos son ruido de red y potenciales interferencias externas, por lo que se deben eliminar sin alterar las características de la señal en reposo.

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Se selecciona para eliminar el ruido de red sin afectar la temporalidad de la señal en reposo.
   - **Parámetros**: Frecuencia de corte de 60 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: Proporciona una eliminación efectiva del ruido sin afectar las bajas frecuencias, que son las más importantes en reposo.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: Su atenuación rápida permite eliminar el ruido de red de forma eficiente.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, ondulación de 5 dB.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**:
- **Gráfica en el Dominio de la Frecuencia**: 
- **Transformada corta de Fourier**: 

### Análisis del Filtro

- **Diagrama de Polos y Ceros**:
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## 5. Señal EMG - Bíceps Braquial Oposición Leve

### Descripción de la Señal

Esta señal refleja la actividad muscular bajo una leve contracción. Los artefactos más comunes incluyen la interferencia de red y ruidos de baja frecuencia que no corresponden a la actividad muscular.

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Permite eliminar el ruido de red de 60 Hz sin afectar la integridad temporal de la señal EMG.
   - **Parámetros**: Frecuencia de corte de 60 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: Su atenuación suave en la banda de paso es ideal para preservar la señal EMG durante contracción leve.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: Es útil para atenuar rápidamente las frecuencias no deseadas por encima de 60 Hz.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, ondulación de 5 dB.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**: 
- **Gráfica en el Dominio de la Frecuencia**: 
- **Transformada corta de Fourier**: 

### Análisis del Filtro

- **Diagrama de Polos y Ceros**: 
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## 6. Señal EMG - Bíceps Braquial Oposición Fuerte

### Descripción de la Señal

Esta señal refleja la actividad del bíceps bajo una fuerte contracción. Las frecuencias de interés están más distribuidas, pero el ruido de red y los artefactos de alta frecuencia aún deben ser eliminados.

### Filtros Aplicados y Justificación

1. **Filtro FIR con Ventana de Hamming**:
   - **Justificación**: Permite eliminar el ruido de red mientras se mantiene la fase lineal, esencial en señales EMG de alta intensidad.
   - **Parámetros**: Frecuencia de corte de 60 Hz, número de coeficientes: 101, fs: 1000 Hz.

2. **Filtro IIR Butterworth**:
   - **Justificación**: Proporciona una respuesta en frecuencia suave que es útil para mantener la integridad de la señal durante contracciones fuertes.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, fs: 1000 Hz.

3. **Filtro IIR Chebyshev Tipo I**:
   - **Justificación**: Su capacidad para atenuar rápidamente las frecuencias no deseadas es clave para señales con altos niveles de contracción muscular.
   - **Parámetros**: Orden 5, frecuencia de corte de 60 Hz, ondulación de 5 dB.

### Análisis de Señales

- **Gráfica en el Dominio del Tiempo**: 
- **Gráfica en el Dominio de la Frecuencia**: 
- **Transformada corta de Fourier**: 

### Análisis del Filtro

- **Diagrama de Polos y Ceros**: 
- **Diagrama de Bode (Magnitud y Fase)**: 

---

## Conclusiones

El análisis de las señales EMG y ECG utilizando tres tipos diferentes de filtros ha permitido identificar las técnicas más adecuadas para cada tipo de señal. Los filtros FIR, Butterworth y Chebyshev presentan distintas ventajas según el contexto: los FIR son ideales para mantener la fase, mientras que los IIR permiten una atenuación más rápida de las frecuencias no deseadas. Esta combinación de filtros asegura una correcta preservación de la señal útil y la eliminación eficiente de ruidos y artefactos.

