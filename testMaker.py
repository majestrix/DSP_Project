import ZCRer as z
import os
import myTTS
import pyaudio
import wave
import struct
import time

# tts = myTTS.myTTS()
# tts.playText("Hello my name is amjad the boss")
# tts.close()

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1,
                    rate=44100,input=True,
                    frames_per_buffer=1024)
for i in range(2,3):
    print("Recording...")
    frames=[]
    animation="||||||||||///////////----------\\\\\\\\\\\\\\\\\\"
    idx=0
    for t in range(0,int(44100 / 1024 * 2)):
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        data = stream.read(1024)
        frames.append(data)
    print("Finished!")
    waveFile = wave.open(os.path.dirname(__file__)+"/test2/yes/yes"+str(i)+".wav", 'wb')
    waveFile.setnchannels(1)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(44100)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    time.sleep(2)

# for i in range(0,len(frames))
stream.stop_stream()
stream.close()
audio.terminate()
