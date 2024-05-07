import numpy as np
import matplotlib.pyplot as plt

# Function to read data from file
def read_signal_from_file(filename):
    with open(filename, 'r') as file:
        signal = np.loadtxt(file)
    return signal

# Read signals from files
up_h_signal = read_signal_from_file('./Dataset/Train/Up/yukari1h.txt')
up_v_signal = read_signal_from_file('./Dataset/Train/Up/yukari1v.txt')
down_h_signal = read_signal_from_file('./Dataset/Train/Down/asagi1h.txt')
down_v_signal = read_signal_from_file("./Dataset/Train/Down/asagi1v.txt")
right_h_signal = read_signal_from_file('./Dataset/Train/Right/sag1h.txt')
right_v_signal = read_signal_from_file('./Dataset/Train/Right/sag1v.txt')
left_h_signal = read_signal_from_file('./Dataset/Train/Left/sol1h.txt')
left_v_signal = read_signal_from_file('./Dataset/Train/Left/sol1v.txt')
blink_h_signal = read_signal_from_file('./Dataset/Train/blink/kirp2h.txt')
blink_v_signal = read_signal_from_file('./Dataset/Train/blink/kirp2v.txt')

# Combine signals
combined_horizontal = up_h_signal + down_h_signal + right_h_signal + left_h_signal + blink_h_signal
combined_vertical = up_v_signal + down_v_signal + right_v_signal + left_v_signal + blink_v_signal

# Plotting
plt.figure(figsize=(12, 6))

# Plot horizontal signal
plt.subplot(2, 1, 1)
plt.plot(combined_horizontal, color='b')
plt.title('Combined Horizontal Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot vertical signal
plt.subplot(2, 1, 2)
plt.plot(combined_vertical, color='r')
plt.title('Combined Vertical Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
