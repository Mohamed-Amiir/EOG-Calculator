# import main
import ReadingSignals as RS
import Preprocessing as Pre
# import FeatureExtraction as FE
# import Classification as Cls    
# import numpy as np
# import os
# import shutil
import matplotlib.pyplot as plt


path = "Dataset/Test/*"
Signals = RS.GetSignals(path)

concSignals = Pre.GetConcatenateSignals(Signals)

plt.plot(concSignals[5])
plt.title("Before Filtering and Resampling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

Filtered_Signals = Pre.Butter_Bandpass_Filter(concSignals, low_cutt_off=1, high_cutt_off=30, sampling_rate=176, order=2)


plt.plot(Filtered_Signals[5])
plt.title("after Filtering and Resampling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

Resampled_Signals = Pre.Resampling(Filtered_Signals, 50)

plt.plot(Resampled_Signals[5])
plt.title("after Filtering and Resampling")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()