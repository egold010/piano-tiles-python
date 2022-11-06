import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
time.sleep(3)

#black color: 1,1,1
#blue color: 54,159,198
#pos1: 948,632
#pos2: 1074, 632
#pos3: 1196, 632
#pos4: 1322, 632

posList = [(948, 632), (1074, 632), (1196, 632), (1322, 632)]
cdList = [0, 0, 0, 0]

for i in range(len(posList)):
    if pyautogui.pixelMatchesColor(posList[i][0], posList[i][1], (54, 159, 198)):
        pyautogui.click(posList[i][0], posList[i][1])
while True:
    im = pyautogui.screenshot()

    #column 1
    if sum(im.getpixel((948, 632))) < 100:
        if not cdList[0]:
            pyautogui.click(948, 932)
            cdList[0] = 1
    else:
        cdList[0] = 0

    # column 2
    if sum(im.getpixel((1074, 632))) < 100:
        if not cdList[1]:
            pyautogui.click(1074, 932)
            cdList[1] = 1
    else:
        cdList[1] = 0

    # column 3
    if sum(im.getpixel((1196, 632))) < 100:
        if not cdList[2]:
            pyautogui.click(1196, 932)
            cdList[2] = 1
    else:
        cdList[2] = 0

    # column 4
    if sum(im.getpixel((1322, 632))) < 100:
        if not cdList[3]:
            pyautogui.click(1322, 932)
            cdList[3] = 1
    else:
        cdList[3] = 0