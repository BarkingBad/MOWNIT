using WAV
using Plots
using FFTW

snd, sampFreq = wavread("mownit.wav")
length, channels = size(snd)
duration = length/sampFreq
channel1 = snd[:,1]

timeArray = (0:(length-1)) / sampFreq
timeArray = timeArray * 1000

pl1 = plot(timeArray, channel1)
savefig("pl1.svg")
y=fft(channel1)
pl2 = sticks((abs.(fft(channel1))))
savefig("pl2.svg")
for (i,v) in enumerate(y)
    if abs.(v) <= 200
        if abs.(v) >= 120
            y[i] = y[i] - 120
        else
            y[i] = 0
        end
    end
end
k = ifft(y)
j = real(k)
pl3 = plot(timeArray, j)
savefig("pl3.svg")
wavwrite(j, sampFreq, "./output.wav")

