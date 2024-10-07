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

# Código para Filtrado y Análisis de Señales EMG y ECG

```python
#Librerías importadas
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, cheby1, firwin, freqz, spectrogram, tf2zpk
# Función para cargar la señal desde un archivo
def load_signal(file_name):
    return np.loadtxt(file_name, delimiter='\t', skiprows=1)

# Función para aplicar filtro FIR con ventana de Hamming
def apply_fir_filter(signal, fs, cutoff, numtaps=101):
    taps = firwin(numtaps, cutoff, window='hamming', fs=fs)
    filtered_signal = lfilter(taps, 1.0, signal)
    return filtered_signal, taps

# Función para aplicar filtro IIR Butterworth
def apply_butter_filter(signal, fs, cutoff, order=5):
    b, a = butter(order, cutoff / (0.5 * fs), btype='low')
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal, (b, a)

# Función para aplicar filtro IIR Chebyshev tipo I
def apply_cheby_filter(signal, fs, cutoff, order=5):
    b, a = cheby1(order, 5, cutoff / (0.5 * fs), btype='low')
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal, (b, a)
# Parámetros para señales ECG
fs_ecg = 1000  # Frecuencia de muestreo en Hz para señales ECG
cutoff_ecg = 40  # Frecuencia de corte en Hz para ECG

# Parámetros para señales EMG
fs_emg = 1000  # Frecuencia de muestreo en Hz para señales EMG
cutoff_emg = 60  # Frecuencia de corte en Hz para EMG (eliminar ruido de red)

numtaps_fir = 101  # Número de coeficientes para FIR
# Lista de archivos de las señales ECG y EMG
files_ecg = ['Señal ECG - Estado basal III derivación.txt', 
             'Señal ECG - Estado con Respiracion III deriv.txt', 
             'Señal ECG - Estado sin Respiracion III deriv.txt']

files_emg = ['Señal EMG - bicep braquial en reposo.txt', 
             'Señal EMG - bicep braquial oposición leve.txt', 
             'Señal EMG - bicep braquial oposición fuerte.txt']
# Función para aplicar filtros y mostrar los resultados
def process_signal(signal, fs, cutoff, signal_name):
    # Aplicar los tres filtros
    filtered_signal_fir, taps_fir = apply_fir_filter(signal, fs, cutoff, numtaps=numtaps_fir)
    filtered_signal_butter, coeffs_butter = apply_butter_filter(signal, fs, cutoff)
    filtered_signal_cheby, coeffs_cheby = apply_cheby_filter(signal, fs, cutoff)

    # --- Visualización en el Dominio del Tiempo ---
    plt.figure(figsize=(15, 10))
    
    plt.subplot(311)
    plt.plot(signal, label='Original')
    plt.plot(filtered_signal_fir, label='FIR Filtered', linestyle='--')
    plt.title(f'{signal_name} - FIR Filter Application')
    plt.legend()

    plt.subplot(312)
    plt.plot(signal, label='Original')
    plt.plot(filtered_signal_butter, label='Butterworth Filtered', linestyle='--')
    plt.title(f'{signal_name} - Butterworth Filter Application')
    plt.legend()

    plt.subplot(313)
    plt.plot(signal, label='Original')
    plt.plot(filtered_signal_cheby, label='Chebyshev Filtered', linestyle='--')
    plt.title(f'{signal_name} - Chebyshev Filter Application')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # --- Dominio de la Frecuencia ---
    frecuencia = np.fft.fftfreq(len(signal), 1/fs)
    signal_fft = np.fft.fft(signal)
    plt.figure(figsize=(10, 4))
    plt.plot(frecuencia[:len(frecuencia)//2], np.abs(signal_fft)[:len(frecuencia)//2])
    plt.title(f'Espectro de frecuencia de {signal_name}')
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.show()

    # --- Transformada Corta de Fourier (STFT) ---
    f, t, Sxx = spectrogram(signal, fs, nperseg=256)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title(f'Transformada Corta de Fourier de {signal_name}')
    plt.ylabel("Frecuencia [Hz]")
    plt.xlabel("Tiempo [s]")
    plt.colorbar(label="Potencia [dB]")
    plt.show()

    # --- Diagrama de Polos y Ceros del Filtro FIR ---
    z, p, k = tf2zpk(taps_fir, [1])
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
    plt.title(f"Diagrama de Polos y Ceros del FIR - {signal_name}")
    plt.xlabel("Parte real")
    plt.ylabel("Parte imaginaria")
    plt.grid(True)
    plt.legend()
    plt.show()

    # --- Diagrama de Bode del Filtro FIR ---
    w, h = freqz(taps_fir, 1, worN=2000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(w * fs / (2 * np.pi), 20 * np.log10(abs(h)))
    plt.title(f"Respuesta en frecuencia del FIR - {signal_name}")
    plt.ylabel("Magnitud [dB]")
    plt.grid(True)

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(w * fs / (2 * np.pi), np.angle(h))
    plt.ylabel("Fase [radianes]")
    plt.xlabel("Frecuencia [Hz]")
    plt.grid(True)
    plt.show()
# Procesar señales ECG con los parámetros específicos para ECG
for file_name in files_ecg:
    signal = load_signal(file_name)
    process_signal(signal, fs_ecg, cutoff_ecg, f'ECG - {file_name}')

# Procesar señales EMG con los parámetros específicos para EMG
for file_name in files_emg:
    signal = load_signal(file_name)
    process_signal(signal, fs_emg, cutoff_emg, f'EMG - {file_name}')
