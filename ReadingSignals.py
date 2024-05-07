import numpy as np
import glob

def ConvertLines2List (path):
    signal = open(path,'r')
    SignalLines = signal.readlines()
    Amplitudes = []
    for i in range(len(SignalLines) - 1):
        l = SignalLines[i + 1]
        Amplitudes.append(int(l))
    return Amplitudes


def GetSignals(path):
    TrainData = glob.glob(path)
    print("Train data extracted from GLOB:\n",TrainData)
    Signals = []
    for Label in TrainData:
        SignalsPath=glob.glob(Label+"/*")
        for SignalPath in SignalsPath :
            Signals.append(ConvertLines2List(SignalPath))
    return Signals