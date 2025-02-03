// Step 1: Generate a continuous-time signal
ClearFigure
t = 0 to 1 with step size 0.001
f = 5
x = sin(2 * pi * f * t)
// Plot the continuous-time signal
Create first subplot
Plot t vs x
Add title 'Continuous-time Signal'
Add xlabel 'Time (s)'
Add ylabel 'Amplitude'
Add legend 'Continuous-time Signal with freq 5Hz'
// Step 2: Sample the signal at different sampling rates
fs1 = 20
fs2 = 10
fs3 = 6
ts1 = 0 to 1 with step size 1/fs1
ts2 = 0 to 1 with step size 1/fs2
ts3 = 0 to 1 with step size 1/fs3
xs1 = sin(2 * pi * f * ts1)
xs2 = sin(2 * pi * f * ts2)
xs3 = sin(2 * pi * f * ts3)
// Plot the sampled signals
Create second subplot
Plot t vs x in blue
Plot ts1 vs xs1 in red with style -4
Plot ts2 vs xs2 in green with style -5
Plot ts3 vs xs3 in purple with style -6
Add title 'Sampled Signals'
15
Add xlabel 'Time (s)'
Add ylabel 'Amplitude'
Add legend 'Continuous-time', 'Sampled at 20 Hz', 'Sampled at 10 Hz', 'Sampled at 6 Hz'
// Step 3: Reconstruct the signal from samples using interpolation
xr1 = interpolate ts1, xs1 to t using linear
xr2 = interpolate ts2, xs2 to t using linear
xr3 = interpolate ts3, xs3 to t using linear
// Plot the reconstructed signals
Create third subplot
Plot t vs x in blue
Plot t vs xr1 in red with style 2
Plot t vs xr2 in green with style 3
Plot t vs xr3 in purple with style 4
Add title 'Reconstructed Signals'
Add xlabel 'Time (s)'
Add ylabel 'Amplitude'
Add legend 'Continuous-time', 'Reconstructed from 20 Hz samples', 'Reconstructed from 10 Hz samples', 
'Reconstructed from 6 Hz samples
