import ZCRer as z
import os
import myTTS
import pyaudio
import wave
import struct
import numpy
import soundfile as sf

# tts = myTTS.myTTS()
# tts.playText("Hello my name is amjad the boss")
# tts.close()

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1,
                    rate=44100,input=True,
                    frames_per_buffer=1024)
print("Recording...")
frames=[]
animation="||||||||||///////////----------\\\\\\\\\\\\\\\\\\"
idx=0
for i in range(0,int(44100 / 1024 * 2)):
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    data = stream.read(1024)
    frames.append(data)
print("Finished!")

# for i in range(0,len(frames))
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open("mictest.wav", 'wb')
waveFile.setnchannels(1)
waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(44100)
waveFile.writeframes(b''.join(frames))
waveFile.close()

data,fs = sf.read(os.path.dirname(__file__)+"/mictest.wav")
# data,fs = sf.read("mictest.wav")
ZCR_test = z.ZCR(data)
ZCR_yes = z.fileZCR(os.path.dirname(__file__)+"/test2/yes/*.wav")
ZCR_no = z.fileZCR(os.path.dirname(__file__)+"/test2/no/*.wav")

yes_sim = z.findSimilarity(ZCR_test,ZCR_yes)
no_sim = z.findSimilarity(ZCR_test,ZCR_no)

ans = False
if(yes_sim > no_sim):
    ans=True
print(ans)
print(yes_sim,no_sim)
os.remove("mictest.wav")