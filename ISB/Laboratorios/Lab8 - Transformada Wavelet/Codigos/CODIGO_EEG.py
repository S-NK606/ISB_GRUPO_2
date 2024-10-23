import os
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.optimize import differential_evolution
from sklearn.metrics import mean_squared_error
from scipy.signal import butter, filtfilt

# Función para calcular RMSE
def rmse(signal1, signal2):
    return np.sqrt(mean_squared_error(signal1, signal2))

# Filtro pasabajas para eliminar componentes fuera de 0-100 Hz
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Función de fitness para optimización
def fitness_function(thresholds, original_signal, coeffs, wavelet, level):
    CA = coeffs[0]  # Coeficiente de aproximación (AC)
    CD = coeffs[1:]  # Coeficientes de detalle (DC)

    # Aplicar umbrales solo a los coeficientes de aproximación
    thresholded_CA = np.where(np.abs(CA) < thresholds[0], 0, CA)
    
    # Construir los nuevos coeficientes con el CA umbralizado y los DC sin cambios
    thresholded_coeffs = [thresholded_CA] + CD

    # Reconstruir la señal utilizando la transformada inversa de wavelet
    reconstructed_signal = pywt.waverec(thresholded_coeffs, wavelet)

    # Error RMSE entre la señal original y la señal reconstruida
    error_rmse = rmse(original_signal, reconstructed_signal)
    
    # Relación señal a ruido (SAR)
    sar = 10 * np.log10(np.std(original_signal) / np.std(original_signal - reconstructed_signal))

    return error_rmse / sar

# Aplicar DWT y obtener coeficientes
def apply_wavelet(signal, wavelet='db8', level=6):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    return coeffs

# Graficar los coeficientes de detalle y la aproximación
def plot_wavelet_coeffs(signal, coeffs, time, niveles, signal_name):
    plt.figure(figsize=(12, 10))

    # Graficar la señal original
    plt.subplot(4, 1, 1)
    plt.plot(time, signal)
    plt.title(f'Señal EEG Original - {signal_name}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')

    # Graficar coeficientes de detalle
    for i in range(1, 4):
        plt.subplot(4, 1, i + 1)
        plt.plot(coeffs[niveles - i + 1])
        plt.title(f'Detalle Nivel {i}')
        plt.ylabel('Amplitud')

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 10))
    for i in range(4, niveles + 1):
        plt.subplot(4, 1, i - 3)
        plt.plot(coeffs[niveles - i + 1])
        plt.title(f'Detalle Nivel {i}')
        plt.ylabel('Amplitud')

    # Graficar coeficiente de aproximación
    plt.subplot(4, 1, 4)
    plt.plot(coeffs[0])
    plt.title('Aproximación')
    plt.ylabel('Amplitud')

    plt.tight_layout()
    plt.show()

# Optimización usando Differential Evolution
def pso_optimize(signal, coeffs, wavelet='db8', level=6):
    # Solo optimizamos umbrales para el coeficiente de aproximación
    bounds = [(0, np.max(np.abs(coeffs[0])))]
    result = differential_evolution(fitness_function, bounds, args=(signal, coeffs, wavelet, level), strategy='best1bin', maxiter=100)
    return result.x, result.fun

# Graficar FFT
def plot_fft(signal, fs, title="FFT"):
    N = len(signal)
    fft_values = np.fft.fft(signal)
    fft_magnitude = np.abs(fft_values)[:N//2]
    fft_frequencies = np.fft.fftfreq(N, 1/fs)[:N//2]

    plt.figure(figsize=(10, 4))
    plt.plot(fft_frequencies, fft_magnitude)
    plt.grid(True)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.title(title)
    plt.show()

# Parámetros de muestreo
Fs = 1000  # Frecuencia de muestreo
duracion = 6  # 6 segundos
muestras = duracion * Fs
niveles = 6  # Nivel de descomposición de wavelet

# Lista de archivos a procesar
file_paths = [
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\SEÑALES A FILTRAR\\PARA EEG\\EstadodeReposoI.txt",
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\SEÑALES A FILTRAR\\PARA EEG\\EstadodeReposoII.txt",
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\SEÑALES A FILTRAR\\PARA EEG\\ojoabiertoojocerrado.txt",
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\SEÑALES A FILTRAR\\PARA EEG\\preguntasdificiles.txt",
]

nombres = ["Estado Reposo I", "Estado Reposo II", "Ojo Abierto/Cerrado", "Preguntas Difíciles"]

# Procesar cada archivo
for idx, file_path in enumerate(file_paths):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_start = next((i for i, line in enumerate(lines) if 'EndOfHeader' in line), None)
    if data_start is None:
        raise ValueError(f"No se encontró 'EndOfHeader' en el archivo {file_path}.")

    data_lines = lines[data_start + 1:]
    data = np.array([list(map(float, line.strip().split('\t'))) for line in data_lines])

    signal1 = data[:, -1]
    signal1 = signal1[:muestras]  # Tomar los primeros 6 segundos

    # Graficar la señal original
    time = np.arange(0, len(signal1)) / Fs
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal1, label=f"Señal original - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal EEG original - {nombres[idx]}")
    plt.show()

    # Aplicar DWT
    coeffs = apply_wavelet(signal1, level=niveles)

    # Graficar coeficientes de detalle y aproximación
    plot_wavelet_coeffs(signal1, coeffs, time, niveles, nombres[idx])

    # Optimización de umbrales para coeficientes de aproximación
    best_thresholds, _ = pso_optimize(signal1, coeffs)

    # Aplicar umbrales a los coeficientes de aproximación
    CA = coeffs[0]
    thresholded_CA = np.where(np.abs(CA) < best_thresholds[0], 0, CA)
    signal_filtered_wavelet = pywt.waverec([thresholded_CA] + coeffs[1:], 'db8')

    # Graficar la señal filtrada
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal_filtered_wavelet, label=f"Señal filtrada reconstruida - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal EEG filtrada (Wavelet) - {nombres[idx]}")
    plt.show()

    # Graficar la FFT de la señal filtrada
    plot_fft(signal_filtered_wavelet, Fs, title=f"FFT de Señal Filtrada - {nombres[idx]}")
