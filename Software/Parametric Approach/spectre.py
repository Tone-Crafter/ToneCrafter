# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:48:50 2021

@author: user
"""

import numpy as np

import matplotlib.pyplot as plt

import librosa
import librosa.display

from scipy import signal




input_file = 'maniac.wav'
output_file = 'G53-41101-1111-00002.wav'

x, sr = librosa.load('Bohemian Rhapsody.wav',offset=7, duration=0.5)
#x, sr = librosa.load('G53-58308-1111-00035.wav',offset=0.5, duration=0.5)

y=x


    
fs = sr  # Sample frequency (Hz)






Notestriees=[[32.70,  65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01,  8372.02 ],
             [34.65,  69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92,  8869.84 ],
             [36.71,  73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64,  9397.28 ],
             [38.89,  77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03,  9956.06 ],
             [41.20,  82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02, 5274.04, 10548.08 ],
             [43.65,  87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65, 11175.30 ],
             [46.25,  92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91, 11839.82 ],
             [49.00,  98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93, 12543.86 ],
             [51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88, 13289.76 ],
             [55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00, 14080.00 ],
             [58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62, 14917.24 ],
             [61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13, 15804.26 ]]

Notes=[32.70,  65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01,  8372.02 ,
       34.65,  69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92,  8869.84 ,
       36.71,  73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64,  9397.28 ,
       38.89,  77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03,  9956.06 ,
       41.20,  82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02, 5274.04, 10548.08 ,
       43.65,  87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65, 11175.30 ,
       46.25,  92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91, 11839.82 ,
       49.00,  98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93, 12543.86 ,
       51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88, 13289.76 ,
       55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00, 14080.00 ,
       58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62, 14917.24 ,
       61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13, 15804.26 ]


Notesecrites=["Do0","Do#0", "Ré0", "Ré#0", "Mi0", "Fa0", "Fa#0", "Sol#0", "La0", "La#0", "Si0",
              "Do1","Do#1", "Ré1", "Ré#1", "Mi1", "Fa1", "Fa#1", "Sol#1", "La1", "La#1", "Si1",
              "Do2","Do#2", "Ré2", "Ré#2", "Mi2", "Fa2", "Fa#2", "Sol#2", "La2", "La#2", "Si2",
              "Do3","Do#3", "Ré3", "Ré#3", "Mi3", "Fa3", "Fa#3", "Sol#3", "La3", "La#3", "Si3",
              "Do4","Do#4", "Ré4", "Ré#4", "Mi4", "Fa4", "Fa#4", "Sol#4", "La4", "La#4", "Si4",
              "Do5","Do#5", "Ré5", "Ré#5", "Mi5", "Fa5", "Fa#5", "Sol#5", "La5", "La#5", "Si5",
              "Do6","Do#6", "Ré6", "Ré#6", "Mi6", "Fa6", "Fa#6", "Sol6#", "La6", "La#6", "Si6",
              "Do7","Do#7", "Ré7", "Ré#7", "Mi7", "Fa7", "Fa#7", "Sol#7", "La7", "La#7", "Si7",
              "Do8","Do#8", "Ré8", "Ré#8", "Mi8", "Fa8", "Fa#8", "Sol#8", "La8", "La#8", "Si8",
              "Do9","Do#9", "Ré9", "Ré#9", "Mi9", "Fa9", "Fa#9", "Sol#9", "La9", "La#9", "Si9",
              "Do10","Do#10", "Ré10", "Ré#10", "Mi10", "Fa10", "Fa#10", "Sol#10", "La10", "La#10", "Si10",
              "Do11","Do#11", "Ré11", "Ré#11", "Mi11", "Fa11", "Fa#11", "Sol#11", "La11", "La#11", "Si11",
              "Do12","Do#12", "Ré12", "Ré#12", "Mi12", "Fa12", "Fa#12", "Sol#12", "La12", "La#12", "Si12"]

Note=[]
for i in range(9):
    for j in range(12):
        Note.append(Notestriees[j][i])

L=[]
for i in range (len(Notes)-1):
    a=np.sqrt(Note[i]*Note[i+1])
    L.append(a)
    
ro=2**14
n_fft=ro
  # Frequency to be removed from signal (Hz)

Q = 10  # Quality factor



for i in range(len(L)):
    
    b, a = signal.iirnotch(L[i]*2/fs, Q, fs)
    zi =signal.lfilter_zi(b, a)
    z = signal.filtfilt(b, a, x)
    x=z

hop_length = 256

fig, ax = plt.subplots()
D = librosa.amplitude_to_db(np.abs(librosa.stft(x,n_fft=ro,hop_length=hop_length)), ref=np.max)

img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=sr, hop_length=hop_length)

librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length,
                         x_axis='time' )

ax.set_title('Log-frequency power spectrogram')
ax.label_outer()

plt.colorbar(img, format="%+2.f dB")

fig, ax = plt.subplots()
D = librosa.amplitude_to_db(np.abs(librosa.stft(y,n_fft=ro,hop_length=hop_length)), ref=np.max)

img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                               sr=sr, hop_length=hop_length)

librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length,
                         x_axis='time' )

ax.set_title('Log-frequency power spectrogram')
ax.label_outer()

plt.colorbar(img, format="%+2.f dB")





#fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
#D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y,n_fft=ro,hop_length=hop_length)), ref=np.max)
#
#img = librosa.display.specshow(D2, y_axis='linear', x_axis='time',
#                               sr=sr, ax=ax[0],  hop_length=hop_length)
#ax[0].set(title='Linear-frequency power spectrogram')
#ax[0].label_outer()
#
#hop_length = 256
#D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=ro,  hop_length=hop_length)),
#                            ref=np.max)
#librosa.display.specshow(D2, y_axis='log', sr=sr, hop_length=hop_length,
#                         x_axis='time', ax=ax[1])
#ax[1].set(title='Log-frequency power spectrogram')
#ax[1].label_outer()
#fig.colorbar(img, ax=ax, format="%+2.f dB")




#D4 = np.abs(librosa.stft(x))
#image_max = ndi.maximum_filter(D, size=1, mode='constant')
#
## Comparison between image_max and im to find the coordinates of local maxima
#coordinates = peak_local_max(D, min_distance=8)
#
## display results
#fig, axes = plt.subplots(1, 3, figsize=(8, 8), sharex=True, sharey=True)
#ax = axes.ravel()
#ax[0].imshow(D, cmap=plt.cm.gray)
#ax[0].axis('off')
#ax[0].set_title('Original')
#
#ax[1].imshow(image_max, cmap=plt.cm.gray)
#ax[1].axis('off')
#ax[1].set_title('Maximum filter')
#
#ax[2].imshow(D, cmap=plt.cm.gray)
#ax[2].autoscale(False)
#ax[2].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
#ax[2].axis('off')
#ax[2].set_title('Peak local max')
#
#fig.tight_layout()
#
#plt.show()
#
#
#plt.plot(coordinates[:, 1], coordinates[:, 0], 'r.')
M=D.tolist()

K=[]
for i in range(int(len(M)/2)):
    K.append(2*i*fs/ro)
Mean=[]
M2=[]

for i in range (len(M)-24):
    M2.append(M[i+23])

for i in range (len(M2)):
    Mean.append(np.mean(M2[i]))
    
a=np.max(Mean)
Meanrangée=sorted(Mean)

tab=np.arange(0, 1 + n_fft / 2) * fs / n_fft
liste=tab.tolist()

Freq=[]


n= len(Meanrangée)
for i in range (10):
    b=Mean.index(Meanrangée[n-i-1])
    Freq.append(((b+24)*fs/ro))
    
FreqNorm=[]



for i in range (len(Freq)):
    a=Freq[i]
    j=0
    b=Note[j]
    c=Note[j+1]
    while a>np.sqrt(b*c):
        j=j+1
        b=Note[j]
        c=Note[j+1]
        
    c=Note[j]
    FreqNorm.append(c)
print(FreqNorm)
print(Freq)

a=min(FreqNorm)
b=Note.index(a)
print(b)
print(Notesecrites[b-3])






