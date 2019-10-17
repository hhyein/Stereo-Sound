import wave, array

def make_stereo(input1, input2, output):
    wav1 = wave.open(input1)
    wav2 = wave.open(input2)
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav1.getparams()
    assert comptype == 'NONE'  # Compressed not supported yet
    array_type = {1:'B', 2: 'h', 4: 'l'}[sampwidth]
    left_channel = array.array(array_type, wav1.readframes(nframes))[::nchannels]
    right_channel = array.array(array_type, wav2.readframes(nframes))[::nchannels]
    
    wav1.close()
    wav2.close()
    
    stereo = 2 * left_channel
    stereo[1::2] = right_channel

    ofile = wave.open(output, 'w')
    ofile.setparams((2, sampwidth, framerate, nframes, comptype, compname))
    ofile.writeframes(stereo.tostring())
    ofile.close()

make_stereo('StarWars60.wav', 'PinkPanther60.wav', "test.wav")
