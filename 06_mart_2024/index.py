import cv2
import numpy as np
#/read to movie/*******************************************
"""movie = cv2.VideoCapture("video.mp4") #kendi istediğin videoyu koy bu kısma
while True:
    state, frame = movie.read()
    if state == 0:
        break
    frame =  cv2.resize(frame, (480, 480))
    cv2.imshow("car",frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

movie.release()
cv2.destroyAllWindow() #bütün pencereleri kapat"""
#/temel cizim islemleri  /**********************************************
"""screen = np.zeros((512, 512, 3), dtype = np.uint8) + 255
#print(screen)
#renkler rgb değil bgr şeklinde olur
#line
cv2.line(screen, (0, 200), (512, 200), (25, 125, 124), thickness=15)
cv2.line(screen, (25, 100), (100, 255), (10, 255, 125), 3)
#dikdörtgen
cv2.rectangle(screen, (10, 10), (175, 175), (123, 45, 30), 5)
cv2.rectangle(screen, (300, 300), (450, 450), (123, 180, 60), -5) #- değer verince thickness değerine dikdörtgenin içini doldurur
#çember
cv2.circle(screen, (200, 200), 40, (15, 45, 90), 3) # - dersek içi dolu olur
#elips
cv2.ellipse(screen, (250, 400), (50, 20), 45, 0, 270, (255, 0, 0), 2)
#üçgen
x = (400, 60)
y = (90, 80)
z = (300, 40)
cv2.line(screen, x, y, (0, 0, 255), 2)
cv2.line(screen, y, z, (0, 0, 255), 2)
cv2.line(screen, z, x, (0, 0, 255), 2)
#çokgen
points = np.array([[50, 350], [100, 350], [125, 375], [75, 400]], np.int32)
cv2.polylines(screen, [points], False, (0, 125, 255), 3)
#yazı yazdırma ekrana text
cv2.putText(screen, "munire kutlum", (50, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), cv2.LINE_4)

cv2.imshow("sahne", screen)
cv2.waitKey(0)
cv2.destroyAllWindow()"""

#/  track bar yapısı  /**********************************************
"""def emptyFunc(x):
    pass
cv2.namedWindow("screen")
cv2.createTrackbar("F-Size", "screen", 25, 250, emptyFunc)
fs =  0.25
while True:
    img = np.zeros((512, 512, 3), dtype=np.uint8) + 255
    cv2.putText(img, "Open-CV", (100,255), cv2.FONT_HERSHEY_SIMPLEX, fs, (0, 0, 255), cv2.LINE_4)
    cv2.imshow("screen", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    fs = cv2.getTrackbarPos("F-Size", "screen")
    fs = fs/100
#cv2.waitKey(0)
cv2.destroyAllWindows()"""


#/  BOX PLOT  /**********************************************
# minVal = 10
# maxVal = 70
# q1 = 25
# q3 = 45
# medianVal = 30
# offsetHorizontal = 50
# offsetVertical = 400
# coefficient = 5

# screen = np.zeros((600, 600, 3), dtype=np.uint8) + 255
# #sayı doğrusu çizgisi
# cv2.line(screen, (offsetHorizontal, offsetVertical), (450, offsetVertical), (0, 0, 0), 2)
# #min- q1 arası
# cv2.line(screen, (offsetHorizontal + minVal*coefficient, offsetVertical-50), (offsetHorizontal + q1*coefficient, offsetVertical-50), (0, 0, 0), 2)
# #box
# cv2.rectangle(screen, (offsetHorizontal + coefficient*q1, offsetVertical - 75), (offsetHorizontal + coefficient*q3, offsetVertical - 25), (0, 0, 0), 2)
# #median
# cv2.line(screen, (offsetHorizontal + medianVal*coefficient, offsetVertical - 25), (offsetHorizontal + medianVal * coefficient, offsetVertical - 75), (0, 255, 0), 2)
# #q3- max arası
# cv2.line(screen, (offsetHorizontal + q3*coefficient, offsetVertical-50), (offsetHorizontal + maxVal*coefficient, offsetVertical-50), (0, 0, 0), 2)


# cv2.imshow("screen", screen)
# cv2.waitKey(0)
# cv2.destroyAllWindows()