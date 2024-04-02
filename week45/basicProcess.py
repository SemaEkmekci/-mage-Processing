import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
### 1. piksel...
img = cv2.imread("../Images/kertenkele.jpg")
pxl = img[125,125,1]
dim = img.shape
#print(dim)

b = img[:,:,0] # Blue
g = img[:,:,1] #Green
r = img[:,:,2] #Red
# print(b)
cv2.imshow("Animal", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(img)

### 2.Histogram
img = cv2.imread("../Images/kertenkele.jpg")
b = img[:,:,0] # Blue
g = img[:,:,1] #Green
r = img[:,:,2] #Red

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.show()


### 3. ROI
img = cv2.imread("../Images/brain.JPG")
print(img.shape)

cv2.rectangle(img, (150, 175), (250, 275),(0,220,0), 3)
cancernImg = img[175:275,150:250]
#print(cancernImg)

cv2.imshow("Brain", cancernImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


### 4.Image Add
j = cv2.imread("../Images/jerry.jpg")
t = cv2.imread("../Images/tom.jpg")

print("Jerry Shape: ", j.shape)
print("Tom Shape: ", t.shape)

tomAndJerry = cv2.add(t,j)
tomAndJerryWeighted = cv2.addWeighted(t, 0.6, j, 0.4, 0)
jAdded = cv2.add(j, -50)

#cv2.imshow("Tom", t)
cv2.imshow("Jerry", j)
cv2.imshow("Jerry Added", jAdded)
#cv2.imshow("Tom&Jerry", tomAndJerry)
#cv2.imshow("Tom&Jerry Weighted", tomAndJerryWeighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

### 5. Mantıksal İşlemler
img1 = cv2.imread("../Images/img1.jpg")
img2 = cv2.imread("../Images/img2.jpg")
imgAnd = cv2.bitwise_and(img1,img2)
imgOr = cv2.bitwise_or(img1, img2)
imgNot = cv2.bitwise_not(img1)

cv2.imshow("img-1", img1)
cv2.imshow("img-2", img2)
cv2.imshow("img-and", imgAnd)
cv2.imshow("img-or", imgOr)
cv2.imshow("img-not", imgNot)
cv2.waitKey(0)
cv2.destroyAllWindows()


### 6. Görüntü döndürme
img = cv2.imread("../Images/cameraman.jpg", cv2.IMREAD_GRAYSCALE)

r,c = img.shape
rotationRules = cv2.getRotationMatrix2D((125, r/2), 90, 1)
rotatedImg = cv2.warpAffine(img, rotationRules, (c+100,r+100))

cv2.imshow("Cameraman", img)
cv2.imshow("Rotated Cameraman", rotatedImg)

### 7. Filters
img = cv2.imread("../Images/particles.png", cv2.IMREAD_GRAYSCALE)
imgF1 = cv2.blur(img, (11,11))
imgF2 = cv2.medianBlur(img, 5)

cv2.imshow("Particles", img)
cv2.imshow("Mean Filter", imgF1)
cv2.imshow("Median Filter", imgF2)

### 8. Morfolojik İşlemler
img = cv2.imread("../Images/particles.png", 0)
img = cv2.bitwise_not(img)

msk = np.ones((3,3), np.uint8)
msk[:,0] = 0
print(msk)
erosedImg = cv2.erode(img, msk, iterations=1)
dilatedImg = cv2.dilate(img, msk, iterations=1)
openedImg = cv2.morphologyEx(img, cv2.MORPH_OPEN, msk)
closedImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, msk)

cv2.imshow("Particles", img)
#cv2.imshow("Erosed Img", erosedImg)
#cv2.imshow("Dilated Img", dilatedImg)
cv2.imshow("Opened Img", openedImg)
cv2.imshow("Closed Img", closedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

###9. Köşe Tespiti
imgColor = cv2.imread("../Images/img2.jpg")
img = cv2.cvtColor(imgColor, cv2.COLOR_BGR2GRAY)
imgFloat = np.float32(img)
cornrs = cv2.goodFeaturesToTrack(imgFloat, 50, 0.01, 15)
#print(len(cornrs))

for crnr in cornrs:
    x,y = crnr.ravel()
    cv2.circle(imgColor, (int(x),int(y)), 3, (0, 255, 0), -1)

cv2.imshow("Image", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()


### 10. Kenar Tespiti
img = cv2.imread("../Images/cameraman.jpg")
edges = cv2.Canny(img, 50, 150)

#print(edges)

cv2.imshow("Cameraman", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("../Images/brain.JPG")
res, threshImg = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

cv2.imshow("Cameraman", img)
cv2.imshow("Threshold-Img", threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

### 12. Renk Uzayları (Plt Hatalı)
img=cv2.imread("../Images/kertenkele.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

"""
plt.subplot(131)
plt.show(img, cmap = 'gray')
plt.title("Kertenkele")

plt.subplot(132)
plt.show(imgGray, cmap = 'gray')
plt.title("Gray")

plt.subplot(133)
plt.show(imgHsv, cmap = 'gray')
plt.title("HSV")

plt.show()
"""

cv2.imshow("Kertenkele", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("HSV", imgHsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
