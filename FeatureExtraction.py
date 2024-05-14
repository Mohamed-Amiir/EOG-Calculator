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



def raw_sample_features(eog_signals):
    extracted_features_array = []
    for eog_signal in eog_signals:
        # Baseline Drift: Calculate the mean of the signal
        baseline_drift = np.mean(eog_signal)
        
        # Amplitude of Eye Movements: Calculate the peak-to-peak amplitude
        amplitude = np.max(eog_signal) - np.min(eog_signal)
        
        # Duration of Eye Movements: Calculate the time duration of the signal
        duration = len(eog_signal)
        
        # Directional Information: Determine the direction of eye movements based on signal polarity
        direction = 1 if np.mean(eog_signal) > 0 else 0
        
        # Frequency Characteristics: Calculate the FFT of the signal to analyze frequency components
        fft_result = np.fft.fft(eog_signal)
        frequency_components = np.abs(fft_result)
        dominant_frequency = np.argmax(frequency_components)
        
        # Artifact Rejection: Check for signal quality based on standard deviation
        std_deviation = np.std(eog_signal)
        artifact_rejection = 1 if std_deviation < 0.1 else 0
        
        # Store the extracted features in a dictionary
        features = [
            baseline_drift,
            amplitude,
            duration,
            direction,
            dominant_frequency,
            artifact_rejection
        ]
        
        extracted_features_array.append(features)
    
    return extracted_features_array





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




