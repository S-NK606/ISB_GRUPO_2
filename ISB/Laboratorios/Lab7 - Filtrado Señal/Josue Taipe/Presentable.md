# **LABORATORIO 7: – Filtrado de señales EMG y ECG**

Este entregable fue elaboración personal - Josue Francisco Taipe Callañaupa (75504516) <br>
El codigo que se usó para este trabajo, está comentado en este archivo .md
# **Primera sección - EMG**

<!-- CODIGO USADO PARA FILTRAR LA SEÑAL EMG 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz, spectrogram, tf2zpk

# Leer los datos del archivo EMG
data = np.loadtxt(r'D:\UNIV\Introducción Señales\SeñalesFILTRO\EMG\BICEPFUERTE.txt', skiprows=4)  # Ajusta este archivo
emg_signal = data[:, 5]  # Extraer la columna EMG (A1)
fs = 1000  # Frecuencia de muestreo en Hz 

# --- Sección 1: Análisis de señales ---
# Dominio del tiempo
time = np.arange(len(emg_signal)) / fs
plt.figure(figsize=(10, 4))
plt.plot(time, emg_signal)
plt.title("Señal EMG en el dominio del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia
frecuencia = np.fft.fftfreq(len(emg_signal), 1/fs)
emg_fft = np.fft.fft(emg_signal)
plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(emg_fft)[:len(frecuencia)//2])
plt.title("Espectro de frecuencia de la señal EMG")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

# Transformada corta de Fourier (STFT)
f, t, Sxx = spectrogram(emg_signal, fs, nperseg=256)
plt.figure(figsize=(10, 4))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title("Transformada de Fourier de tiempo corto (STFT)")
plt.ylabel("Frecuencia [Hz]")
plt.xlabel("Tiempo [s]")
plt.colorbar(label="Potencia [dB]")
plt.show()

# --- Sección 2: Análisis del filtro ---
# Parámetros del filtro FIR
cutoff_frequencies = [20, 450]  # Frecuencias de corte para la señal EMG
numtaps = 101  # Número de coeficientes del filtro
filtro_fir = firwin(numtaps, cutoff_frequencies, pass_zero=False, fs=fs)

# Aplicar el filtro FIR a la señal EMG
emg_filtrada = lfilter(filtro_fir, 1.0, emg_signal)

# Diagrama de polos y ceros
z, p, k = tf2zpk(filtro_fir, [1])
plt.figure(figsize=(6, 6))
plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
plt.title("Diagrama de polos y ceros del filtro FIR")
plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
plt.grid(True)
plt.legend()
plt.show()

# Diagrama de Bode (magnitud y fase)
w, h = freqz(filtro_fir, 1, worN=2000)
plt.figure(figsize=(10, 6))

# Magnitud
plt.subplot(2, 1, 1)
plt.plot(w * fs / (2 * np.pi), 20 * np.log10(abs(h)))
plt.title("Respuesta en frecuencia del filtro FIR")
plt.ylabel("Magnitud [dB]")
plt.grid(True)

# Fase
plt.subplot(2, 1, 2)
plt.plot(w * fs / (2 * np.pi), np.angle(h))
plt.ylabel("Fase [radianes]")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)

plt.show()

 -->

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

<!-- CODIGO USADO PARA FILTRAR LA SEÑAL ECG 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz, spectrogram, tf2zpk

# Leer los datos del archivo ECG
data = np.loadtxt(r'D:\UNIV\Introducción Señales\SeñalesFILTRO\ECG\Simulacion 150 bpm.txt', skiprows=4)  # Ajusta este archivo
ecg_signal = data[:, 5]  # Extraer la columna ECG (A1)
fs = 1000  # Frecuencia de muestreo en Hz

# --- Sección 1: Análisis de señales ---
# Dominio del tiempo
time = np.arange(len(ecg_signal)) / fs
plt.figure(figsize=(10, 4))
plt.plot(time, ecg_signal)
plt.title("Señal ECG en el dominio del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia
frecuencia = np.fft.fftfreq(len(ecg_signal), 1/fs)
ecg_fft = np.fft.fft(ecg_signal)
plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(ecg_fft)[:len(frecuencia)//2])
plt.title("Espectro de frecuencia de la señal ECG")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

# Transformada corta de Fourier (STFT)
f, t, Sxx = spectrogram(ecg_signal, fs, nperseg=256)
plt.figure(figsize=(10, 4))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title("Transformada de Fourier de tiempo corto (STFT) para la señal ECG")
plt.ylabel("Frecuencia [Hz]")
plt.xlabel("Tiempo [s]")
plt.colorbar(label="Potencia [dB]")
plt.show()

# --- Sección 2: Análisis del filtro ---
# Parámetros del filtro FIR
cutoff_frequency = 100  # Frecuencia de corte para la señal ECG
numtaps = 101  # Número de coeficientes del filtro
filtro_fir = firwin(numtaps, cutoff_frequency, pass_zero=True, fs=fs)  # Filtro pasabaja

# Aplicar el filtro FIR a la señal ECG
ecg_filtrada = lfilter(filtro_fir, 1.0, ecg_signal)

# Diagrama de polos y ceros
z, p, k = tf2zpk(filtro_fir, [1])
plt.figure(figsize=(6, 6))
plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
plt.title("Diagrama de polos y ceros del filtro FIR pasabaja")
plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
plt.grid(True)
plt.legend()
plt.show()

# Diagrama de Bode (magnitud y fase)
w, h = freqz(filtro_fir, 1, worN=2000)
plt.figure(figsize=(10, 6))

# Magnitud
plt.subplot(2, 1, 1)
plt.plot(w * fs / (2 * np.pi), 20 * np.log10(abs(h)))
plt.title("Respuesta en frecuencia del filtro FIR pasabaja")
plt.ylabel("Magnitud [dB]")
plt.grid(True)

# Fase
plt.subplot(2, 1, 2)
plt.plot(w * fs / (2 * np.pi), np.angle(h))
plt.ylabel("Fase [radianes]")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)

plt.show()


 -->



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
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/estadobasal1TFT.png" width="600" height="266"></p>
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
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150DOM.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Frecuencia 
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150FREC.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Transformada corta de Fourier
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150TFT.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Diagrama de Polos y Ceros
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150POLOS.png" width="600" height="266"></p>
</p
  
<p align="justify">
<p align="center"> Señal 150 BPM - Diagrama de Bode
<p align="center"><img src="/ISB/Laboratorios/Lab7 - Filtrado Señal/Josue Taipe/Imagenes/150BOLE.png" width="600" height="266"></p>
</p
<p align="justify">
  
### Justificación  <br>

El filtro FIR pasabaja fue elegido específicamente para asegurar que la señal ECG mantenga su integridad y claridad, eliminando eficientemente las interferencias y el ruido que podrían afectar el análisis clínico de la señal. <br>

1. Rango de frecuencias de interés para ECG: Las señales ECG tienen frecuencias significativas en el rango de 0.5 Hz a 100 Hz. Los componentes de alta frecuencia suelen ser ruido o artefactos que pueden distorsionar la interpretación de la señal. <br>

2. Eliminación de ruido de alta frecuencia: Un filtro pasabaja es ideal para este caso, ya que permite preservar las frecuencias bajas que son características de la señal ECG, mientras que elimina las componentes de alta frecuencia que no contienen información relevante para el análisis del ECG.<br>

3.Uso de la ventana de Hamming: Esta ventana es utilizada por su capacidad de minimizar las ondulaciones en la respuesta del filtro (ripple), ofreciendo una buena atenuación en la banda de parada sin comprometer significativamente la respuesta de la señal en la banda de paso.

























