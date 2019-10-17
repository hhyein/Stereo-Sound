import numpy as np
import wave, array, struct


def volume(input_s, side):
    s = np.fromstring(input_s, np.int16)
    s_arr = list(range(0, len(s)))
    
    if(side == 'l'):
        for i in range(len(s)):
             s_arr[i] = np.sin(2 * i*((np.pi)/len(s)))*(0.5)
    else:
        for i in range(len(s)):
            s_arr[i] = np.sin(2 * i*((np.pi)/len(s)))*(-0.5)
            
    for i in range(len(s)):
        s[i] = s[i] * ((np.cos(2 * i*((np.pi)/len(s))) + 1.2) + s_arr[i])
            
    s = s.astype(np.int16)
    s = struct.pack('h'*len(s), (*s))
    return s


def make_mono(input1):
    wav = wave.open(input1)

    params = wav.getparams()
    nframes = params[3]
     
    s = wav.readframes(nframes)
    s = np.fromstring(s, np.int16)

    s_left = s[0::2]
    s_right = s[1::2]
    
    s_left = s_left.astype(np.int16)
    s_left = struct.pack('h'*len(s_left), (*s_left))
    s_right = s_right.astype(np.int16)
    s_right = struct.pack('h'*len(s_right), (*s_right))
    
    return (s_left, s_right, params)


def make_stereo(s_left, s_right, output, params):
    sampwidth = params[1]
    
    array_type = {1:'B', 2: 'h', 4: 'l'}[sampwidth]
    left_channel = array.array(array_type, s_left)
    right_channel = array.array(array_type, s_right)
    
    stereo = 2 * left_channel
    stereo[0::2] = left_channel
    stereo[1::2] = right_channel

    ofile = wave.open(output, 'w')
    ofile.setparams((2, params[1], params[2], params[3], params[4], params[5]))
    ofile.writeframes(stereo.tostring())
    ofile.close()


(s_left, s_right, params) = make_mono('sound.wav')
s_left = volume(s_left, 'r')
s_right = volume(s_right, 'l')
make_stereo(s_left, s_right, "resultest.wav", params)
