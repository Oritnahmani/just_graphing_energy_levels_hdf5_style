import h5py
import matplotlib.pyplot as plt
import numpy as np


data = h5py.File("Spectrum_Results.h5")

DOS = data['nevanlinna']['dos']
freqs = data['nevanlinna']['freqs']
np_dos = np.array(DOS) 

dos=np.sum(np_dos, axis=(1,2))

freq = np.array(freqs)

plt.xlim([-0.5,0.5])
for i in range(len(dos[1,:])):
    plt.plot(freq*27.2113, dos[:,i])
plt.savefig('spectrum_beta.pdf')