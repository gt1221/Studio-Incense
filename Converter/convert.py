import cv2
import mediapipe as mp
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

#path is      /Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense

def Mask(x1, y1, x2, y2, height, width):

    result_path = r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/result/mask2.png"

    imgMask = np.zeros((height, width), np.uint8)

    cv2.rectangle(imgMask, (x1, y1), (x2, y2), color = (255), thickness = -1)
    cv2.imwrite(result_path, imgMask)
    

    return result_path

def Inpaint(image, mask):
    print(image)
    print(mask)
    img = cv2.imread(image)
    msk = cv2.imread(mask, 0)

    dst = cv2.inpaint(img, msk, 3, cv2.INPAINT_TELEA)
    cv2.imwrite(r"/Users/genkitakasaki1/Desktop/Python/App2/converter/pic/reslut/inpaint.png", dst)
    print("aaaa")

def Show(image):
    img = cv2.imread(image)

    list_x = []
    list_y = [] 

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                          max_num_hands=2,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                list_x.append(cx), list_y.append(cy)
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
    if not list_x == [] and not list_y == []:
        x1 = min(list_x)
        y1 = min(list_y)
        x2 = max(list_x)
        y2 = max(list_y)
    
    height, width = img.shape[:2]

    """
    print("x1 = {0}, y1 = {1}, x2 = {2}, y2 = {3}".format(x1, y1, x2, y2))
    height, width = img.shape[:2]
    print("width = {0}, height = {1}".format(width, height))
    print(img.shape)
    """

    result_path = Mask(x1, y1, x2, y2, height, width)

    #Inpaint(image, result_path)

    mask = cv2.imread(result_path, 0)
    new = cv2.imread(image)
    dst = cv2.inpaint(new, mask, 3, cv2.INPAINT_TELEA)
    cv2.imwrite(r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/result/kekka2.png", dst)


    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/ore.jpg"
Show(path)