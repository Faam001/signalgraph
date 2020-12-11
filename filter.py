#Dicek dulu apabila venv sudah aktif untuk memakai lib 
#gunakan source ../sig/bin/activate

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


S = 50000
T = 1/S
t = 0.1
n = S*t
f = [120,460,9610,19210]
print('the sinusoidals frequencies are: ',f)
omg = [2*np.pi*f[0], 2*np.pi*f[1], 2*np.pi*f[2], 2*np.pi*f[3]]
time = np.arange(n)*T

signals = [np.sin(omg[0]*time), np.sin(omg[1]*time), np.sin(omg[2]*time),
np.sin(omg[3]*time)]

signal = signals[0] + signals[1] + signals[2] + signals[3]


Y = sp.fft.fft(signal)
F = np.linspace(0,S, len(Y))

fig, ax = plt.subplots(2)
ax[0].plot(time, signal)
ax[0].set_title("signal combination")
ax[1].plot(F, np.abs(Y)/len(Y))
ax[1].set_title("FFT")
plt.show()


Flcut = 3000
Fhcut = 15000

#lowpass filter
print('this is the lowpass filter result')
H1 = (F<Flcut) + (F>S-Flcut)
Z1 = Y*H1
z1 = np.real(np.fft.ifft(Z1))

fig, axlow = plt.subplots(2)
axlow[0].plot(F,H1)
axlow[0].set_title("lowpass")
axlow[1].plot(time,z1)
axlow[1].set_title("lowpass result")
plt.show()

#highpass filter
print('this is the highpass filter result')
H2 = (F>Fhcut)&(F<S-Fhcut)
Z2 = Y*H2
z2 = np.real(np.fft.ifft(Z2))

fig, axhigh = plt.subplots(2)
axhigh[0].plot(F,H2)
axhigh[0].set_title("highpass")
axhigh[1].plot(time,z2)
axhigh[1].set_title("highpass result")
plt.show()

#bandpass filter
print('this is the bandpass filter result')
H3 = (F>Flcut)&(F<Fhcut)+(F>S-Fhcut)&(F<S-Flcut)
Z3 = Y*H3
z3 = np.real(np.fft.ifft(Z3))

fig, axbp = plt.subplots(2)
axbp[0].plot(F,H3)
axbp[0].set_title("bandpass")
axbp[1].plot(time,z3)
axbp[1].set_title("bandpass result")
plt.show()

#bandstop filter
print('this is the bandstop filter result')
H4 = (F<Flcut)+(F>Fhcut)&(F<S-Fhcut)+(F>S-Flcut)
Z4 = Y*H4
z4 = np.real(np.fft.ifft(Z4))

fig, axbs = plt.subplots(2)
axbs[0].plot(F,H4)
axbs[0].set_title("bandstop")
axbs[1].plot(time,z4)
axbs[1].set_title("bandstop result")
plt.show()
