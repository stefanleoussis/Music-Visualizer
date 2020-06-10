import simpleaudio as sa

filename = 'file_example_WAV_10MG.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()