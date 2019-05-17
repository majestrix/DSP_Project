import numpy as np
import soundfile as sf
import glob
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