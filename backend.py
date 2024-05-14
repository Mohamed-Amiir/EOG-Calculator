from typing import Any
import random
import numpy as np
import main, Classification as CL



# get movements
def GetMovement(Model, TestSignals: list[np.ndarray], Direction: int):
    shift = (len(TestSignals) / 5) * Direction
    rand_picked_num = random.randint(0, 3)
    sample_index = rand_picked_num + shift
    TestSignal = TestSignals[int(sample_index)]
    prediction = Model.predict([TestSignal])
    print("prediction for " + GetClass(int(Direction)), " is  ", GetClass(int(prediction)))
    return prediction


def GetClass(ClassId: int) -> str:
    Classes = ["Blink","Down", "Left", "Right", "Up"]
    return Classes[ClassId]


# Model = CL.LoadModel('SVM')
# # load test signals
# TestSignels = main.Get_Prepared_Signals(1)

# move = GetMovement(Model, TestSignels, 4)
# print(move)
