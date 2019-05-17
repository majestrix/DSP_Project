import numpy as np
import soundfile as sf
import glob
import os
from scipy import spatial

def ZCR(signal):
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

def fileZCR(dir):
    files = glob.glob(dir)
    totalZCR = []
    for path in files:
        data ,fs = sf.read(path)
        signalZCR = ZCR(data)
        totalZCR.append(signalZCR)
    return np.mean(totalZCR,axis=0)

def findSimilarity(one,two):
    return 1 - spatial.distance.cosine(one,two)


def main():
    yes_path = os.path.dirname(__file__) + "/train/yes/*.wav"
    ZCR_yes = fileZCR(yes_path)
    no_path = os.path.dirname(__file__) + "/train/no/*.wav"
    ZCR_no = fileZCR(no_path)

    yes_test = glob.glob(os.path.dirname(__file__) + "/test/yes/*.wav")
    no_test = glob.glob(os.path.dirname(__file__) + "/test/no/*.wav")

    for file in yes_test+no_test:
        data,fs = sf.read(file)
        test = ZCR(data)
        yes_sim = findSimilarity(test,ZCR_yes)
        no_sim = findSimilarity(test,ZCR_no)
        ans = False
        if(yes_sim > no_sim):
            ans=True
        print("is %s a yes? %r" % (file.rsplit('\\')[-1],ans))

if __name__ == "__main__":
    main()