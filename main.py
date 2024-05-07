import Preprocessing as Pre
import ReadingSignals as RS
import Classification
import FeatureExtraction
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
def Get_Prepared_Signals(Signal_Type):
    if Signal_Type==1:
        Path ="Dataset/Test/*"
    else:
        Path = "Dataset/Train/*"
    Signals = RS.GetSignals(Path)
    # -------------------------------> Preprocessing <---------------------------------------
    ConcSignals = Pre.GetConcatenateSignals(Signals)

    # Filtering Signals
    Filtered_Signals = Pre.Butter_Bandpass_Filter\
        (ConcSignals, low_cutt_off=1, high_cutt_off=30, sampling_rate=176, order=2)

    # Resampling Signals
    Resampled_Signals = Pre.Resampling(Filtered_Signals, 50)

    # -------------------------------> Feature Extraction <---------------------------------------
    # Wavelets
    DWT_Train_Signals = FeatureExtraction.wavelet_features(Resampled_Signals, wavelet='db1', level=2)

    # Time Domain Features


    Features = DWT_Train_Signals
    return Features

def getMovements(Signals):
    movementSignals = int(len(Signals)/4)
    signal = []
    for i in range(0,4):
        Movesig = []
        for index in range(i*4,(i*4)+ movementSignals-1):
            Movesig.append(Signals[index])
        signal.append(Movesig)
    return signal



Features = Get_Prepared_Signals(-1)
Signal_Labels = Classification.GetLabels(Features)

SVMTrain = Classification.Train_SVM_Classifier(Features, Signal_Labels)
RFTrain = Classification.Train_RF_Classifier(Features, Signal_Labels)
DTTrain = Classification.Train_DT_Classifier(Features, Signal_Labels)

if SVMTrain > DTTrain:
    print("SVM classifier is better with train accuracy : %.2f%%" % round(SVMTrain*100, 2))
elif SVMTrain == DTTrain:
    print("Both has the same accuracy : %.2f%%" % round(DTTrain*100, 2))
else:
    print("Decision Tree classifier is better with train accuracy: %.2f%%" % round(DTTrain*100, 2))

