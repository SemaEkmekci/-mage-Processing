import cv2
import numpy

## Screen
screen = numpy.zeros((512, 512, 3), dtype=numpy.uint8) + 255
# print(screen)
# Renkler RGB değil, BGR şeklinde kullanılır.
## Line
"""
cv2.line(screen, (25, 25), (100, 25), (100, 100, 255), thickness=2)
cv2.line(screen, (25, 100), (100, 255), (10, 255, 125), 3)

## Rectangle
cv2.rectangle(screen, (75, 75), (175, 175), (255, 0, 255), 2)
cv2.rectangle(screen, (300, 300), (420, 400), (255, 0, 0), -1)

## Circle
cv2.circle(screen, (256, 256), 50, (0, 255, 0), -1)
cv2.circle(screen, (256, 256), 50, (0, 0, 255), 1)

## Elips
cv2.ellipse(screen, (250, 400), (50, 20), 45, 0, 180, (255, 0, 0), -1)

## Triangle
x = (255, 50)
y = (200, 150)
z = (300, 150)
cv2.line(screen, x, y, (0, 0, 255), 2)
cv2.line(screen, y, z, (0, 0 ,255), 2)
cv2.line(screen, z, x, (0, 0 ,255), 2)

## Polylines
points = numpy.array([[50, 350], [100, 350], [125, 375], [75, 400]], numpy.int32)
cv2.polylines(screen, [points], True, (125, 125, 125), 2)
"""

## Text
#cv2.putText(screen, "Goruntu Isleme", (50, 50), cv2.FONT_ITALIC, 1.5, (0, 0 ,255), cv2.LINE_4, 1, True)
cv2.putText(screen, "OpenCV", (25, 25), 4, 1, (0, 255, 0), 1, cv2.LINE_4)


cv2.imshow("Screen", screen)
cv2.waitKey(0)
cv2.destroyAllWindows()