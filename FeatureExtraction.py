import csv
import pywt
import numpy as np
# import scipy.signal
# import matplotlib.pyplot as plt
from scipy.fftpack import fft


def wavelet_features(preprocessed_signals, wavelet, level):

    features = []
    for signal in preprocessed_signals:
        # Compute the DWT of the preprocessed signal
        coeffs = pywt.wavedec(signal, wavelet, level=level)
        res = coeffs[0]
        features.append(res)
    
    wavelets = 'wavelets_data.csv'
    # Save the reconstructed data
    with open(wavelets, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Freq', 'Data'])  # Write header
        writer.writerows(zip(range(len(features)), features))  # Write data row


    print("DWT Is Done \n")
    return features


def raw_sample_features(preprocessed_signals):
    # Baseline Drift: Calculate the mean of the signal
    baseline_drift = np.mean(preprocessed_signals)
    
    # Amplitude of Eye Movements: Calculate the peak-to-peak amplitude
    amplitude = np.max(preprocessed_signals) - np.min(preprocessed_signals)
    
    # Duration of Eye Movements: Calculate the time duration of the signal
    duration = len(preprocessed_signals)
    
    # Directional Information: Determine the direction of eye movements based on signal polarity
    direction = "Rightward" if np.mean(preprocessed_signals) > 0 else "Leftward"
    
    # Frequency Characteristics: Calculate the FFT of the signal to analyze frequency components
    fft_result = np.fft.fft(preprocessed_signals)
    frequency_components = np.abs(fft_result)
    dominant_frequency = np.argmax(frequency_components)
    
    # Artifact Rejection: Check for signal quality based on standard deviation
    std_deviation = np.std(preprocessed_signals)
    artifact_rejection = "Good" if std_deviation < 0.1 else "Poor"
    
    # Create a dictionary to store the extracted features
    features = {
        "Baseline Drift": baseline_drift,
        "Amplitude": amplitude,
        "Duration": duration,
        "Direction": direction,
        "Dominant Frequency": dominant_frequency,
        "Artifact Rejection": artifact_rejection
    }
    
    return features



def stat_features(preprocessed_signals):
    features = []
    for signal in preprocessed_signals:
        mean = np.mean(signal)
        maximum = np.max(signal)
        minimum = np.min(signal)
        std_dev = np.std(signal)
        signal_features = [mean, maximum, minimum, std_dev]
        features.append(signal_features)
    print("Time Domain Features Extraction Is Done \n")
    return features




