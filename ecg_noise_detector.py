# -*- coding: utf-8 -*-
"""
Created on Mon May 12 12:19:38 2014

@author: UTILIZADOR
"""
# ECG NOISE DETECTOR 

from base64 import *
from numpy import *
from scipy import *
from pylab import *
from novainstrumentation import *
import novainstrumentation as ni

data = loadtxt("C:\\OpenSignals_3.0\\experiencia3.txt")

ecg = data[:,-1]

fs=1000.

t=arange(len(ecg))/fs
#Para retirar o DC e colocar o referencial na origem
media=mean(ecg)
ecg=ecg-media


subplot(2,1,1)
plot(t, ecg)
title('ECG')
xlabel('Time(ms)')
ylabel('ECG(mV)')
grid()


counter = ni.peaks(ecg,400)

noise=zeros(len(ecg))

noise[min(counter):max(counter)]=1
        
subplot(2,1,2)
plot(t,noise)
title('ECG NOISE DETECTOR')
xlabel('Time(ms)')
ylabel('Detection')
axis([0, 100, -1, 1.5])
grid()
plt.tight_layout() 
show()

savefig("ECG_detector.jpg")