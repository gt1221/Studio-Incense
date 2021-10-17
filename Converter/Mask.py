import cv2

img = cv2.imread(r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/ex.jpg", cv2.IMREAD_COLOR)
#コールバック関数
#マウスイベントが起こるとここへ来る

list_x = []
list_y = []

def printCoor(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        list_x.append(x)
        list_y.append(y)

def Mask():
    ano = img.copy()
    cv2.rectangle(ano, (list_x[0], list_y[0]), (list_x[1], list_y[1]), 
                  (0, 0, 0), thickness=-1)
    cv2.imwrite(r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/ano2.png", ano)


#img = cv2.imread('gazou.bmp')
#画像のウインドウに名前をつけ、コールバック関数をセット
cv2.namedWindow('image')
cv2.setMouseCallback('image',printCoor)
cv2.moveWindow('image', 100, 200)
while(1):
    cv2.imshow('image',img)
    #ESCキーでブレーク
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

Mask()

