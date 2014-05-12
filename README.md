#Report 

## Goal

Our main goal was to find noise on an ECG signal. 

## Team

* Luísa Fialho, 32103
* Ana Sousa, 31522
* Enrica Leto, 42561

## Process

We passed by the several steps:

### Step 1 - First signal recorded

In the first step we've recorded data.
We used the best signal extracted from bitalino. 

### Step 2 - Improved signal

We created an array for the time of the signal with the sampling frequency. 
Then we have done the subtraction of the ecg signal mean with itself, to reduce to zero the baseline of the signal.  

### Step 3 - Defining the signal processing stages

We created an array that values one (1) when there is noise (values above 400 mV). Otherwise, it gives zero(0).  

The image represents the ECG signal above and the Noise Detector bellow:

![graphs](https://github.com/luisafialho/ecg_noise_detector/blob/master/ECG_detector.jpg)


### Step 4 - The final outcome

#### Code


``` python

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
```

The complete code can be found on the github link:

[project code page](https://github.com/luisafialho/ecg_noise_detector/blob/master/ecg_noise_detector.py)


