
---

# Simulation of Sampling Theorem

## Aim:
To study:
- a) **Scilab Simulation** of Sampling Theorem
- b) **Python Simulation** of Sampling Theorem

## Software Required:
- **Scilab** / **Python**

## Theory:

The **Sampling Theorem**, also known as the **Nyquist-Shannon Sampling Theorem**, is fundamental in digital signal processing. It establishes the conditions under which a continuous-time signal can be perfectly represented and reconstructed from its samples. The theorem states that a band-limited signal (a signal with no frequencies higher than a maximum frequency \( f_{max} \)) can be completely recovered if it is sampled at a rate greater than twice the maximum frequency, i.e., the **Nyquist rate** \( f_s > 2 f_{max} \).

This ensures no information loss during sampling and prevents **aliasing**, where higher frequencies could be misinterpreted as lower frequencies, leading to distortion. The original signal can be reconstructed using the sinc interpolation formula. In practice, an anti-aliasing filter is applied before sampling to ensure the signal is band-limited, and the sampled values are quantized to discrete levels for digital representation. The Sampling Theorem is essential in various fields, including **digital audio**, **image processing**, and **telecommunications**, ensuring accurate conversion and preservation of continuous signals in digital form.

---

## Program (a): **Scilab Program Structure for Sampling Theorem**

```scilab
// Step 1: Generate a continuous-time signal
clf; // Clear the current figure
t = ...; // Time vector
f = ...; // Frequency
x = ...; // Continuous-time signal

// Plot the continuous-time signal
subplot(3,1,1);
plot(t, x);
title('Continuous-time Signal');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Continuous-time Signal with freq ... Hz');

// Step 2: Sample the signal at different sampling rates
fs1 = ...; // Sampling frequency
ts1 = ...; // Sampling times
xs1 = ...; // Sampled signal

// Repeat for fs2, fs3

// Plot the sampled signals
subplot(3,1,2);
plot(t, x, 'b'); // Original continuous-time signal
plot2d(ts1, xs1, style=-4, rect=[0, -1.5, 1, 1.5]); // Sampled signal at fs1

// Repeat for fs2, fs3
title('Sampled Signals');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Continuous-time', 'Sampled at ... Hz', 'Sampled at ... Hz', 'Sampled at ... Hz');

// Step 3: Reconstruct the signal from samples using interpolation
xr1 = interp1(ts1, xs1, t, 'linear'); // Reconstructed signal from fs1 samples

// Repeat for xr2, xr3

// Plot the reconstructed signals
subplot(3,1,3);
plot(t, x, 'b'); // Original continuous-time signal
plot2d(t, xr1, style=2, rect=[0, -1.5, 1, 1.5]); // Reconstructed signal from fs1 samples

// Repeat for xr2, xr3
title('Reconstructed Signals');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Continuous-time', 'Reconstructed from ... Hz samples', 'Reconstructed from ... Hz samples', 'Reconstructed from ... Hz samples');
```

###  Output:

![image](https://github.com/user-attachments/assets/e0012ab8-0bb1-4f37-861d-ed3368bf17da)

---

## Program (b): **Python Program Structure for Sampling Theorem**

```python
# Step 1: Generate a continuous-time signal
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, 0.001)  # Time vector
f = 5  # Frequency
x = np.sin(2 * np.pi * f * t)

# Plot the continuous-time signal
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Continuous-time Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend(['Continuous-time Signal with freq 5Hz'])

# Step 2: Sample the signal at different sampling rates
fs1 = 20
fs2 = 10
fs3 = 6
ts1 = np.arange(0, 1, 1/fs1)
ts2 = np.arange(0, 1, 1/fs2)
ts3 = np.arange(0, 1, 1/fs3)
xs1 = np.sin(2 * np.pi * f * ts1)
xs2 = np.sin(2 * np.pi * f * ts2)
xs3 = np.sin(2 * np.pi * f * ts3)

# Plot the sampled signals
plt.subplot(3, 1, 2)
plt.plot(t, x, 'b')  # Original continuous-time signal
plt.stem(ts1, xs1, 'r', label="Sampled at 20 Hz", basefmt=" ", linefmt='r-', markerfmt='ro')
plt.stem(ts2, xs2, 'g', label="Sampled at 10 Hz", basefmt=" ", linefmt='g-', markerfmt='go')
plt.stem(ts3, xs3, 'purple', label="Sampled at 6 Hz", basefmt=" ", linefmt='purple-', markerfmt='po')
plt.title('Sampled Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Step 3: Reconstruct the signal from samples using interpolation
from scipy.interpolate import interp1d

reconstruction1 = interp1d(ts1, xs1, kind='linear', fill_value="extrapolate")
reconstruction2 = interp1d(ts2, xs2, kind='linear', fill_value="extrapolate")
reconstruction3 = interp1d(ts3, xs3, kind='linear', fill_value="extrapolate")

xr1 = reconstruction1(t)
xr2 = reconstruction2(t)
xr3 = reconstruction3(t)

# Plot the reconstructed signals
plt.subplot(3, 1, 3)
plt.plot(t, x, 'b')  # Original continuous-time signal
plt.plot(t, xr1, 'r', label="Reconstructed from 20 Hz samples")
plt.plot(t, xr2, 'g', label="Reconstructed from 10 Hz samples")
plt.plot(t, xr3, 'purple', label="Reconstructed from 6 Hz samples")
plt.title('Reconstructed Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
```

###  Output:

The Python program generates three subplots:

![image](https://github.com/user-attachments/assets/00ae5e46-18f4-4061-8b52-0961b784b11b)

 **Continuous-time signal**.

![image](https://github.com/user-attachments/assets/4e8c9ac3-cd7e-4395-8b62-d706e8bb608d)

 **Sampled signals** at different sampling frequencies.

![image](https://github.com/user-attachments/assets/4b2de6b1-d7b1-45d8-b750-8c28dab2a8b8)

**Reconstructed signals** from the sampled signals.

---

## Conclusion:

The **Sampling Theorem** ensures that a continuous-time signal can be completely reconstructed from its discrete samples if the sampling rate is greater than twice the maximum frequency of the signal (Nyquist rate). By simulating the theorem in both Scilab and Python, we can observe how varying the sampling rate affects the quality of the sampled and reconstructed signals. 

---

