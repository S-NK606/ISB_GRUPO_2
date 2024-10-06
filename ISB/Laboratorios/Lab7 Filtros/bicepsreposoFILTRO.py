##filtro FIR 1  
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz, spectrogram, tf2zpk

# Leer los datos del archivo EMG
data = np.loadtxt(r'BICEPREPOSO.txt', skiprows=4)  # Ajusta este archivo
emg_signal = data[:, 5]  # Extraer la columna EMG (A1)
fs = 1000  # Frecuencia de muestreo en Hz (como especificado en el archivo)

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

