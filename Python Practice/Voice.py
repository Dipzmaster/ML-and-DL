# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:50:58 2021

@author: HP
"""

import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")

voice_recorder(10, "record.wav")