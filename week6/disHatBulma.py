import cv2
import numpy
"""
### 1. Dış Hat Bulma
img = cv2.imread("../Images/img4.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, imgThreshold = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)

cntrs, res = cv2.findContours(imgThreshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

## Alan ve Cevre
cntr = cntrs[2]
mmnts = cv2.moments(cntr)
print(mmnts)
area = mmnts["m00"]
print("Area: ", area)

area = cv2.contourArea(cntr)
print("Area: ", area)

cevre = cv2.arcLength(cntr, True)
print("Perimeter: ", cevre)

centerX = int(mmnts["m10"]/mmnts["m00"])
centerY = int(mmnts["m01"]/mmnts["m00"])

cv2.circle(img, (centerX, centerY), 3, (0, 255, 0), -1)

## Geometrik

#print(cntrs[1])
cv2.drawContours(img, cntrs, -1, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

###2. Nesne Takibi
movie = cv2.VideoCapture("../Movies/kopek.mp4")

while True:
    res, frame = movie.read()
    if not res:
        break

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_limit = numpy.array([0, 0, 220])
    up_limit = numpy.array([255, 15, 255])
    frameMask = cv2.inRange(frameHSV, low_limit, up_limit)
    frameResult = cv2.bitwise_and(frame, frame, mask=frameMask)

    cv2.imshow("Kopek", frame)
    cv2.imshow("Masked", frameResult)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
movie.release()
cv2.destroyAllWindows()

