from PIL import Image
import os

attr = \
    {
        "Sex?(M/F)": ["M","F"],
        "Eye Color?": ["brown","blue"],
        "Hair color?": ["dark","blonde"],
        "Shirt color?": ["white","blue","yellow","pink","red"],
        "Ethinicity?": ["white","black"],
        "Profession?": ["doctor","carpenter","student","cook","dancer","soccer player","police","gaming","none"]
    }
charInfo = [
            [1,"F", "dark", "brown", "white", "white", "doctor"],
            [2,"M", "dark", "blue", "blue", "white", "carpenter"],
            [3,"M", "blonde", "brown", "blue", "white", "none"],
            [4,"M", "blonde", "blue", "yellow", "white", "student"],
            [5,"F", "blonde", "blue", "pink", "white", "cook"],
            [6,"F", "blonde", "blue", "white", "white", "none"],
            [7,"F", "dark", "blue", "pink", "white", "dancer"],
            [8,"F", "dark", "brown", "red", "black", "none"],
            [9,"M", "dark", "brown", "red", "black", "soccer player"],
            [10,"M", "blonde", "blue", "blue", "white", "police"],
            [11,"M", "dark", "blue", "blue", "white", "gaming"],
            [12,"F", "blonde", "brown", "blue", "white", "none"]
            ]


def askQuestions():
    qs = attr.copy()
    sub = charInfo.copy()
    while sub.__len__() > 1:
        count = 1
        for q,a in qs.items():
            print(str(count) + '.'  + q)
            count = count+1
        print('Pick a question to answer!')
        qnum = input('>')
        qnum = int(qnum)-1
        foundQ = list(qs.keys())[qnum]

        for j in qs[foundQ]:
            toCompare = [y for x in sub for y in x]
            if j in toCompare:
                ans = input('>'+j.capitalize()+'?')
                if ans == 'Y' or ans == 'y':
                    if j in qs[foundQ]:
                        sub = [per for per in sub if j in per]
                        del qs[foundQ]
                        break

    print(sub)
    img = Image.open(os.path.dirname(__file__)+"/"+str(sub[0][0]) + '.jpg')
    img.show()



# img = mpimg.imread(sub[0][0] + '.jpg')
# imgplot = plt.imshow(img)
# plt.show()

askQuestions()
