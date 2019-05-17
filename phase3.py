import ZCRer
import myTTS
from PIL import Image
import os
import random
import time
import matplotlib.pyplot as plt
import matplotlib.image as mimg

attr = \
    {
        "Are you a %s": ["Boy","Girl"],
        "Do you have %s eyes?": ["brown","blue"],
        "Do you have %s hair?": ["dark","blonde"],
        "Are you wearing a %s shirt?": ["white","blue","yellow","pink","red"],
        "Are you %?": ["white","black"],
        "Do you work as a %s": ["doctor","carpenter","student","cook","dancer","soccer player","police","gamer","none"]
    }
charInfo = [
            [1,"Girl", "dark", "brown", "white", "white", "doctor"],
            [2,"M", "dark", "blue", "blue", "white", "carpenter"],
            [3,"M", "blonde", "brown", "blue", "white", "none"],
            [4,"M", "blonde", "blue", "yellow", "white", "student"],
            [5,"Girl", "blonde", "blue", "pink", "white", "cook"],
            [6,"Girl", "blonde", "blue", "white", "white", "none"],
            [7,"Girl", "dark", "blue", "pink", "white", "dancer"],
            [8,"Girl", "dark", "brown", "red", "black", "none"],
            [9,"M", "dark", "brown", "red", "black", "soccer player"],
            [10,"M", "blonde", "blue", "blue", "white", "police"],
            [11,"M", "dark", "blue", "blue", "white", "gaming"],
            [12,"Girl", "blonde", "brown", "blue", "white", "none"]
            ]

def askQuestions():
    rec = ZCRer.ZCRer()
    tts = myTTS.myTTS()
    qs = attr.copy()
    sub = charInfo.copy()
    while sub.__len__() > 1:
        count = 0
        if(count == 0):
            rnd = 0
        else:
            rnd = random.randint(0,qs.items().__len__()-1)           
        foundQ = list(qs.keys())[rnd]
        count += 1

        for j in qs[foundQ]:
            toCompare = [y for x in sub for y in x]
            if j in toCompare:
                question = foundQ.replace("%s",j)
                print(question)
                tts.playText(question)
                ans = rec.recordAnswer()
                ans = rec.recognizeAnswer(ans,"test2/")
                if ans:
                    if j in qs[foundQ]:
                        sub = [per for per in sub if j in per]
                        del qs[foundQ]
                        break

    print(sub)
    tts.close()
    rec.close()
    img = mimg.imread(str(sub[0][0]) + ".jpg")
    imgplot = plt.imshow(img)
    plt.title("Guessed it!")
    plt.axis("off")
    plt.show()

askQuestions()

