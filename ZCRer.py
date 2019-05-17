import numpy as np
import soundfile as sf
import glob
from scipy import spatial
import os
import pyaudio
import wave

class ZCRer:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
    
    def ZCR(self,signal):
        end = len(signal)
        end3 = int(end/3)
        s1 = signal[0:end3]
        s2 = signal[end3:2*end3]
        s3 = signal[2*end3:end]
        s = [s1,s2,s3]
        ZCR = []
        for i in s:
            ZCR.append(np.mean(
                        np.abs(
                            np.diff(
                                np.sign(i)
                                )
                            )
                        )/2)
        ZCR.append(np.sum(signal**2))
        return ZCR

    def fileZCR(self,dir):
        files = glob.glob(dir)
        totalZCR = []
        for path in files:
            data ,fs = sf.read(path)
            signalZCR = self.ZCR(data)
            totalZCR.append(signalZCR)
        return np.mean(totalZCR,axis=0)

    def findSimilarity(self,one,two):
        return 1 - spatial.distance.cosine(one,two)

    def recordAnswer(self):    
        stream = self.audio.open(format=pyaudio.paInt16, channels=1,
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

        waveFile = wave.open("mictest.wav", 'wb')
        waveFile.setnchannels(1)
        waveFile.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(44100)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        data,fs = sf.read(os.path.dirname(__file__)+"/mictest.wav")
        os.remove(os.path.dirname(__file__)+"/mictest.wav")
        ZCR_test = self.ZCR(data)

        return ZCR_test

    def recognizeAnswer(self,testData,trainPath):
        ZCR_yes = self.fileZCR(os.path.dirname(__file__)+"/"+trainPath+"yes/*.wav")
        ZCR_no = self.fileZCR(os.path.dirname(__file__)+"/"+trainPath+"no/*.wav")
        yes_sim = self.findSimilarity(testData,ZCR_yes)
        no_sim = self.findSimilarity(testData,ZCR_no)

        ans = False
        if(yes_sim > no_sim):
            ans=True
        print("yes" if ans else "no")
        return ans

    def close(self):
        self.audio = pyaudio.PyAudio()