import numpy as np
import struct

wav = wave.open("StarWars60.wav")
p = wav.getparams()
f = p[3]
s = wav.readframes(f)
wav.close()

s = np.fromstring(s, np.int16)
for i in range(len(s)):
    s[i] = s[i] / (np.sin(i/10000) + 1.8)
s = s.astype(np.int16)
s = struct.pack('h'*len(s), (*s))

w = wave.open("result.wav", "wb")
w.setparams(p)
w.writeframes(s)
w.close()
