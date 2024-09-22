import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

# SETTING FOR CAMERA
cap = cv2.VideoCapture(0)

# SETTING FOR RESOLUTION
cap.set(3, 1280)
cap.set(4, 720)

# SETTING OF DETECTION CONFIDENCE OF 0.8 AND MAXIMUM 2 HANDS
detector = HandDetector(detectionCon=0.8, maxHands=2)

keys = [["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","X","C","V","B","N","M",",",".","/"]]
finalText = ""

keyboard = Controller()

def drawALL(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

class Button():
    def __init__(self, pos, text, size=[80, 80]):
        self.pos = pos
        self.text = text
        self.size = size

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([(j * 100) + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    img = drawALL(img, buttonList)
    
    if hands:
        for hand in hands:
            lmList = hand["lmList"]
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, button.pos, (x+w, y+h), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 12, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 3)
                    
                    # Extract x and y coordinates for landmarks 8 and 12
                    x1, y1 = lmList[8][0], lmList[8][1]
                    x2, y2 = lmList[12][0], lmList[12][1]
                    
                    try:
                        # Calculate distance
                        l, _, _ = detector.findDistance((x1, y1), (x2, y2), img)
                        print(l)

                        # When clicked
                        if l < 54:
                            keyboard.press(button.text)
                            cv2.rectangle(img, button.pos, (x+w, y+h), (0, 255, 0), cv2.FILLED)
                            cv2.putText(img, button.text, (x + 12, y + 65),
                                        cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 3)
                            finalText += button.text
                            sleep(0.15)
                    except Exception as e:
                        print(f"Error calculating distance: {str(e)}")

                cv2.rectangle(img, (50,350), (700,450), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, finalText, (60, 430),
                            cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 3)


    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()