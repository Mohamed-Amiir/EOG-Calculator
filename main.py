import Preprocessing as Pre
import ReadingSignals as RS
import Classification
import FeatureExtraction
import numpy as np
import matplotlib.pyplot as plt


from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.metrics import accuracy_score
# from matplotlib import pyplot as plt
def Get_Prepared_Signals(Signal_Type):
    if Signal_Type == 1:
        Path = "Dataset/Test/*"
    else:
        Path = "Dataset/Train/*"
    Signals = RS.GetSignals(Path)

    # -------------------------------> Preprocessing <---------------------------------------
    ConcSignals = Pre.GetConcatenateSignals(Signals)
    # # Plotting the first element of ConcSignals
    # plt.plot(ConcSignals[0])
    # plt.title("Before Filtering and Resampling")
    # plt.xlabel("Time")
    # plt.ylabel("Amplitude")
    # plt.show()

    # Filtering Signals
    Filtered_Signals = Pre.Butter_Bandpass_Filter \
        (ConcSignals, low_cutt_off=1, high_cutt_off=30, sampling_rate=176, order=2)

    # Resampling Signals
    Resampled_Signals = Pre.Resampling(Filtered_Signals, 50)
    # plt.plot(Resampled_Signals[0])
    # plt.title("After Filtering and Resampling")
    # plt.xlabel("Time")
    # plt.ylabel("Amplitude")
    # plt.show()    
    # -------------------------------> Feature Extraction <---------------------------------------
    # Wavelets
    DWT_Train_Signals = FeatureExtraction.wavelet_features(Resampled_Signals, wavelet='db1', level=2)

    # Time Domain Features

    Features = DWT_Train_Signals
    return Features

def getMovements(Signals):
    movementSignals = int(len(Signals) / 4)
    signal = []
    for i in range(0, 4):
        Movesig = []
        for index in range(i * 4, (i * 4) + movementSignals - 1):
            Movesig.append(Signals[index])
        signal.append(Movesig)
    return signal

def Train_SVM_Classifier(Train_Signals, Labels):
    # def Train_SVM_Classifier(Train_Signals, Labels, Test_Signals, TestLabels):
    # Create the SVM classifier
    SVM_Model = SVC(kernel='linear', C=15, random_state=42)
    
    # Train the classifier on the training set
    SVM_Model.fit(Train_Signals, Labels)
    Classification.SaveModel(SVM_Model,'SVM')
    scores = cross_val_score(SVM_Model, Train_Signals, Labels, cv=5)
    trainAcc = np.mean(scores)
    accuracy = SVM_Model.score(Train_Signals, Labels)

    Test_Signals = Get_Prepared_Signals(1)
    TestLabels = Classification.GetLabels(Test_Signals)

    y_pred = SVM_Model.predict(Test_Signals)
    # Evaluate the accuracy of the model

    TestAccuracy = accuracy_score(TestLabels, y_pred)
    print("\n")
    print("SVM Train Accuracy = %.2f%%" % round(accuracy * 100, 2))
    print("\n")
    print("SVM Test Accurcy = %.2f%%" % round(TestAccuracy * 100, 2))
    print("\n")

    # print("SVM Test Accuracy: {:.2f}%".format(accuracy * 100))
    return accuracy

Features = Get_Prepared_Signals(-1)
Signal_Labels = Classification.GetLabels(Features)

SVMTrain = Train_SVM_Classifier(Features, Signal_Labels)


# RFTrain = Classification.Train_RF_Classifier(Features, Signal_Labels)
# DTTrain = Classification.Train_DT_Classifier(Features, Signal_Labels)

# if SVMTrain > DTTrain:
#     print("SVM classifier is better with train accuracy : %.2f%%" % round(SVMTrain * 100, 2))
# elif SVMTrain == DTTrain:
#     print("Both has the same accuracy : %.2f%%" % round(DTTrain * 100, 2))
# else:
#     print("Decision Tree classifier is better with train accuracy: %.2f%%" % round(DTTrain * 100, 2))

