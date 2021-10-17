import cv2
 
 
image = cv2.imread(r"/Users/genkitakasaki1/Desktop/git/Studio-Incense/Studio-Incense/converter/pic/ano2.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 150, 250, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image = thresh, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_NONE)

image_copy = image.copy()
cv2.drawContours(image = image_copy, contours = contours, 
                 contourIdx = -1, color = (0, 255, 0), 
                 thickness = 2, lineType = cv2.LINE_AA)



cv2.imshow("Img", image_copy)
cv2.imshow("image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()