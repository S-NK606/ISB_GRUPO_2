import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, filtfilt, stft, freqz, tf2zpk

# Función para filtro FIR con ventana Blackman
def fir_bandpass(lowcut, highcut, fs, numtaps=101):
    nyq = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyq
    high = highcut / nyq
    if low <= 0 or high >= 1:
        raise ValueError("Las frecuencias de corte deben estar en el rango (0, 1).")
    fir_coeff = firwin(numtaps, [low, high], pass_zero=False, window='blackman')
    return fir_coeff

# Aplicación del filtro FIR
def fir_bandpass_filter(data, lowcut, highcut, fs, numtaps=101):
    fir_coeff = fir_bandpass(lowcut, highcut, fs, numtaps)
    y = filtfilt(fir_coeff, 1.0, data)
    return y

# Función para graficar FFT
def plot_fft(signal, fs, title="FFT"):
    N = len(signal)
    fft_values = np.fft.fft(signal)
    fft_magnitude = np.abs(fft_values)[:N//2]
    fft_frequencies = np.fft.fftfreq(N, 1/fs)[:N//2]

    # Escala logarítmica en decibeles (opcional)
    fft_magnitude_db = 20 * np.log10(fft_magnitude / np.max(fft_magnitude))  # Magnitud en decibelios

    plt.figure(figsize=(10, 4))
    plt.plot(fft_frequencies, fft_magnitude_db)  # Gráfica en dB, puedes cambiar a fft_magnitude si prefieres magnitudes lineales
    plt.grid(True)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.title(title)
    # plt.xlim([0, 200])  # Ajusta el límite de frecuencia según sea necesario
    # plt.xticks(np.arange(0, 200, 10))
    plt.show()

# Parámetros de muestreo
Fs = 1000  # Frecuencia de muestreo
lowcut = 10.0
highcut = 490.0

# Definir duración en segundos (5 segundos)
duracion = 15
muestras = duracion * Fs  # Número de muestras correspondientes a 5 segundos

# Lista de archivos a procesar
file_paths = [
    "C:\\Users\\sofmi\\Downloads\\files\\gastrocnemioleve.txt",
    "C:\\Users\\sofmi\\Downloads\\files\\gastrocnemiofuerte.txt",
    "C:\\Users\\sofmi\\Downloads\\files\\gastrocnemioreposo.txt"
]

nombres = ["Gastronecmio con oposición leve", "Gastronecmio con oposición fuerte", "Gastronecmio en reposo"]

# Procesar cada archivo
for idx, file_path in enumerate(file_paths):
    # Leer archivo, ignorando las líneas de encabezado
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_start = None
    for i, line in enumerate(lines):
        if 'EndOfHeader' in line:
            data_start = i + 1
            break

    if data_start is None:
        raise ValueError(f"No se encontró 'EndOfHeader' en el archivo {file_path}.")

    # Convertir las líneas de datos a un array de NumPy
    data_lines = lines[data_start:]
    data = np.array([list(map(float, line.strip().split('\t'))) for line in data_lines])

    # Extraer la señal EMG (última columna en los datos)
    signal1 = data[:, 5]

    # Tomar los primeros 5 segundos de la señal (5000 muestras si Fs = 1000 Hz)
    signal1 = signal1[:muestras]
    # Graficar señal original
    time = np.arange(0, len(signal1)) / Fs  # Vector de tiempo

    plt.figure(figsize=(10, 4))
    plt.plot(time, signal1, label=f"Señal original - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal original EMG - {nombres[idx]}")
    plt.show()



    # Graficar la FFT de la señal original
    plot_fft(signal1, Fs, title=f"FFT de Señal Original - {nombres[idx]}")

    # Aplicar filtro pasa banda FIR con ventana Blackman
    try:
        signal_filtered = fir_bandpass_filter(signal1, lowcut, highcut, Fs)
    except ValueError as e:
        print(f"Error aplicando filtro pasa banda: {e}")
        continue

    # Gráfica en el dominio del tiempo (señal filtrada)
    time = np.arange(0, len(signal1)) / Fs
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal_filtered, label=f"Señal filtrada - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal EMG filtrada (Filtro Pasabanda FIR) - {nombres[idx]}")
    plt.show()

    # Graficar FFT de la señal filtrada
    plot_fft(signal_filtered, Fs, title=f"FFT de Señal Filtrada - {nombres[idx]}")

    # Transformada Corta de Fourier (STFT)
    f, t_stft, Zxx = stft(signal_filtered, Fs, nperseg=256)
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud')
    plt.title(f"Transformada Corta de Fourier (STFT) - {nombres[idx]}")
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.colorbar(label='Magnitud')
    plt.show()


    # Diagrama de polos y ceros del filtro
    fir_coeff = fir_bandpass(lowcut, highcut, Fs)
    z, p, k = tf2zpk(fir_coeff, 1)
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(z), np.imag(z), s=50, marker='o', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), s=50, marker='x', label='Polos')
    plt.title('Diagrama de Polos y Ceros')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Diagrama de Bode (magnitud y fase)
    w, h = freqz(fir_coeff, worN=8000)
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(0.5 * Fs * w / np.pi, 20 * np.log10(np.abs(h)))
    plt.title('Diagrama de Bode - Magnitud y Fase')
    plt.ylabel('Magnitud [dB]')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(0.5 * Fs * w / np.pi, np.angle(h))
    plt.ylabel('Fase [radianes]')
    plt.xlabel('Frecuencia [Hz]')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

