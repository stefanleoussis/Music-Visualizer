#!/usr/bin/env python3

import struct
# import audioop
import pyaudio # from http://people.csail.mit.edu/hubert/pyaudio/
import time

def list_devices():
    # List all audio input devices
    p = pyaudio.PyAudio()
    i = 0
    n = p.get_device_count()
    while i < n:
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print(str(i)+'. '+dev['name'])
        i += 1

def arduino_soundlight(inputDeviceIdx):

    chunk    = 800 # Change if too fast/slow, never less than 1024

    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16,
                    channels = 1,
                    rate = 32000, #44100,
                    input = True,
                    frames_per_buffer = chunk,
                    input_device_index = inputDeviceIdx)

    print("Starting, use Ctrl+C to stop")

    avgRms = 0

    try:
        while True:
            data  = stream.read(chunk)
            data = struct.unpack('<800h', data)

            #This is where you should do something to display the audio data

    except KeyboardInterrupt:
        pass
    finally:
        print("\nStopping")
        stream.close()
        p.terminate()



if __name__ == '__main__':
    list_devices()
    inputDeviceIdx = input("Enter device # to stream from: ")
    arduino_soundlight(int(inputDeviceIdx))
