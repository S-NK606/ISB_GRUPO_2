import numpy as np
import pywt  # Paquete para la Transformada Wavelet
from sklearn.decomposition import FastICA, PCA
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch
from scipy.stats import kurtosis


# Función de sustracción de media para evitar desplazamientos no deseados
def mean_subtraction(data):
    return data - np.mean(data)

# Umbral mejorado basado en la amplitud máxima de los coeficientes
def improved_threshold_adaptive(coeff, max_coeff):
    lambd = 0.2 * max_coeff  # Ajuste en función de la amplitud del coeficiente
    return np.where(
        np.abs(coeff) >= lambd,
        np.sign(coeff) * (np.abs(coeff) - (2 * lambd / (1 + np.exp(lambd - np.abs(coeff))))),
        0
    )

# Función para el filtro wavelet multicapa optimizado
def wavelet_denoise_ecg(data, wavelet='db4', level=3):
    # Preprocesamiento: Sustracción de la media para centrar la señal
    data = mean_subtraction(data)
    
    # Decomposición wavelet de múltiples niveles
    coeffs = pywt.wavedec(data, wavelet, level=level)
    
    # Calcular el máximo coeficiente para ajuste adaptativo del umbral
    max_coeff = np.max([np.max(np.abs(c)) for c in coeffs[1:]])
    
    # Aplicar el umbral mejorado adaptativo a los coeficientes de detalle
    coeffs[1:] = [improved_threshold_adaptive(coeff, max_coeff) for coeff in coeffs[1:]]
    
    # Reconstrucción final de la señal
    denoised_signal = pywt.waverec(coeffs, wavelet)
    return denoised_signal


# Funciones de extracción de características
def maximum_fractal_length(signal):
    kmax = 4
    N = len(signal)
    lengths = np.zeros(kmax)
    for k in range(1, kmax + 1):
        lengths[k - 1] = np.sum(np.abs(signal[k:] - signal[:-k])) / (N - k)
    return np.mean(lengths)

def myopulse_percentage_rate(signal, threshold=100e-3):
    return np.sum(np.abs(signal) > threshold) / len(signal)

def v_order(signal, v=3):
    return np.mean(np.power(np.abs(signal), v)) ** (1 / v)

def willison_amplitude(signal, threshold=50e-3):
    return np.sum(np.abs(np.diff(signal)) > threshold)

def sample_entropy(signal, m=2, r=None):
    if r is None:
        r = 0.2 * np.std(signal)
    N = len(signal)
    def phi(m):
        x = np.array([signal[i:i + m] for i in range(N - m + 1)])
        C = np.sum([np.sum(np.all(np.abs(x - x[j]) <= r, axis=1) - 1) for j in range(len(x))]) / len(x)
        return C / (N - m + 1)
    return -np.log(phi(m + 1) / phi(m))

def hjorth2(signal):
    derivative = np.diff(signal)
    return np.var(derivative) / np.var(signal)

def kurt(signal):
    return kurtosis(signal)

def slope_sign_change(signal, threshold=None):
    if threshold is None:
        threshold = 0.03 * np.std(signal)
    diff1 = np.diff(signal)
    diff2 = np.diff(diff1)
    diff2 = np.append(diff2, 0)
    return np.sum(np.logical_and(diff1 > threshold, diff2 < -threshold))

# Función para calcular características en ventanas deslizantes
def calculate_features_in_windows(signal, window_size, step_size, fs):
    n_windows = (len(signal) - window_size) // step_size + 1
    features = {
        'MFL': [],
        'MYOP': [],
        'V-order': [],
        'WAMP': [],
        'SampEn': [],
        'Hjorth2': [],
        'Kurtosis': [],
        'SSC': []
    }
    
    for i in range(n_windows):
        start = i * step_size
        end = start + window_size
        window_signal = signal[start:end]
        
        features['MFL'].append(maximum_fractal_length(window_signal))
        features['MYOP'].append(myopulse_percentage_rate(window_signal))
        features['V-order'].append(v_order(window_signal))
        features['WAMP'].append(willison_amplitude(window_signal))
        features['SampEn'].append(sample_entropy(window_signal))
        features['Hjorth2'].append(hjorth2(window_signal))
        features['Kurtosis'].append(kurt(window_signal))
        features['SSC'].append(slope_sign_change(window_signal))
    
    return features, n_windows

# Función para plotear características contra el tiempo
def plot_features_against_time(features, time, feature_name):
    plt.figure()
    plt.plot(time, features, label=feature_name)
    plt.title(f"{feature_name} vs Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel(feature_name)
    plt.legend()
    plt.show()

# Función para RMS
def moving_rms(signal, window_size, fs):
    window = int(window_size * fs)
    return np.sqrt(np.convolve(signal**2, np.ones(window)/window, mode='same'))

# Función para plotear FFT
def plot_fft(signal, fs, title="FFT"):
    N = len(signal)
    fft_values = np.fft.fft(signal)
    fft_magnitude = np.abs(fft_values)[:N//2]
    fft_frequencies = np.fft.fftfreq(N, 1/fs)[:N//2]
    fft_magnitude_db = 20 * np.log10(fft_magnitude / np.max(fft_magnitude))
    
    plt.figure(figsize=(10, 4))
    plt.plot(fft_frequencies, fft_magnitude_db)
    plt.grid(True)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.title(title)
    plt.xlim([0, 200])
    plt.xticks(np.arange(0, 200, 10))
    plt.show()

# Parámetros de muestreo
Fs = 1000
Ts = 1 / Fs
window_size = int(0.2 * Fs)
step_size = int(0.05 * Fs)

# Lista de archivos a procesar
file_paths = [
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\files (1)\\bicep braquial leve.txt",
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\files (1)\\bicep braquial oposición fuerte.txt",
    "C:\\Users\\sofmi\\OneDrive\\Desktop\\10MO CICLO\\INTRO SEÑALES\\files (1)\\bicep braquial en reposo.txt",
]

nombres = ["Bicep con oposición leve", "Bicep con oposición fuerte", "Bicep en reposo"]

# Frecuencias de corte del filtro pasa banda y notch
lowcut = 10.0
highcut = 499.0
notch_freq = 60.0

# Procesar cada archivo
for idx, file_path in enumerate(file_paths):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_start = None
    for i, line in enumerate(lines):
        if 'EndOfHeader' in line:
            data_start = i + 1
            break
    if data_start is None:
        raise ValueError(f"No se encontró 'EndOfHeader' en el archivo {file_path}.")

    data_lines = lines[data_start:]
    data = np.array([list(map(float, line.strip().split('\t'))) for line in data_lines])
    signal1 = data[:, 5]

    plot_fft(signal1, Fs, title=f"FFT de Señal Original - {nombres[idx]}")

    try:
        signal_filtered_wavelet = wavelet_denoise_ecg(signal1, wavelet='db4', level=4)
    except ValueError as e:
        print(f"Error aplicando filtro wavelet: {e}")
        continue
    plot_fft(signal_filtered_wavelet, Fs, title=f"FFT de Señal Filtrada - {nombres[idx]}")

    signal_rectified = np.abs(signal_filtered_wavelet)

    # Calcular características en ventanas deslizantes
    features, n_windows = calculate_features_in_windows(signal_filtered_wavelet, window_size, step_size, Fs)


    # Potencia media
    mean_power = np.mean(signal_rectified**2)

    # RMS y promedio móvil
    rms_envelope = moving_rms(signal_rectified, 0.05, Fs)
    mvc = np.max(rms_envelope)
    rms_normalized = (rms_envelope / mvc) * 100
    
    # Vector de tiempo ajustado para las características
    time = np.arange(n_windows) * (step_size / Fs)
    time_signal = np.arange(len(signal1)) / Fs
    
    plt.figure(figsize=(10, 4))
    plt.plot(time_signal, signal1, label=f"Señal original - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal original EMG - {nombres[idx]}")
    plt.show()

    # Graficar señal filtrada
    plt.figure(figsize=(10, 4))
    plt.plot(time_signal, signal_filtered_wavelet, label=f"Señal filtrada - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal EMG filtrada (Wavelet) - {nombres[idx]}")
    plt.show()

    # Graficar señal rectificada
    plt.figure(figsize=(10, 4))
    plt.plot(time_signal, signal_rectified, label=f"Señal rectificada - {nombres[idx]}")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"Señal EMG rectificada - {nombres[idx]}")
    plt.show()

    # Graficar RMS y la señal normalizada
    plt.figure(figsize=(10, 4))
    plt.plot(time_signal, rms_envelope, label="RMS Envelope")
    plt.plot(time_signal, rms_normalized, label="RMS Normalized (MVC)")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(f"RMS y RMS Normalizado - {nombres[idx]}")
    plt.show()
    # Extracción de características
    mfl = maximum_fractal_length(signal_rectified)  # Maximum Fractal Length
    myop = myopulse_percentage_rate(signal_rectified)  # Myopulse Percentage Rate
    v_order_val = v_order(signal_rectified)  # V-order
    wamp = willison_amplitude(signal_rectified)  # Willison Amplitude
    sampen = sample_entropy(signal_rectified)  # Sample Entropy
    hjorth_param = hjorth2(signal_rectified)  # Hjorth Parameter
    kurt_val = kurt(signal_rectified)  # Kurtosis
    ssc = slope_sign_change(signal_rectified)  # Slope Sign Change


    # Adjust time array to match the number of windows
    time_windows = np.arange(n_windows) * (step_size / Fs)  # time for each window

    # Graficar cada característica en función del tiempo
    for feature_name, feature_values in features.items():
        plot_features_against_time(feature_values, time, feature_name)
