from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist
import pandas as pd
from matplotlib.pyplot import figure
import numpy as np
figure(figsize=(7, 7), dpi=100)
df = pd.read_csv('eis.txt', delimiter='\t')
frequencies = df['Frequency']
Zre = df['Zre']
Zim = -df['Zim']
Z = np.vectorize(complex)(Zre, Zim)
plt.plot(np.real(Z), -np.imag(Z),':')



circuit = 'L0-R1-p(R2,CPE0)-p(R3,CPE1)-W0'
initial_guess = [1.3e-8, 3.8e-4,5.9e-5, 7.7e1,8e-1,2.9e-4,2.4e5,1,2.8e-5]
circuit = CustomCircuit(circuit, initial_guess=initial_guess)
circuit.fit(frequencies, Z)
Z_fit = circuit.predict(frequencies)

plt.plot(np.real(Z_fit), -np.imag(Z_fit),':')
print(circuit)

plt.legend(['Data', 'Fit'])
plt.show()