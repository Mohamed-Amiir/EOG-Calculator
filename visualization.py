import matplotlib.pyplot as plt
import Preprocessing as pp
# Read the signal data from sag1h.txt
with open('class/right/sag1h.txt', 'r') as file:
    sag1h_data = [float(line.strip()) for line in file]

# Read the signal data from sag1v.txt
with open('class/right/sag1v.txt', 'r') as file:
    sag1v_data = [float(line.strip()) for line in file]

# Read the signal data from sol1v.txt
with open('class/left/sol1v.txt', 'r') as file:
    sol1v_data = [float(line.strip()) for line in file]

# Read the signal data from sol1h.txt
with open('class/left/sol1h.txt', 'r') as file:
    sol1h_data = [float(line.strip()) for line in file]

# Read the signal data from asagi1h.txt
with open('class/down/asagi1h.txt', 'r') as file:
    asagi1h_data = [float(line.strip()) for line in file]

# Read the signal data from asagi1v.txt
with open('class/down/asagi1v.txt', 'r') as file:
    asagi1v_data = [float(line.strip()) for line in file]

# Read the signal data from yukari1h.txt
with open('class/up/yukari1h.txt', 'r') as file:
    yukari1h_data = [float(line.strip()) for line in file]

# Read the signal data from yukari1v.txt
with open('class/up/yukari1v.txt', 'r') as file:
    yukari1v_data = [float(line.strip()) for line in file]



# Read the signal data from yukari1h.txt
with open('class/blink/kirp8h.txt', 'r') as file:
    ExampleH = [float(line.strip()) for line in file]

# Read the signal data from yukari1v.txt
with open('class/blink/kirp8h.txt', 'r') as file:
    ExampleV = [float(line.strip()) for line in file]


# Plot the h signal data
plt.subplot(2, 1, 1)
plt.title('Horizontal')
plt.plot(ExampleH)
plt.legend()

# Plot the v signal data
plt.subplot(2, 1, 2)
plt.title('Vertical')
plt.plot(ExampleV)
plt.legend()

plt.show()

# exH = pp.Butter_Bandpass_Filter([ExampleH],0.5,50,500,4)
# exV = pp.Butter_Bandpass_Filter([ExampleV],0.5,50,500,4)


# # Plot the h signal data
# plt.subplot(2, 1, 1)
# plt.title('Horizontal')
# plt.plot(exH)
# plt.legend()

# # Plot the v signal data
# plt.subplot(2, 1, 2)
# plt.title('Vertical')
# plt.plot(exV)
# plt.legend()

# plt.show()